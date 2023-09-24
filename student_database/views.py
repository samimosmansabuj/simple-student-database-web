from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import os

# Create your views here.
def index(request):
    all_prof = active_profile.objects.all()
    if request.method == 'GET':
        search_kay = request.GET.get('search_bar')
        if search_kay:
            all_prof = active_profile.objects.filter(name__icontains = search_kay)
        elif search_kay == 'None':
            return redirect('indext')
        else:
            all_prof = active_profile.objects.all()

    return render(request, 'index.html', locals())


def profile_details(request, id):
    select_prof = active_profile.objects.get(id=id)

    return render(request, 'profile_details.html', locals())



# Add New File Start------------------------------------------------
def add_new(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_name = request.POST.get('course_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')

        address_street = request.POST.get('address_street')
        upazila = request.POST.get('upazila')
        district = request.POST.get('district')
        address = f'{address_street}, {upazila}, {district}'

        if active_profile.objects.filter(phone_number=phone_number).exists():
            messages.warning(request, 'This Phone Number is already taken!')
        elif active_profile.objects.filter(email=email).exists():
            messages.warning(request, 'This Email Address is already taken!')
        else:
            if image:
                active_profile.objects.create(
                name = name,
                phone_number = phone_number,
                email = email,
                image = image,
                date_of_birth = date_of_birth,
                gender = gender,
                occupation = occupation,
                address = address,
                course_name = course_name
                )
                messages.success(request, 'Account Create Successfully!')
                return redirect('index')
            else:
                active_profile.objects.create(
                name = name,
                phone_number = phone_number,
                email = email,
                date_of_birth = date_of_birth,
                gender = gender,
                occupation = occupation,
                address = address,
                course_name = course_name
                )
                messages.success(request, 'Account Create Successfully!')
                return redirect('index')

    return render(request, 'add_new.html', locals())
# Add New File End------------------------------------------------



# Update Profile File Start------------------------------------------------
def update_profile(request, id):
    select_porf = active_profile.objects.get(id=id)

    full_address = select_porf.address.split(',')
    address_street = full_address[0]
    address_upazila = full_address[1]
    address_district = full_address[2]

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')
        course_name = request.POST.get('course_name')

        address_street = request.POST.get('address_street')
        upazila = request.POST.get('upazila')
        district = request.POST.get('district')
        full_address = f'{address_street}, {upazila}, {district}'

        select_porf.name = name
        select_porf.phone_number = phone_number
        select_porf.email = email
        select_porf.gender = gender
        select_porf.occupation = occupation
        select_porf.address = full_address
        select_porf.course_name = course_name
        if image:
            if select_porf.image != 'profile_default_icon.png':
                os.remove(select_porf.image.path)
            select_porf.image = image

        select_porf.save()
        messages.success(request, 'Profile Update Successfully!')

    return  render(request, 'update_profile.html', locals())
# Update Profile File End------------------------------------------------


# Delete Profile File Start------------------------------------------------
def delete(request, id):
    del_prof = active_profile.objects.get(id=id)

    trash_profile.objects.create(
        name = del_prof.name,
        phone_number = del_prof.phone_number,
        image = del_prof.image,
        email = del_prof.email,
        date_of_birth = del_prof.date_of_birth,
        gender = del_prof.gender,
        occupation = del_prof.occupation,
        address = del_prof.address,
        course_name = del_prof.course_name,
        previous_id = del_prof.id
    )
    del_prof.delete()
    return redirect('index')
# Delete Profile File End------------------------------------------------


# Restore Profile File Start------------------------------------------------
def restore(request, id):
    restore_prof = trash_profile.objects.get(id=id)

    active_profile.objects.create(
        name = restore_prof.name,
        phone_number = restore_prof.phone_number,
        image = restore_prof.image,
        email = restore_prof.email,
        date_of_birth = restore_prof.date_of_birth,
        gender = restore_prof.gender,
        occupation = restore_prof.occupation,
        address = restore_prof.address,
        course_name = restore_prof.course_name,
        id = restore_prof.previous_id
    )
    restore_prof.delete()
    return redirect('inactive_profile')
# Restore Profile File End------------------------------------------------


# Permanent Delete Profile File Start------------------------------------------------
def p_delete(request, id):
    p_delete_prof = trash_profile.objects.get(id=id)
    if p_delete_prof.image != 'profile_default_icon.png':
        os.remove(p_delete_prof.image.path)
    p_delete_prof.delete()
    return redirect('inactive_profile')
# Permanent Delete Profile File End------------------------------------------------



# Inactive Profile File Start------------------------------------------------
def inactive_profile(request):
    inactive_prof = trash_profile.objects.all()

    return render(request, 'inactive_profile.html', locals())
# Inactive Profile File End------------------------------------------------

