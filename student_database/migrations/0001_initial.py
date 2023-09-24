# Generated by Django 4.2.5 on 2023-09-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='active_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.TextField(max_length=14)),
                ('image', models.ImageField(default='profile_default_icon.png', upload_to='profil_pic')),
                ('email', models.EmailField(max_length=40)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=10)),
                ('occupation', models.CharField(choices=[('Student', 'Student'), ('Job Holder', 'Job Holder'), ('Business', 'Business'), ('Teacher', 'Teacher'), ('Unemployed', 'Unemployed')], default='Student', max_length=10)),
                ('address', models.TextField(max_length=100)),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='trash_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.TextField(max_length=14)),
                ('image', models.ImageField(default='profile_default_icon.png', upload_to='profil_pic')),
                ('email', models.EmailField(max_length=40)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=10)),
                ('occupation', models.CharField(choices=[('Student', 'Student'), ('Job Holder', 'Job Holder'), ('Business', 'Business'), ('Teacher', 'Teacher'), ('Unemployed', 'Unemployed')], default='Student', max_length=10)),
                ('address', models.TextField(max_length=100)),
                ('course_name', models.CharField(max_length=30)),
                ('previous_id', models.IntegerField(default=0)),
            ],
        ),
    ]