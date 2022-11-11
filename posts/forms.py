from django import forms
from .models import Post, Post_a

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "cover", "surname", "firstname", "level", "date"]


class ApproveForm(forms.ModelForm):

    class Meta:
        model = Post_a
        fields = ["Approve"]