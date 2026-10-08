"""
URL configuration for greencloud project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from storage.views import home,login_view,register_view,dashboard,delete_file,logout_view,view_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/',register_view),
    path('dashboard/', dashboard, name='dashboard'),
    path('view/<int:file_id>/', view_file, name='view_file'),
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
    path('logout/', logout_view, name='logout'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

