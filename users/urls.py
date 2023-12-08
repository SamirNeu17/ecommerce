from django.urls import path
import users.views as user_views

urlpatterns = [
    path("",user_views.index, name="index"),
    path("login",user_views.user_login,name="login"),
    path("register",user_views.register,name="register"),
    path("profile",user_views.user_profile,name="profile"),
]