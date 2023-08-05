
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('C:\Users\LENOVO\Desktop\Django\Quora_Project\quora_app')),
]
