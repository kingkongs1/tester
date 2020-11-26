from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('ec2-3-35-141-102.ap-northeast-2.compute.amazonaws.com', include('catalog.urls')),
    path('3.35.127.177', include('catalog.urls')),
]
