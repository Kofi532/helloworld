from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from .models import Post, Experience, Post_a
from django.urls import reverse_lazy  # new
from multi_form_view import MultiModelFormView
from django.views import generic
from .forms import PostForm, ApproveForm
from django.shortcuts import render
from .models import Post_a
from itertools import chain
import pandas as pd
from django.shortcuts import redirect,  get_object_or_404
from django.urls import reverse
from django.template import loader

def index(request):
  mymembers = Post.objects.all().values()
  template = loader.get_template('delete.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
    mymembers = Post.objects.all().values()
    template = loader.get_template('add.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  a = request.POST['three']
  b = request.POST['four']
  c = request.POST['five']
  d = request.POST['six']
  e = request.POST['seven']
  f = request.POST['eight']
  g = request.POST['nine']
  member = Post(title=x, content=y, image=a, surname=b, firstname =c, level=d, date = e, idd= f, approve=g  )
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Post.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Post.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  nine = request.POST['nine']
  member = Post.objects.get(id=id)
  member.approve = nine
  member.save()
  return HttpResponseRedirect(reverse('index'))




class HomePageView(ListView):
    model = Post
    template_name = "posthome.html"
    success_url = ''
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['form'] = ApproveForm()
        return context

def ablog(request):
    stu_blog = Post.objects.all().filter(approve='yes')
    return render(request, 'ablog.html', {'stu_blog': stu_blog})


def list_and_create(request):
    
    if request.method == 'POST':
        form = ApproveForm(request.POST or None)
        form.save()
    else:
        form = ApproveForm()
    # notice this comes after saving the form to pick up new objects
    objects = Post.objects.all()
    elements = Post_a.objects.all()
    df = pd.DataFrame(Post.objects.all().values())
    df2 = pd.DataFrame(Post_a.objects.all().values())
    df3 = pd.merge(df, df2, on='idd', how='outer')

    cols = [i for i in df3]
    rake = [dict(zip(cols, i)) for i in df3.values]
    return render(request, 'posthome.html', {'objects': objects, 'form': form, 'rake': rake})



def students_blog(request):
    objectss = Post.objects.all()
    df = pd.DataFrame(Post.objects.all().values())
    df2 = pd.DataFrame(Post_a.objects.all().values())
    df3 = pd.merge(df, df2, on='idd', how='outer')
    df3 = df3.drop('image', axis=1)
    cols = [i for i in df3]
    rake = [dict(zip(cols, i)) for i in df3.values]
    return render(request, 'posthome2.html', {'objectss': objectss, 'rake': rake})


#
def meetings(request):
    meetingData = Post.objects.all()
    return render(request, 'posthome2.html', {'data': meetingData })


class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = "/we/"



class List(CreateView):
    model = Post_a
    form_class = ApproveForm
    template_name = 'posthome.html'
    success_url = "/"


