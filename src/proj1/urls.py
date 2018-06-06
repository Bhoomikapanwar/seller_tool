"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from app1 import views as v
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/',  v.home),
    path('login/', auth_views.login,name='login'),
    path('login/logredi/',v.logredi),
    path('logout/',auth_views.logout,{'next_page':'/login'},name='logout'),
    path('gst/' , v.gst),
    path('kyc/' , v.kyc),
    path('credit/', v.Credit),
    path('profile/',v.profile),
    path('notif/', include(notifications.urls, namespace='notifications')),
    #path('noti/',v.noti),
    path('health/',v.main),
    path('home/',v.home)
]
