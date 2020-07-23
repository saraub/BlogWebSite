from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,CustomerForm,BlogForm,CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from .decorators import*
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



from .models import *

# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
 
    
    return render(request,'store/home.html')


def store(request):
    
    blogposts= Item.objects.all()
    for blog in blogposts:
        if blog.likes.filter(id=request.user.id).exists():
            blog.is_liked=True
            
        else:
            blog.is_liked=False
            

            
    
    context= {"blogposts":blogposts}
    return render(request, 'store/store.html',context)



def contact(request):
    return render(request, 'store/contact.html')

@unauthenticated_user
def registerPage(request):
 
        
    
        form= CreateUserForm()
        
        
        if request.method == 'POST':
            form= CreateUserForm(request.POST)
            
            if form.is_valid():
                user= form.save()
                username= form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                
                Customer.objects.create(
                    user=user,
                    
				)
                messages.success(request,'Account has been created for'+ username)
                return redirect('login')
                
        
        context={'form': form}
        return render(request, 'store/register.html',context)
    
   
@unauthenticated_user
def loginPage(request):
    
    if request.method=='POST':
       username= request.POST.get('username')
       password= request.POST.get('password')
       
       
           
       user=authenticate(request, username=username,password= password)
       if user is not None:
            login(request, user)
            return redirect('home')
       else:
           messages.info(request, 'Username or Password is incorrect')
           
    
    context = {}
    return render(request, 'store/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def userPage(request):

    user=request.user.customer
    
    likedpost=Item.objects.filter(likes=request.user.id)
    blogposts= Item.objects.filter(user=request.user)
    context= {'blogposts':blogposts,'user':user,'likedpost':likedpost}
    return render(request,'store/user.html',context)
def delete(request,blog_id):
    item=Item.objects.get(id=blog_id)
    if request.POST:
        item.delete()
        return redirect('home')
    context={'item':item}
    return render(request,'store/blog_delete.html',context)


@login_required(login_url='login')
def profile_settings(request):
    customer= request.user.customer
    form= CustomerForm(instance=customer)
    
    if request.method=='POST':
        form= CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context={'form':form}
    return render(request,'store/profile_settings.html',context)


def comment(request):
    form=CommentForm()
    
    if request.method=='POST':
        form= CommentForm(request.POST)
        blog=Item.objects.filter(id=request.POST.get('blog_id'))
            
        
        if form.is_valid():
  
            instance= form.save(commit=False)
            instance.user=request.user
            instance.item_in=Item.objects.filter(id=blog)
            instance.save()
            
            return redirect('home')

    context={'form':form}
    return render(request,'store/comment.html',context)


def likes(request):
    blog=get_object_or_404(Item,id=request.POST.get('blog_id'))
    
    
    if blog.likes.filter(id=request.user.id).exists():
           
        blog.likes.remove(request.user)
        blog.is_liked=False
    else:
        blog.likes.add(request.user)
        blog.is_liked=True
        
   
    return redirect('store')    
    
    

@login_required(login_url='login')
def blog_creation(request):
    
    form= BlogForm()
   
    
    if request.method=='POST':
        
         form= BlogForm(request.POST)
        
         if form.is_valid():

                instance= form.save(commit=False)
                instance.user=request.user
                instance.save()
                
                return redirect('home')
        
    context={'form': form}
    return render(request, 'store/create_blog.html',context)



def blog_edit(request,blog_id):
    
    item=Item.objects.get(id=blog_id)
    
    
    form= BlogForm(instance=item)
    if request.method=='POST':
        form= BlogForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
     
    context={'form':form,'item':item}
 
    return render(request,'store/blog_edit.html',context)