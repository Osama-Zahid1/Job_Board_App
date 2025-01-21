from django.contrib import admin
from .models import Seekermodel,Recruitermodel,Jobmodel

@admin.register(Seekermodel)
class Seekeradmin(admin.ModelAdmin):
    list_display=['username', 'email', 'address', 'degree',"resume",'pic']
@admin.register(Recruitermodel)
class Recruiteradmin(admin.ModelAdmin):
    list_display=['username', 'email', 'businessname', 'businesstype']
@admin.register(Jobmodel)
class jobadmin(admin.ModelAdmin):
   list_display=['jobtitle', 'jobdesp', 'skillsreq', 'businessadd',"salary"]