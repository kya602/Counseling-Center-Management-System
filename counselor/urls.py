from django.conf.urls import url
from . import views

app_name = 'counselor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<pk>[0-9]+)/slots/$', views.slotlist, name='slots'),
    url(r'^profile/(?P<pk>[0-9]+)/slots/add$', views.CreateTimeSlot.as_view(), name='addSlot'),
]