# Generated by Django 4.2.5 on 2023-09-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_database', '0002_alter_trash_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active_profile',
            name='image',
            field=models.ImageField(default='avatars', upload_to='profil_pic'),
        ),
    ]
