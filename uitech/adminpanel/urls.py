from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, AdminDashboardView, SmartHiringView, DetailHiringView, CreateHiringView, EditHiringView, DeleteHiringView, InternsView, InternsDetailView, CreateInternView, EditInternView, DeleteInternView


app_name = 'adminpanel'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('smart_hiring/', SmartHiringView.as_view(), name='smart_hiring'),
    path('hiring_detail/<int:pk>/', DetailHiringView.as_view(), name='hiring_detail'),
    path('create_hiring/', CreateHiringView.as_view(), name='create_hiring'),
    path('edit_hiring/<int:pk>/', EditHiringView.as_view(), name='edit_hiring'),
    path('delete_hiring/<int:pk>/', DeleteHiringView.as_view(), name='delete_hiring'),
    #URLs for Internship Students
    path('interns_list/', InternsView.as_view(), name='interns_list'),
    path('interns_detail/<int:pk>/', InternsDetailView.as_view(), name='interns_detail'),
    path('create_intern/', CreateInternView.as_view(), name='create_intern'),
    path('edit_intern/<int:pk>/', EditInternView.as_view(), name='edit_intern'),
    path('delete_intern/<int:pk>/', DeleteInternView.as_view(), name='delete_intern'),
    path('logout/', LogoutView.as_view(), name= 'logout'),
]