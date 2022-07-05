from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    #path(r'static/main/(<path>.*)', serve,{'document_root': os.path.join(os.path.dirname(__file__), '/static/')} ),
    #path(r'media/(<path>.*)', serve,{'document_root': os.path.join(os.path.dirname(__file__), '/media/')} ),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


'''if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]'''