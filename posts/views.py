from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView, TemplateView
from .models import Post, Experience, Post_a
from django.urls import reverse_lazy  # new
from django.views import generic
from .forms import PostForm, ApproveForm
from django.shortcuts import render
from .models import Post_a
from itertools import chain
import pandas as pd
from django.shortcuts import redirect,  get_object_or_404
from django.urls import reverse
from django.template import loader
from pages.models import Clubm, Sportm
from posts.models import Post as Kk


headmistress = ['abena', 'kofiadukpo']
headboy = ['patrick']
sports_prefect = ['jake', 'Kwame']
clubs_prefect = ['selorm', 'kofiadukpo']


def index(request):
  username = None
  username = request.user.username 
  mymembers = Post.objects.all().filter(approve='Pending')
  template = loader.get_template('delete.html')
  #template = loader.get_template('posthome.html')
  context = {
    'mymembers': mymembers,
  }
  if username in headmistress:
    return HttpResponse(template.render(context, request))
  else:
    return render(request, 'imm.html')

def add(request):
  username = None
  username = request.user.username 
  mymembers = Post.objects.all().filter(approve='Pending')
  template = loader.get_template('add.html')
  context = {
      'mymembers': mymembers,
  }
  if username in headmistress:
    return HttpResponse(template.render(context, request))
  else:
    return render(request, 'imm.html')

def addrecord(request):
  username = None
  username = request.user.username 
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
  if username in headmistress: 
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')

def delete(request, id):
  username = None
  username = request.user.username 
  member = Post.objects.get(id=id)
  member.delete()
  if username in headmistress:
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')

def update(request, id):
  username = None
  username = request.user.username 
  mymember = Post.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  if username in headmistress:
    return HttpResponse(template.render(context, request))
  else:
    return render(request, 'imm.html')

def updaterecord(request, id):
  username = None
  username = request.user.username 
  nine = request.POST['nine']
  member = Post.objects.get(id=id)
  member.approve = nine
  member.save()
  if username in headmistress:
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')

#





class HomePageView(ListView):
    model = Post
    template_name = "posthome.html"
    success_url = ''
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['form'] = ApproveForm()
        return context


def ablog(request):
  username = None
  username = request.user.username
  stu_blog = Post.objects.all().filter(approve='Yes')
  clu_blog = Clubm.objects.all().filter(approve='Yes')
  spo_blog = Sportm.objects.all().filter(approve='Yes')
  return render(request, 'ablog.html', {'stu_blog': stu_blog, 'clu_blog': clu_blog, 'spo_blog': spo_blog})

def list_and_create(request):
    username = None
    username = request.user.username    
    # notice this comes after saving the form to pick up new objects
    objects = Post.objects.all().filter(approve='Pending')
    elements = Post_a.objects.all()
    df = pd.DataFrame(Post.objects.all().values())
    df2 = pd.DataFrame(Post_a.objects.all().values())
  #  df3 = pd.merge(df, df2, on='idd', how='outer')

    cols = [i for i in df]
    rake = [dict(zip(cols, i)) for i in df.values]
    if username in headmistress:
      return render(request, 'posthome.html', {'objects': objects, 'rake': rake})
    else:
      return render(request, 'imm.html')


def pclub(request):
  username = None
  username = request.user.username  
  coc = Clubm.objects.all().filter(approve='Pending')
  if username in headmistress:  
    return render(request, 'aclub.html', {'coc': coc})
  else:
    return render(request, 'imm.html')


def psport(request):
  username = None
  username = request.user.username 
  coc = Sportm.objects.all().filter(approve='Pending')
  if username in headmistress:
    return render(request, 'asport.html', {'coc': coc})
  else:
    return render(request, 'imm.html')


class AppView(TemplateView):

    template_name = "approv.html"


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


