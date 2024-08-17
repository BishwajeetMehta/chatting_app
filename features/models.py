from django.db import models
from custom_auth.models import User

# Create your models here.


class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    started_date =models.DateField()
    completed_date = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.institution
    

class Work(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    office_name = models.CharField(max_length=100)
    position = models.CharField(max_length=75)
    started_date =models.DateField()
    completed_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.office_name
    

class FriendRequest(models.Model):
   from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
   to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
   status = models.CharField(max_length=15,default="pending")
   created_at = models.DateTimeField(auto_now_add=True)