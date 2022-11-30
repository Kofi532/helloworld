from django import forms
from .models import Post, Cals

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["Approve","Comments", "date"]

class Event(forms.ModelForm):
    class Meta:
        model = Cals
        fields = ["username", "title", "eventdate", "eventtime", "date", "approve", "act"]
        widgets = {
            'eventtime': forms.TimeInput(attrs={'type': 'time'}),
            'eventdate': forms.DateInput(attrs={'type': 'date'}),
            'approve': forms.TextInput(attrs={'type': 'hidden'}),
            'date': forms.TextInput(attrs={'type': 'hidden'}),
            'act': forms.TextInput(attrs={'type': 'hidden'}),
        }
