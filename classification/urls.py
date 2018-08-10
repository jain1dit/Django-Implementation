from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
	path('', views.upload_file, name = 'upload_file'),
	path('', views.index, name = 'index'),
] 
