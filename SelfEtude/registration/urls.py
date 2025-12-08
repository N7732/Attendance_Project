from django. urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('', views.LoginView, name='login'),
    path('home/', views.home, name='home'),
    path('attendance/', views.do_attendance, name='do_attendance'),
    path('admin/open-attendance/', views.open_attendance, name='open_attendance'),]