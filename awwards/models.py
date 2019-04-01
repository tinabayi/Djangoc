from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prof_picture = models.ImageField(upload_to = 'images/',null=True)
    user_bio = models.CharField(max_length =200)
    projects_posted=  models.IntegerField()
    contact_information=models.CharField(max_length=30,null=True)
   