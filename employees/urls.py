from django.urls import path
from .views import (
    StaffRoleList,
    ManagerListCreateView, ManagerRetrieveUpdateDestroyView,
    InternListCreateView, InternRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('staff/', StaffRoleList.as_view(), name='staff-role-list'),

    # CRUD for Manager
    path('managers/', ManagerListCreateView.as_view(), name='manager-list-create'),
    path('managers/<int:pk>/', ManagerRetrieveUpdateDestroyView.as_view(), name='manager-detail'),

    # CRUD for Intern
    path('interns/', InternListCreateView.as_view(), name='intern-list-create'),
    path('interns/<int:pk>/', InternRetrieveUpdateDestroyView.as_view(), name='intern-detail'),
]