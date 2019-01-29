# Generated by Django 2.1.5 on 2019-01-29 01:12

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
                ('email_confirmed', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('age', models.CharField(blank=True, max_length=30, null=True)),
                ('school', models.CharField(blank=True, max_length=100)),
                ('major', models.CharField(blank=True, max_length=30)),
                ('appStatus', models.CharField(default='Pending', max_length=30)),
                ('phoneNumber', models.CharField(blank=True, max_length=12)),
                ('Gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'), ('Prefer not to disclose', 'Prefer not to disclose')], max_length=30)),
                ('Race', models.CharField(blank=True, choices=[('Asian', 'Asian'), ('Black or African American', 'Black or African American'), ('Latino or Latin American', 'Latino or Latin American'), ('Native American', 'Native American'), ('Native Hawaiian or other Pacific Islander', 'Native Hawaiian or other Pacific Islander'), ('Other', 'Other'), ('Prefer not to diclose', 'Prefer not to disclose'), ('Two or more races', 'Two or more races'), ('White', 'White')], max_length=30)),
                ('LevelofStudy', models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('5th Year or beyond', '5th Year or beyond'), ('Prefer not to disclose', 'Prefer not to disclose')], default='', max_length=30)),
                ('gradYear', models.CharField(choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='', max_length=30)),
                ('dietRestrictions', models.CharField(default='', max_length=100)),
                ('Resume', models.URLField(blank=True, max_length=500)),
                ('conductBox', models.BooleanField(default=False)),
                ('shareBox', models.BooleanField(default=False)),
                ('meme', models.URLField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]