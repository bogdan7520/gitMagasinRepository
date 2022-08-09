from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os
from django.views.static import serve

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('krizhma', views.kr_page, name='kr_page'),
    path('vishivka_100x100', views.vish_page_100x100, name='vish_page_100x100'),
    path('vishivka_140x70', views.vish_page_140x70, name='vish_page_140x70'),
    path('ostalnoe', views.ost_page, name='ost_page'),
    path('<int:pk>', views.tovarDetailView.as_view(), name='news_detail'),
    #path(r'^static/(?P<path>.*)$', serve,{'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
    #path(r'^media/(?P<path>.*)$', serve,{'document_root': os.path.join(os.path.dirname(__file__), 'media')} ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
