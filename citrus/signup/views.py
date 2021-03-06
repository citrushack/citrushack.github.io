from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import SignUpForm
from .forms import ProfileForm
from .forms import ProfileEditForm
from .tokens import account_activation_token
from django.db import transaction
import os
from django.conf import settings
from .models import Profile
from .models import MyUser
# Create your views here.

def profile(request): #when user is not logged in redirect to login page 
	if not request.user.is_authenticated:
	    return redirect('login')
	return render(request, 'signup/profile.html', context={}, )

@transaction.atomic
def apply(request):
    if request.method == 'POST':
       user_form = SignUpForm(request.POST)
       profile_form = ProfileForm(request.POST)
       if user_form.is_valid() and profile_form.is_valid():
           user = user_form.save()
           #user.is_active = False
           user.refresh_from_db()  # load the profile instance created by the signal
           profile_form = ProfileForm(request.POST, instance=user.profile)
           profile_form.full_clean()
           profile_form.save()
           #user.save()
           #current_site = get_current_site(request)
           #subject = 'Activate Your CitrusHack Account'
           #message = render_to_string('signup/account_activation_email.html', {
           #    'user': user,
           #    'domain': current_site.domain,
           #    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
           #    'token': account_activation_token.make_token(user),
           #})
           #user.email_user(subject, message)
           login(request, user)
           return redirect('profile')
    else:
       user_form = SignUpForm()
       profile_form = ProfileForm()
    #return render(request, 'signup/dummyapply.html', {'user_form': user_form, 'profile_form': profile_form})
    return render(request, 'signup/apply.html', {'user_form': user_form, 'profile_form': profile_form})

@transaction.atomic
def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
       #     messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
       # else:
       #     messages.error(request, _('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'signup/edit.html', { 'profile_form': profile_form })

def account_activation_sent(request):
    return render(request, 'signup/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('profile')
    else:
        return render(request, 'signup/account_activation_invalid.html')
