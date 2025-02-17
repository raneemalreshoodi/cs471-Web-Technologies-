"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import apps.bookmodule.views

from django.contrib import admin
from django.urls import path
from django.urls import path, include
from apps.bookmodule import views  # ✅ Correct Import
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
path('admin/', admin.site.urls),
path('books/', include("apps.bookmodule.urls")), #include urls.py of bookmodule app
path('users/', include("apps.usermodule.urls")) #include urls.py of usermodule app
]
# urlpatterns = [
# path('admin/', admin.site.urls),
# path('', apps.bookmodule.views.index), #add only this line of code
# # path('index2/<int:val1>/', apps.bookmodule.views.index2) #add only this line
#   path('', views.index, name='index'),
# path('books/', include("apps.bookmodule.urls")), #include urls.py of bookmodule app
# path('users/', include("apps.usermodule.urls")) #include urls.py of usermodule app
#   ]

# import apps.templates # Ensure `include` is imported if used
