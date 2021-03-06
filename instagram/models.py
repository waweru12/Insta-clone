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
    caption= models.CharField(max_length =200)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    
  
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Comment(models.Model):
    image = models.ForeignKey('Image')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.comment


    def save_comment(self):
        self.save()
    
    def delete_comment(self):
        self.delete()
