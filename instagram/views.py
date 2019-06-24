from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewImageForm, EditProfile,UpdateProfile

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
  image = Image.objects.all()
  return render(request, 'index.html', {"image":image})

def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        profile = Profile.objects.all()
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message, "profile":searched_profiles, "profile":profile})
    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html', {"message":message})

@login_required(login_url="/accounts/login/")
def profile(request,id):
    image = Image.objects.filter(id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.all()
    try:
      profile3 = Profile.objects.filter(name_id=id)
    except ObjectDoesNotExist:
      return redirect() 
    return render(request, 'profile.html', {"image":image, "user":user, "profile":profile3, "profile":profile})

@login_required(login_url='/accounts/login/')
def upload(request):
   current_user = request.user
   if request.method == 'POST':
       form = NewImageForm(request.POST, request.FILES)
       if form.is_valid():
           image = form.save(commit=False)
           image.user = current_user
           image.save()
       return redirect(home)

   else:
       form = NewImageForm()
   return render(request, 'new-image.html', {"form": form})