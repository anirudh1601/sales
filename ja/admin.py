from django.contrib import admin
from .models import Sales,SalesForceModel
# Register your models here.
admin.site.register(SalesForceModel)
admin.site.register(Sales)