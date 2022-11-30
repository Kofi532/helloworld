from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from .forms import PostForm, Post, Event
from .models import Cals
from django.http import HttpResponse
from django.template import loader
from posts.models import Post
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from posts.models import Post as Pop
from django.http import HttpResponse
from django.template import loader
from pages.models import Clubm, Sportm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from posts.views import headboy, headmistress, sports_prefect, clubs_prefect
from pages.models import Clubm, Sportm
import pandas as pd
from datetime import datetime, date

#from users.models import Post


def index(request):
  username = None
  username = request.user.username 
  mymembers = Clubm.objects.all().filter(approve='Pending')
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
  mymembers = Clubm.objects.all().filter(approve='Pending')
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
  member = Clubm(title=x, content=y, image=a, surname=b, firstname =c, level=d, date = e, idd= f, approve=g  )
  member.save()
  if username in headmistress: 
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')

def delete(request, id):
  username = None
  username = request.user.username 
  member = Clubm.objects.get(id=id)
  member.delete()
  if username in headmistress:
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')

def update(request, id):
  username = None
  username = request.user.username 
  mymember = Clubm.objects.get(id=id)
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
  member = Clubm.objects.get(id=id)
  member.approve = nine
  member.save()
  if username in headmistress:
    return HttpResponseRedirect(reverse('index'))
  else:
    return render(request, 'imm.html')


class ApprovePostView(UserPassesTestMixin, CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "approval.html"
    success_url = "/"  
    def test_func(self):
        return self.request.user.is_superuser

def testing(request):
  c = Pop.objects.all()
  all_posts = Post.objects.all()
  template = loader.get_template('approval.html')
  context = {
    'all_posts': all_posts,
    'c': c,
  }
  return HttpResponse(template.render(context, request))

def a_view(request):
    username = None
    usernamed = request.user.username 
    Club_post = Clubm.objects.all().filter(username= usernamed)
    Sport_post = Sportm.objects.all().filter(username= usernamed)
    all_posts = Post.objects.all().filter(username= usernamed)
    return render(request, "head.html", {'all_posts': all_posts, 'Club_post': Club_post, 'Sport_post': Sport_post})

def calenda(request):
    day = datetime.today().replace(day=1)
    day1 = day.strftime("%A")
    month = day.strftime("%B")
    yearr = datetime.now().year
 #   d1 = Cals.objects.all().filter(username= usernamed)
    df = pd.DataFrame(Cals.objects.all().values())
    df = df[df['act'] == 'Yes']
    df['days'] = (df['eventdate'].dt.day)
    d1 = df[df['days'] == 1].iloc[:1]
    d2 = df[df['days'] == 2].iloc[:1]
    d3 = df[df['days'] == 3].iloc[:1]
    d4 = df[df['days'] == 4].iloc[:1]
    d5 = df[df['days'] == 5].iloc[:1]
    d6 = df[df['days'] == 6].iloc[:1]
    d7 = df[df['days'] == 7].iloc[:1]
    d8 = df[df['days'] == 8].iloc[:1]
    d9 = df[df['days'] == 9].iloc[:1]
    d10 = df[df['days'] == 10].iloc[:1]
    d11 = df[df['days'] == 11].iloc[:1]
    d12 = df[df['days'] == 12].iloc[:1]
    d13 = df[df['days'] == 13].iloc[:1]
    d14 = df[df['days'] == 14].iloc[:1]
    d15 = df[df['days'] == 15].iloc[:1]
    d16 = df[df['days'] == 16].iloc[:1]
    d17 = df[df['days'] == 17].iloc[:1]
    d18 = df[df['days'] == 18].iloc[:1]
    d19 = df[df['days'] == 19].iloc[:1]
    d20 = df[df['days'] == 20].iloc[:1]
    d21 = (df[df['days'] == 21]).iloc[:1]
    d22 = df[df['days'] == 22].iloc[:1]
    d23 = df[df['days'] == 23].iloc[:1]
    d24 = df[df['days'] == 24].iloc[:1]
    d25 = df[df['days'] == 25].iloc[:1]
    d26 = df[df['days'] == 26].iloc[:1]
    d27 = df[df['days'] == 27].iloc[:1]
    d28 = df[df['days'] == 28].iloc[:1]
    d29 = df[df['days'] == 29].iloc[:1]
    d30 = df[df['days'] == 30].iloc[:1]
    d31 = df[df['days'] == 31].iloc[:1]
    col1 = [i for i in d1]
    dd1 = [dict(zip(col1, i)) for i in d1.values]
    col2 = [i for i in d2]
    dd2 = [dict(zip(col2, i)) for i in d2.values]
    col3 = [i for i in d3]
    dd3 = [dict(zip(col3, i)) for i in d3.values]
    col4 = [i for i in d4]
    dd4 = [dict(zip(col4, i)) for i in d4.values]
    col5 = [i for i in d5]
    dd5 = [dict(zip(col5, i)) for i in d5.values]
    col6 = [i for i in d6]
    dd6 = [dict(zip(col6, i)) for i in d6.values]
    col7 = [i for i in d7]
    dd7 = [dict(zip(col7, i)) for i in d7.values]
    col8 = [i for i in d8]
    dd8 = [dict(zip(col8, i)) for i in d8.values]
    col9 = [i for i in d9]
    dd9 = [dict(zip(col9, i)) for i in d9.values]
    col10 = [i for i in d10]
    dd10 = [dict(zip(col10, i)) for i in d10.values]
    col11 = [i for i in d11]
    dd11 = [dict(zip(col11, i)) for i in d11.values]
    col12 = [i for i in d12]
    dd12 = [dict(zip(col12, i)) for i in d12.values]
    col13 = [i for i in d13]
    dd13 = [dict(zip(col13, i)) for i in d13.values]
    col14 = [i for i in d14]
    dd14 = [dict(zip(col14, i)) for i in d14.values]
    col15 = [i for i in d15]
    dd15 = [dict(zip(col15, i)) for i in d15.values]
    col16 = [i for i in d16]
    dd16 = [dict(zip(col16, i)) for i in d16.values]
    col17 = [i for i in d17]
    dd17 = [dict(zip(col17, i)) for i in d17.values]
    col18 = [i for i in d18]
    dd18 = [dict(zip(col18, i)) for i in d18.values]
    col19 = [i for i in d19]
    dd19 = [dict(zip(col19, i)) for i in d19.values]
    col20 = [i for i in d20]
    dd20 = [dict(zip(col20, i)) for i in d20.values]
    col21 = [i for i in d21]
    dd21 = [dict(zip(col21, i)) for i in d21.values]
    col22 = [i for i in d22]
    dd22 = [dict(zip(col22, i)) for i in d22.values]
    col23 = [i for i in d23]
    dd23 = [dict(zip(col23, i)) for i in d23.values]
    col24 = [i for i in d24]
    dd24 = [dict(zip(col24, i)) for i in d24.values]
    col25 = [i for i in d25]
    dd25 = [dict(zip(col25, i)) for i in d25.values]
    col26 = [i for i in d26]
    dd26 = [dict(zip(col26, i)) for i in d26.values]
    col27 = [i for i in d27]
    dd27 = [dict(zip(col27, i)) for i in d27.values]
    col28 = [i for i in d28]
    dd28 = [dict(zip(col28, i)) for i in d28.values]
    col29 = [i for i in d29]
    dd29 = [dict(zip(col29, i)) for i in d29.values]
    col30 = [i for i in d30]
    dd30 = [dict(zip(col30, i)) for i in d30.values]
    col31 = [i for i in d31]
    dd31 = [dict(zip(col31, i)) for i in d31.values]
    tt = date.today()
    ttt = tt.month
#    MonMes = Eventm.objects.all().filter(eventmonth='January')[0]
    return render(request, 'calenda.html', {'ttt': ttt, 'dd1': dd1, 'dd2': dd2, 'dd3': dd3, 'dd4': dd4, 'dd5': dd5, 'dd6': dd6, 'dd7': dd7, 'dd8': dd8, 'dd9': dd9, 'dd10': dd10, 'dd11': dd11, 'dd12': dd12, 'dd13': dd13, 'dd14': dd14, 'dd15': dd15, 'dd16': dd16, 'dd17': dd17, 'dd18': dd18, 'dd19': dd19, 'dd20': dd20, 'dd21': dd21, 'dd22': dd22, 'dd23': dd23, 'dd24': dd24, 'dd25': dd25, 'dd26': dd26, 'dd27': dd27, 'dd28': dd28, 'dd29': dd29, 'dd30': dd30, 'dd31': dd31, 'day1': day1, 'month': month, 'yearr': yearr})

class CalsPostView(CreateView):  # new
    model = Cals
    form_class = Event
    template_name = "events.html"
    success_url = "/we/"