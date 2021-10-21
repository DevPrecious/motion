from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from app.models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'firstname', 'lastname', 'password1', 'password2')

class UserLoginFrom(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Credentials")

class ProofForm(forms.ModelForm):
    class Meta:
        model = Proof
        fields = ['username', 'image']