# Generated by Django 2.1.5 on 2019-01-30 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('app_status', models.CharField(default='PENDING', max_length=30)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(default='', max_length=50)),
                ('level_of_study', models.CharField(choices=[(None, ''), ('Undergraduate', 'Undergraduate'), ('Graduate', 'Graduate'), ('High School', 'High School'), ('Prefer not to disclose', 'Prefer not to disclose')], max_length=30)),
                ('graduation_year', models.CharField(choices=[(None, ''), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023 or later', '2023 or later'), ('Prefer not to disclose', 'Prefer not to disclose')], default='', max_length=30)),
                ('major', models.CharField(default='', max_length=30)),
                ('gender', models.CharField(choices=[(None, ''), ('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'), ('Prefer not to disclose', 'Prefer not to disclose')], default='', max_length=30)),
                ('date_of_birth', models.CharField(default='', max_length=10)),
                ('race', models.CharField(choices=[(None, ''), ('Asian/Pacific Islander', 'Asian/Pacific Islander'), ('Black or African American', 'Black or African American'), ('Hispanic', 'Hispanic'), ('Native American', 'Native American'), ('White/Caucasian', 'White/Caucasian'), ('Other', 'Other'), ('Prefer not to diclose', 'Prefer not to disclose')], default='', max_length=30)),
                ('phone_number', models.CharField(default='', max_length=12)),
                ('shirt_size', models.CharField(choices=[(None, ''), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='', max_length=3)),
                ('dietary_restrictions', models.CharField(blank=True, default='', max_length=100)),
                ('linkedin', models.URLField(blank=True, default='')),
                ('github', models.URLField(blank=True, default='')),
                ('additional_link', models.URLField(blank=True, default='', max_length=500)),
                ('description', models.CharField(default='', max_length=200)),
                ('learn_or_gain', models.CharField(default='', max_length=250)),
                ('resume', models.URLField(blank=True, default='', max_length=500)),
                ('conduct_box', models.BooleanField(null=True)),
                ('share_box', models.BooleanField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
