from django.contrib import admin
from django.urls import include
from django.urls import path
from apps.bookmodule import views

# urlpatterns = [
# path('admin/', admin.site.urls),
# path('books/', include("apps.bookmodule.urls")), #include urls.py of bookmodule app
#     path('', views.index),
#     path('index2/<int:val1>/', views.index2),
#     path('<int:bookId>', views.viewbook)

# ]



# Static Pages
from django.urls import path
from . import views  # Import views from the same directory


urlpatterns = [
    path('<int:bookId>/', views.viewbook, name='viewbook'),  # ✅ Route for book details
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('index2/<str:val1>/', views.index2, name='index2'),  # ✅ Accepts text & numbers



]


