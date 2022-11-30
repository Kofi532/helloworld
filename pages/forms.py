from django import forms
from .models import Post, Clubm, Sportm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["surname", "firstname", "email", "message"]

class Clubs(forms.ModelForm):

    class Meta:
        model = Clubm
        fields = ["username", "surname", "firstname", "level", "title", "message", "image", "approve", "act" ]
        
        widgets = {
            'approve': forms.TextInput(attrs={'type': 'hidden'}),
            'date': forms.TextInput(attrs={'type': 'hidden'}),
            'act': forms.TextInput(attrs={'type': 'hidden'}),
        }
class Sports(forms.ModelForm):

    class Meta:
        model = Sportm
        fields = ["username", "surname", "firstname", "level", "title", "message", "image", "approve", "act"]
        widgets = {
            'approve': forms.TextInput(attrs={'type': 'hidden'}),
            'date': forms.TextInput(attrs={'type': 'hidden'}),
            'act': forms.TextInput(attrs={'type': 'hidden'}),
        }

