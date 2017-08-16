"""EventsApp URL Configuration

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
from django.contrib import admin
from Event import views
from Event.apiviews import GetDetails
# from Event.apiviews import GetDetailsByDate


urlpatterns = {

    url(r'^$', views.index, name="index"),
    url(r'^add/?$', views.create_details, name="add1"),
    url(r'^del/?$', views.delete, name="del1"),
    url(r'^api/details/(\w+)', GetDetails.as_view(), name="del1"),
    url(r'^update/?$', views.update,name="update"),
    url(r'^search$',views.search,name="search")
}
