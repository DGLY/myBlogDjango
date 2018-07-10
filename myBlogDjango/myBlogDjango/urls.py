"""myBlogDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.views.generic import TemplateView
# from django.contrib import admin
from rest_framework.routers import DefaultRouter

from myBlog.views import BlogsListViewset
from suggest.views import createSuggestViewset

Router = DefaultRouter()
Router.register(r'blogs',BlogsListViewset,base_name="blogs")
Router.register(r'suggest',createSuggestViewset,base_name="suggest")

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'',include(Router.urls)),

    url(r'^dgly/', TemplateView.as_view(template_name="index.html"), name="index"),
]
