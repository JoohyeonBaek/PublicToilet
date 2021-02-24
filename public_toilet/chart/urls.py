from django.urls import path

from . import views
from django.conf.urls import url

app_name = 'pulls'
urlpatterns = [
    path('', views.chart_view, name='index'),
    url(r'^chartoption/$', views.option_chart, name='chartoption')
]