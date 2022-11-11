from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm, Post
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class ApprovePostView(UserPassesTestMixin, CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "approval.html"
    success_url = "/"
    def test_func(self):
        return self.request.user.is_superuser


from django.http import HttpResponse
from django.template import loader
#from users.models import Post

def testing(request):
  mydata = Post.objects.all()
  template = loader.get_template('head.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

def a_view(request):
    all_posts = Post.objects.all()
    return render(request, "head.html", {'all_posts': all_posts})