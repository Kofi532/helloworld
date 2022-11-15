from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from .models import Post, Experience, Post_a
from django.urls import reverse_lazy  # new
from multi_form_view import MultiModelFormView
from django.views import generic
from .forms import PostForm, ApproveForm
from django.shortcuts import render
from .models import Post_a



class HomePageView(ListView):
    model = Post
    template_name = "posthome.html"
    success_url = ''
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['form'] = ApproveForm()
        return context

def list_and_create(request):
    
    if request.method == 'POST' and form.is_valid():
        form = ApproveForm(request.POST or None)
        form.save()
    else:
        form = ApproveForm()
    # notice this comes after saving the form to pick up new objects
    objects = Post.objects.all()
    return render(request, 'posthome.html', {'objects': objects, 'form': form})

#
def index(request):
      number1 = list(Post_a.objects.all())
      number2 = int(request.GET.get('number2', 0))
      dict={
            'number1' : number1,
            'number2' : number2,
      }
      return render(request, 'index.html', dict)

#


class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = "/"



class List(CreateView):
    model = Post_a
    form_class = ApproveForm
    template_name = 'posthome.html'
    success_url = "/"


