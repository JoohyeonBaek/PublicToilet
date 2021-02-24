from django.urls import path

from . import views
from django.conf.urls import url

app_name = 'pulls'
urlpatterns = [
    path('', views.showMap, name='index'),
    url(r'^chartoption/$', views.show_chart_option, name='chartoption')
]