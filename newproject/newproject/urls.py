from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import index, successView
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', index,),
    url(r'success/', successView, name='success'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
