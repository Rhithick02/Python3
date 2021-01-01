from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('about/$', views.about),
    re_path('^$', views.homepg),
    re_path('^articles/', include('articles.urls'))
]
urlpatterns += staticfiles_urlpatterns()