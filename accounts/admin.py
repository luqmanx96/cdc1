from django.contrib import admin

# Register your models here.

from .models import *  # * imports everything in the file

admin.site.register(Customer)
admin.site.register(Product)
