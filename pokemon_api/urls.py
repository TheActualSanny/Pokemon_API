from django.contrib import admin
from django.urls import path, include

pattern = 'api/v1/{endpoint}/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(pattern.format(endpoint = 'authentication'), include('authentication.urls')),
    path(pattern.format(endpoint = 'main'), include('api.urls'))
]
