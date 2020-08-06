from django.urls import path

from . import views

urlpatterns = [
    
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('user/', views.userPage, name="userpage"),
    path('blog_delete/<blog_id>', views.delete, name="delete"),
    path('profile/', views.profile_settings, name="profile_settings"),
    path('blog_edit/<blog_id>/',views.blog_edit, name='blog_edit'),
    path('comment/',views.comment, name='comment'),
    path('likes/', views.likes, name="likes"),
    path('blog_create/', views.blog_creation, name="blog_creation"),
    
    
    
]
