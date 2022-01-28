from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(models.Model):
    # user = username, email, password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other feilds
    address = models.CharField(max_length=20,blank=True)
    department = models.CharField(max_length=15, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username
