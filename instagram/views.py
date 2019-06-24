from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Image,Profile,Comments, Followers, PhotoLikes
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import NewImageForm, EditProfile,UpdateProfile,CommentForm,Likes,FollowForm

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
      profile = Profile.objects.filter(name_id=id)
    except ObjectDoesNotExist:
      return redirect() 
    return render(request, 'profile.html', {"image":image, "user":user, "profile":profile})
    
@login_required(login_url="/accounts/login/")
def comments(request,image_id):
    try:
        image=Image.objects.filter(id=image_id).all()
        comment=Comments.objects.filter(images=image_id).all()
    except Exception as e:
        raise  Http404()
    imag=Image.objects.filter(id=image_id).all()
    count=0
    for i in imag:
        count+=i.likes
    if request.method=='POST':
        form=Likes(request.POST)
        k=request.POST.get("like","")
        if k:
            if form.is_valid:
                likes=form.save(commit=False)
                current_user=request.user
                postid=image_id
                if not PhotoLikes.objects.filter(liker=current_user, postid=postid).exists():
                    Image.objects.filter(id=postid).update(likes=F('likes')+1)
                    like = PhotoLikes(postid=postid, liker=current_user)
                    like.save()
                else:
                    Image.objects.filter(id=postid).update(likes=F('likes')-1)
                    PhotoLikes.objects.filter(postid=postid, liker=current_user).delete()
                return redirect('comment',image_id)
    else:
        forms=Likes()
    if request.method=='POST':
        current_user=request.user
        i=request.POST.get("id","")
        form=CommentForm(request.POST)
        if form.is_valid:
            comments=form.save(commit=False)
            comments.user=current_user
            comments.images=i
            comments.save()
            return redirect('comment',image_id)
    else:
        form=CommentForm()
    return render(request,"comment.html",{"images":image,'form':form,"comments":comment,"count":count,"forms":forms})