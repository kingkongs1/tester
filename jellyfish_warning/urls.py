from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('ec2-52-79-80-117.ap-northeast-2.compute.amazonaws.com:8000/', include('catalog.urls')),
]
