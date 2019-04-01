from .models import Profile



class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'projects_posted' ,'contact_information']