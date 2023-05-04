from django.contrib import admin
from django.urls import path, include
import main_app
import account_app.views
from django.contrib.auth import authenticate, login, logout
import django.contrib.auth.urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('singup/', account_app.views.singupPage, name="singup"),
    path('login/', account_app.views.loginPage, name="login"),
    path('logout/', account_app.views.logout, name="logout"),
    path('profile/<str:user>/', account_app.views.UserProfile, name='user_profile'),
    path('profile/<str:user>/edit/', account_app.views.EditProfile, name='edit_profile'),
    path('reset_password_send/', account_app.views.ResetPasswordSend, name="reset_password_send"),
    path('reset_password/', account_app.views.ResetPassword, name="reset_password"),
    path('new_password/', account_app.views.NewPassword, name="new_password"),
    path('forget_password_send/', account_app.views.ForgetPasswordSend),
    path('forget_password/', account_app.views.ForgetPassword),
    path('new_password_forget/', account_app.views.NewPasswordAfterForget),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

