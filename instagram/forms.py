from .models import Image, Profile
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

