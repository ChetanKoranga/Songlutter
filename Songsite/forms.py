from django.contrib.auth.models import User
from django.forms import *

class UserForm(ModelForm):
    password =  CharField(widget=PasswordInput)
    class meta:
        model = User
        fields = ['username','password','email']
