from django import forms
from django.contrib.auth.models  import User
from . models import UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-control'
    }))

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder':'Enter Confirm Password',
        'class':'form-control'
    }))


    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
    
    def clean(self):
       cleaned_data =  super(RegistrationForm,self).clean()
       password = cleaned_data.get('password')
       confirm_password = cleaned_data.get('confirm_password')

       if password != confirm_password:
           raise forms.ValidationError("password and confirm password does not match")
           

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = "Enter First Name"
        self.fields['last_name'].widget.attrs['placeholder'] = "Enter Last  Name"
        self.fields['email'].widget.attrs['placeholder'] = "Enter Email"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

    def clean(self):
       cleaned_data =  super(UserForm,self).clean()

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

class UserProfileForm(forms.ModelForm):

    profile_picture = forms.ImageField(required=False, 
                        error_messages={'invalid':("Image files Only")}, widget=forms.FileInput)
   
    class Meta:
        model = UserProfile
        fields = ['address_line_1','address_line_2','profile_picture','city','state','country','zipcode','phoneno']
    
    def clean(self):
       cleaned_data =  super(UserProfileForm,self).clean()

    def __init__(self,*args,**kwargs):
        super(UserProfileForm,self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"





