from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, UserCreationForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from pages.models import Clubm, Sportm
from django.template import loader
from posts.views import headmistress, headboy, sports_prefect, clubs_prefect
from posts.models import Post
from posts.models import Post as Kk






def stu_zone(request):

    i = len(Kk.objects.all().filter(approve='yes'))
    ii = len(Clubm.objects.all().filter(approve='yes'))
    iii = len(Sportm.objects.all().filter(approve='yes'))
    check = Kk.objects.all().filter(approve='yes')
    check1 = Kk.objects.all().filter(approve='yes')[i-1]
    check2 = Kk.objects.all().filter(approve='yes')[i-2]
    check3 = Kk.objects.all().filter(approve='yes')[i-3]
    club1 = Clubm.objects.all().filter(approve='yes')[ii-1]
    sport1 = Sportm.objects.all().filter(approve='yes')[iii-1]
    sport = Sportm.objects.all().filter(approve='yes')

    return render(request, 'users/service2.html', {'sport': sport, 'check': check, 'check1': check1, 'check2': check2 , 'check3': check3, 'club1': club1, 'sport1': sport1 })

#

def home(request):
    check = Kk.objects.all().filter(approve='yes')
    sport = Sportm.objects.all().filter(approve='yes')

    return render(request, 'users/service2.html', {'sport': sport, 'check': check })

#    return render(request, 'users/home.html')
#

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def index(request):
  username = None
  username = request.user.username 
  mymembers = Sportm.objects.all().filter(approve='Pending')
  template = loader.get_template('delete.html')
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
  mymembers = Sportm.objects.all().filter(approve='Pending')
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
  member = Sportm(title=x, content=y, image=a, surname=b, firstname =c, level=d, date = e, idd= f, approve=g  )
  member.save()
  if username in headmistress: 
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')

def delete(request, id):
  username = None
  username = request.user.username 
  member = Sportm.objects.get(id=id)
  member.delete()
  if username in headmistress:
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')

def update(request, id):
  username = None
  username = request.user.username 
  mymember = Sportm.objects.get(id=id)
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
  member = Sportm.objects.get(id=id)
  member.approve = nine
  member.save()
  if username in headmistress:
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')
# Create your views here.





class BasePageView(TemplateView):
    template_name = "base.html"