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
    profile = models.ForeignKey(Profile)
  
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Comments(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.IntegerField()

    def __str__(self):
        return self.comment
    
    def save_comments(self):
        self.save()

class Followers(models.Model):
    user = models.CharField(max_length=20, default="")
    follower = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.follower
    
    def save_followers(self):
        self.save()

