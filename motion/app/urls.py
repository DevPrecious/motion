from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('logout/', views.logoutPage, name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name = 'app/forgot.html'
    ), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'app/sent.html'
    ), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'app/set.html'
    ), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'app/done.html'
    ), name="password_reset_complete"),
]
