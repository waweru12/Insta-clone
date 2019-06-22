from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to = 'instagram/')
    bio = models.CharField(max_length=250)
    
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()



class Image(models.Model):
    image = models.ImageField(upload_to = 'instagram/')
    image_name = models.CharField(max_length =60)
    profile= models.ForeignKey(Profile)
    caption= models.CharField(max_length =200)
    comment = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile)
  
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()