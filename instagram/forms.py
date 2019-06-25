from .models import Image, Profile,Comment
from django import forms
from django.forms import ModelForm, Textarea, IntegerField


class NewImageForm(forms.ModelForm):
   class Meta:
       model = Image
       fields =('image','image_name','caption')
class EditProfile(forms.ModelForm):
   class Meta:
       model=Profile
       exclude=['']

class UpdateProfile(forms.ModelForm):
   class Meta:
       model=Profile
       exclude=['']

class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       exclude = ['user','image','posted_on']

