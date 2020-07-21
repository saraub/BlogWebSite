from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('user/', views.userPage, name="userpage"),
    path('profile/', views.profile_settings, name="profile_settings"),
    path('blog_create/', views.blog_creation, name="blog_creation"),
    
    
    
]