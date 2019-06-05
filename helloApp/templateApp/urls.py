# howdy/urls.py
from django.conf.urls import url
from templateApp import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', admin.site.urls),
    url(r'^template/$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]