from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
  image = Image.objects.all()
  return render(request, 'index.html', {"image":image})

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "profile":searched_profiles})
    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html', {"message":message})

def profile(request,id):
    image = Image.objects.filter(id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    try:
      profile = Profile.objects.get(name_id=id)
    except ObjectDoesNotExist:
      return redirect() 
    return render(request, 'profile.html', {"image":image, "user":user, "profile":profile})
