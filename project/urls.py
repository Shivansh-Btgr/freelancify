"""
URL configuration for project project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny]) 
def api_root(request, format=None):
    """
    API Root - Job Application Management System
    """
    return Response({
        'message': 'Job Application API',
        'version': '1.0',
        'endpoints': {
            'authentication': '/api/auth/',
            'accounts': '/api/accounts/',
            'posts': '/api/posts/',
            'documentation': {
                'swagger_ui': '/api/docs/',
                'redoc': '/api/redoc/',
                'schema': '/api/schema/',
            }
        },
        'status': 'operational'
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Root endpoint
    path('api/', api_root, name='api-root'),
    
    # API endpoints
    path('api/auth/', include('accounts.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    
    # Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # Redirect root to docs
    path('', RedirectView.as_view(url='/api/docs/', permanent=False), name='root-redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)