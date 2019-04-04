
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comment
from .forms import ProfileForm,NewImageForm,CommentForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ImageSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# from django.contrib.auth import User

@login_required(login_url='/accounts/login/')
def welcome(request):

    projects = Image.objects.all()
    comments=Comment.objects.all()

    return render(request, 'welcome.html',{"projects":projects,"comments":comments})



def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(welcome)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def viewprofile(request,id):

    user = User.objects.get(id = id)
    profile = Profile.objects.get(user = user)
    return render(request, 'viewprofile.html',{"profile":profile,"user":user})
    
@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

    else:
        form = ImageForm()
    return render(request, 'image.html', {"form": form})

def search_results(request):

    if 'project_name' in request.GET and request.GET["project_name"]:
        search_term = request.GET.get("project_name")
        searched_projects = Image.search_by_project_name (search_term)
        message = f"{search_term}"

        return render(request, 'all-awwards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awwards/search.html',{"message":message})


def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = current_user
            comments.save()

            return redirect(welcome)

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form})


def project(request,project_id):
    try:
        project = Image.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-awwards/project.html", {"project": project})  

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class ImageList(APIView):

    def get(self, request, format=None):
        all_project = Image.objects.all()
        serializers = ImageSerializer(all_project, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = ImageSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
