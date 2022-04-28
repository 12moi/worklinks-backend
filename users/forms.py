from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Comment, Jobseeker, Employer,Post, Profile



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('name', 'email', 'Phone no', 'Address','password','confirmpassword')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['Full_name','Address','Email','Contact','Profile_image','Upload_Image']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employer
        exclude = ['user']

class JobseekerForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        exclude = ('user', 'bio','Education', 'Work_experience','skills','References','avalaibility','salary_expections','Job_category')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']