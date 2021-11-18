from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('registration/', views.UserRegisterView.as_view(), name="registration"),
    path('logout/', authViews.LogoutView.as_view(next_page='home'), name='exit'), 
    path('edit/', views.UserEditView.as_view(), name="edit"),
    path('password/', views.PasswordChangeView.as_view(), name="password"),
] 
