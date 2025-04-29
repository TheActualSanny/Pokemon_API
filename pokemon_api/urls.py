from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

pattern = 'api/v1/{endpoint}/'

schema_view = get_schema_view(
    openapi.Info(
        title = 'Pokemon API',
        default_version = 'V1.0.0',
        description = 'An API to fetch Pokemon data'
    ),
    public = True,
    permission_classes = [AllowAny]
)

urlpatterns = [
    path('', schema_view.with_ui('swagger'), name = 'swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc'), name = 'redoc-docs'),
    path('admin/', admin.site.urls),
    path(pattern.format(endpoint = 'authentication'), include('authentication.urls')),
    path(pattern.format(endpoint = 'main'), include('api.urls', namespace = 'api'))
]
