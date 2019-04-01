
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import User

@login_required(login_url='/accounts/login/')
def welcome(request):

    return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
   
    return render(request,'my_profile.html',{"profiles":profiles,"user":user})

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
