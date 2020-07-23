from django.urls import path,include

from .views import url,home


urlpatterns = [
    path('url', url,name='jsondata'),
    path('url/home/', home,name='homepage'), 
]