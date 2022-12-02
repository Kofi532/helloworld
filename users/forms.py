from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

levell = (
    ('Class 1', 'Class 1'),
    ('Class 2', 'Class 2'),
    ('Class 3', 'Class 3'),
    ('Class 4', 'Class 4'),
    ('Class 5', 'Class 5'),
    ('Class 6', 'Class 6'),
    ('J.H.S 1', 'J.H.S 1'),
    ('J.H.S 2', 'J.H.S 2'),
    ('J.H.S 3', 'J.H.S 3'),
)

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    level = forms.ChoiceField(choices=[levell])
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'level', 'email', 'password1', 'password2']