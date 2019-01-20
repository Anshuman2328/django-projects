"""project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    url(r'^', include('apps.first_app.urls'))  # this is done to include the first_app(first_app is the one of the many apps that you can have) url.py, This url.py doesn't exist yet but we need to create it in the first_app folder
]