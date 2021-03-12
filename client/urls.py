from django.conf.urls import url
from . import views

app_name = 'client'

urlpatterns = [
    url(r'signup/$', views.NewClient.as_view(), name='signup'),
    url(r'index/(?P<pk>[0-9]+)/$', views.IndexView.as_view(), name='index'),
    url(r'bookAppointment/$', views.NewQuestionnaire.as_view(), name='bookAppointment'),
    url(r'anxiety_measure/$', views.NewAnxietyMeasure.as_view(), name='anxiety'),
    url(r'depression_measure/$', views.NewDepressionMeasure.as_view(), name='depression'),
    #url(r'index/case_view/(?P<client_id>[0-9]+)/$', views.case_view, name='case_view'),
    #url(r'^client/', views.client),

]
