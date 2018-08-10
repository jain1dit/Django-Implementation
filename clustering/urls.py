from django.urls import path, re_path
from . import views
from django.conf.urls.static import static


urlpatterns = [
		path('', views.index, name = 'index'),
		re_path(r'^results/cluster_data/(?P<fileName>[a-z_.A-Z]+)/(?P<clsIndx>\d{1,2})/$', views.cluster_data, name = 'cluster_data')
] 

