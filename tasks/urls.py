from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('clubs/', views.club_list, name='club_list'),
    path('clubs/create/', views.club_create, name='club_create'),
    path('clubs/<int:pk>/edit/', views.club_update, name='club_update'),
    path('clubs/<int:pk>/delete/', views.club_delete, name='club_delete'),
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/create/', views.enrollment_create, name='enrollment_create'),
    path('enrollments/delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

]