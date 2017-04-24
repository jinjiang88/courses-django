from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^destroy/(?P<cid>\d+)$', views.destroy),
    url(r'^delete/(?P<cid>\d+)$', views.delete)
]
