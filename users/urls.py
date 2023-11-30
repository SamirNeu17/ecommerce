from django.urls import path
import users.views as user_views

urlpatterns = [
    path("",user_views.index, name="index"),
    path("login",user_views.login,name="login"),
    path("user_register",user_views.user_register,name="user_register"),
]