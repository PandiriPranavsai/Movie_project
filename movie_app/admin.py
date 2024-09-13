from django.contrib import admin


from .models import *

# Register your models here.



class StudentAdmin(admin.ModelAdmin):
      list_display=['rdate','hero','heroine','rating','Moviename']
      

admin.site.register(Movie)
