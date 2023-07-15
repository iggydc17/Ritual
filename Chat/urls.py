from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', chatView, name="chat"),
    path('vermensajes/<id>',listaMensajes,name='verChat')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
