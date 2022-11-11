# django_project/urls.py
from django.contrib import admin
from django.urls import path, include  # new
from django.contrib.auth import views as auth_views
import approve
from posts.views import CreatePostView
from users import views as user_views
from pages import views as user_view
from approve import views as approve_view
from django.conf import settings
from django.conf.urls.static import static
from pages.views import HoPageView, uploadImg, AboutPageView
from posts.views import HomePageView, CreatePostView
from posts import views
from posts.views import ApprovalPostView
from pages.views import GreatePostView, PrefectPageView, GalleryPageView
from approve.views import ApprovePostView



urlpatterns = [
    path("", GreatePostView.as_view(), name='home'),
    path("prefects/", PrefectPageView.as_view(), name='prefects'),
    path("about/", AboutPageView.as_view(), name="your-name"),
    path("admin/", admin.site.urls),
 #   path("home/", include("pages.urls")),
 #   path("about/", include("pages.urls")),
    path("service/", include("pages.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
#    path("your-name/", HoPageView.as_view(), name="your-name"),
    path("blog/", include("pages.urls")),
    path('we/', user_views.home, name='home'),
    path('see/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("base/", include("users.urls")),
    path("posthome/", include("posts.urls")),
    path("post/", include("posts.urls")),
    path("dad/", HomePageView.as_view(), name="home"),
    path("mum/", CreatePostView.as_view(), name="post"),
    path("your-name/", user_view.uploadImg, name="display"),
  #  path('modelview/', views.ExperienceList.as_view(), name='experience_list'),
  #  path("prefects/", include("pages.urls")),
    path("gallery/", GalleryPageView.as_view(), name='gallery'),
    path("approve/", ApprovePostView.as_view(), name='approve'),
    path("approval/", ApprovalPostView.as_view(), name='approve'),
    path('apview/', approve_view.testing, name='home'),
    path('approve2/', approve_view.a_view, name='home'),

]


if settings.DEBUG:  # new
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
