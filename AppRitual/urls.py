from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from Chat.views import *


urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('menu/', menu, name='menu'),
    path('acercaRitual', acercaRitual, name='acercaRitual'),
    path('reservaciones/', reservaciones, name='reservaciones'),
    path('trabajadores/', trabajadores, name='trabajadores'),
    path('presentaciones/', presentaciones, name='presentaciones'),
    path('bodasEventos/', bodasEventos, name='bodasEventos'),
    path('getReservas/', getReservas, name='getReservas'),
    path('setReservas/', setReservas, name='setReservas'),
    path('deleteReserva/<id>', deleteReserva, name='deleteReserva'),
    path('editarReserva/<id>', editarReserva, name='editarReserva'),
    path('buscarReservas/', buscarReservas, name='buscarReservas'),
    path('getBodasEventos/', getBodasEventos, name='getBodasEventos'),
    path('setBodasEventos/', setBodasEventos, name='setBodasEventos'),
    path('deleteBodasEventos/<id>', deleteBodasEventos, name='deleteBodasEventos'),
    path('editarBodasEventos/<id>', editarBodasEventos, name='editarBodasEventos'),
    path('buscarBodasEventos/', buscarBodasEventos, name='buscarBodasEventos'),
    path('getTrabajadores/', getTrabajadores, name='getTrabajadores'),
    path('setTrabajadores/', setTrabajadores, name='setTrabajadores'),
    path('buscarTrabajadores/', buscarTrabajadores, name='buscarTrabajadores'),
    path('deleteTrabajadores/<id>', deleteTrabajadores, name='deleteTrabajadores'),
    path('editarTrabajadores/<id>', editarTrabajadores, name='editarTrabajadores'),
    path('', loginWeb, name='login'),
    path('registro/', registro, name='registro'),
    path('', LogoutView.as_view(template_name="login.html"), name="logout"),
    path('contactar/', contactar, name='contactar'),
    path('contactarExitoso/', contactarExitoso, name='contactarExitoso'),
    path('perfil/', perfilview, name="perfil"),
    path('perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('perfil/editarPerfil/perfil/changePassword/', changePassword, name="changePassword"),
    path('perfil/editarPerfil/perfil/changePassword/changePasswordExitoso', changePasswordExitoso, name="changePasswordExitoso"),
    path('perfil/changeAvatar/', editAvatar, name="editAvatar"),
    path('blog/', listaBlog, name="listaBlog"),
    path('blog/crear/', crearBlog, name="crearBlog"),
    path('blog/editar/<int:blog_id>/', editarBlog, name="editarBlog"),
    path('blog/editar/<int:blog_id>/blog/detalle/', editarBlogExitoso, name="editarBlogExitoso"),
    path('blog/eliminar/<int:blog_id>/', eliminarBlog, name="eliminarBlog"),
    path('blog/buscar/', buscarBlogs, name="buscarBlogs"),
    path('blog/buscar/<str:keyword>/<str:date>/', buscarBlogs, name="buscarBlogs"),
    path('blog/detalle/<int:blog_id>/', detalleBlog, name="detalleBlog"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
