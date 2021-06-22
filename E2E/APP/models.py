from django.db import models
from django.contrib.auth.models import User

class user_registery_model(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='media/', blank=True)
    profile_site=models.URLField(blank=True)

    def __str__(self):

        return self.user
# Create your models here.
