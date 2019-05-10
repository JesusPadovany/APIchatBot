from django.conf.urls import url
from bender import views
from django.urls import path
from bender.views import About, Gallery, Member, products_list

urlpatterns = [
    url(r'^questions/$', views.question_list),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.question_detail),
    url(r'^answers/$', views.answer_list),
    url(r'^answers/(?P<pk>[0-9]+)/$', views.answer_detail),
    url(r'^api/(?P<str>[A-Za-z-\s]+$)', views.bot),
]