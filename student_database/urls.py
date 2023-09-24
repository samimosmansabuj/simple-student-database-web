from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_new/', add_new, name='add_new'),
    path('update_profile/<int:id>/', update_profile, name='update_profile'),
    path('profile_details/<int:id>:', profile_details, name='profile_details'),
    path('inactive_profile/', inactive_profile, name='inactive_profile'),
    path('delete/<int:id>/', delete, name='delete'),
    path('restore/<int:id>', restore, name='restore'),
    path('p_delete/<int:id>/', p_delete, name='p_delete'),
]