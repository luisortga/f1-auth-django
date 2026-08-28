"""
URL configuration for f1django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path

from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('pilots/', views.pilots, name='pilots'),
    path('pilots/create/', views.create_pilot, name='create_pilot'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('pilots/<int:pilot_id>/', views.pilot_detail, name='pilot_detail'),
    path('pilots/<int:pilot_id>/delete/', views.delete_pilot, name='delete_pilot'),
]
