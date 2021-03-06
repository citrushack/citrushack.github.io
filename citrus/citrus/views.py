from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

def home(request):
	return render(request, 'home.html', context={}, ) #context is empty unless we want to incorporate data into our landing page

def live(request):
    return render(request, 'live.html', context={}, )

def expo(request):
    return render(request, 'expo.html', context={}, )

def mentor(request):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScp0a5PhwBc-36Im7HkytyqlvTiQSPnNIg3rtaHlSVAPn3U1g/viewform")

def volunteer(request):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdK66VnO-NYPyL_qN8P3GZYUuehluLNB_dgDpiQx9anj8OP3A/viewform")

def workshop(request):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeb5P1dlnnsWL6IPdsZsb3KhGBqL4TKIA8I-p9LoRVndTHVEA/viewform")
