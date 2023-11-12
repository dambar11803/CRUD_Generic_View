"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from school import views 
from school.views import HomePage, AddStudent, StudentList, StudentDetail, StudentUpdate, StudentDelete 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='homepage'),
    path('addstudent/', AddStudent.as_view(), name='addstudent'),
    path('studentlist/', StudentList.as_view(), name='studentlist'),
    path('studentdetail/<int:pk>', StudentDetail.as_view(), name='studentdetail'),
    path('studentupate/<int:pk>', StudentUpdate.as_view(), name='studentupdate'),
    path('studentdelete/<int:pk>', StudentDelete.as_view(), name='studentdelete'),
]


#To display image from Django model to Django Tempate file
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)