from django.urls import path
from .views import StaffRoleList

urlpatterns = [
    path('staff/', StaffRoleList.as_view(), name='staff-role-list'),
]