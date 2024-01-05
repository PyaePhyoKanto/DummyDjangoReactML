from django.contrib import admin
from django.urls import path, include
from myapp.views import home_view  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('', home_view, name='home'),  # Add the root URL
]
