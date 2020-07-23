from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Comment)
