from django.contrib import admin
from . models import Education,Work,FriendRequest
# Register your models here.

@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display =("id","user","institution","started_date","completed_date")

@admin.register(Work)
class Work(admin.ModelAdmin):
    list_display = ("id","office_name","position","started_date","completed_date")

@admin.register(FriendRequest)
class FriendRequest(admin.ModelAdmin):
    list_display= ("id","from_user","to_user","status","created_at")