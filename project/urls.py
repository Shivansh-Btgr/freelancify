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
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root - Job Application Management System
    """
    return Response({
        'message': 'Job Application API',
        'version': '1.0',
        'endpoints': {
            'authentication': {
                'register': reverse('register', request=request, format=format),
                'login': reverse('login', request=request, format=format),
                'logout': reverse('logout', request=request, format=format),
                'token_refresh': reverse('token_refresh', request=request, format=format),
            },
            'accounts': {
                'profile': reverse('profile', request=request, format=format),
            },
            'posts': {
                'list_posts': reverse('post-list', request=request, format=format),
                'create_post': reverse('post-create', request=request, format=format),
                'my_posts': reverse('my-posts', request=request, format=format),
                'my_applications': reverse('my-applications', request=request, format=format),
            },
            'documentation': {
                'swagger_ui': reverse('swagger-ui', request=request, format=format),
                'redoc': reverse('redoc', request=request, format=format),
                'schema': reverse('schema', request=request, format=format),
            }
        },
        'status': 'operational'
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', RedirectView.as_view(url='/api/schema/swagger-ui/', permanent=False), name='root-redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)