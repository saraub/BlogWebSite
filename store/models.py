from django.db import models
from django.contrib.auth.models import User





class Customer(models.Model):
    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=50, default='NAME')
    profile = models.CharField(max_length=2000,null=True)
    image = models.ImageField( default ="profile.jpg", null=True, blank=True)
    facebok=  models.CharField(max_length=2000,null=True)
    twitter=  models.CharField(max_length=2000,null=True)
    
    def __str__(self):
        return self.name


class Item (models.Model):
    user= models.ForeignKey(User, default=None, null=True, blank=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=200,null=False)
    shortdescription= models.CharField(max_length=500, null=False)
    content = models.CharField(max_length=5000, null=False,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    is_liked=models.BooleanField(default=False)
    
    

    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    content=models.CharField(max_length=2000,null=True)
    item=models.ForeignKey(Item, default=None, null=True, blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content