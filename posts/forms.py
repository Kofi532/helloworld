from django import forms
from .models import Post, Post_a

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'approve': forms.TextInput(attrs={'type': 'hidden'}),
            'date': forms.TextInput(attrs={'type': 'hidden'}),
            'idd': forms.TextInput(attrs={'type': 'hidden'}),
        }

class ApproveForm(forms.ModelForm):
    class Meta:
        model = Post_a
        fields = ['Approve', 'Comments', 'Date', 'idd']