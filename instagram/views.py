from django.shortcuts import render
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
  image = Image.objects.all()
  return render(request, 'index.html', {"image":image})