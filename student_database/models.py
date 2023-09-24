from django.db import models


# Create your models here.
class active_profile(models.Model):
    YOUR_OCCUPATION = (
        ('Student', 'Student'),
        ('Job Holder', 'Job Holder'),
        ('Business', 'Business'),
        ('Teacher', 'Teacher'),
        ('Unemployed', 'Unemployed')
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    name = models.CharField(max_length=30)
    phone_number = models.TextField(max_length=14)
    email = models.EmailField(max_length=40)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='profil_pic', default='profile_default_icon.png')
    gender = models.CharField(choices=GENDER, max_length=10, default='Male')
    occupation = models.CharField(choices=YOUR_OCCUPATION, max_length=10, default='Student')
    address = models.TextField(max_length=100)
    course_name = models.CharField(max_length=30)



    def __str__(self) -> str:
        return self.name


class trash_profile(models.Model):
    YOUR_OCCUPATION = (
        ('Student', 'Student'),
        ('Job Holder', 'Job Holder'),
        ('Business', 'Business'),
        ('Teacher', 'Teacher'),
        ('Unemployed', 'Unemployed')
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    name = models.CharField(max_length=30)
    phone_number = models.TextField(max_length=14)
    email = models.EmailField(max_length=40)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='profil_pic', default='profile_default_icon.png')
    gender = models.CharField(choices=GENDER, max_length=10, default='Male')
    occupation = models.CharField(choices=YOUR_OCCUPATION, max_length=10, default='Student')
    address = models.TextField(max_length=100)
    course_name = models.CharField(max_length=30)
    previous_id = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.name
