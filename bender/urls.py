from django.conf.urls import url
from bender import views


urlpatterns = [
    url(r'^questions/$', views.question_list),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.question_detail),
    url(r'^answers/$', views.answer_list),
    url(r'^answers/(?P<pk>[0-9]+)/$', views.answer_detail),
    url(r'^bot/(?P<str>[A-Za-z-\s]+$)', views.bot),
]