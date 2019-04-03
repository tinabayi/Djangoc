
from django import forms
from .models import Profile,Image,Comment



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'projects_posted' ,'contact_information']
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments','likes','user','profile' ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image' ]
    
      