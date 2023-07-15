from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.http import HttpResponseServerError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import reservacionFormularios, eventoFormularios, trabajadorFormularios, AvatarForm, ChangePasswordForm, UserEditForm, BlogForm, EditPerfilForm, ComentarioBlogForm
from .models import Trabajadore, Evento, ReservasMesa, Avatar, Blog, EditPerfil, Comentario
from django.contrib.auth.models import User
from django.db.models import Q



@login_required()
def inicio(request):
    return render(request, "AppRitual/templatePadre.html")

@login_required()
def acercaRitual(request):
    return render(request, "acercaRitual.html")

@login_required()
def menu(request):
    return render(request, "menu.html")

@login_required()
def presentaciones(request):
    return render(request, "presentaciones.html")


# Reservaciones ---------------------------------------------------------------------------------------------------------------------------------------------------


@login_required()
def reservaciones(request):
    Reservaciones = ReservasMesa.objects.all()
    miReserva = reservacionFormularios()

    if request.GET:
        nombre = request.GET["nombre"]
        Reservaciones = ReservasMesa.objects.filter(nombre__icontains=nombre)
        if not Reservaciones:
            Reservaciones = ReservasMesa.objects.filter(apellido__icontains=nombre)

    return render(request, "reservaciones.html", {"Reservaciones": Reservaciones, "miReserva": miReserva})

@login_required()
def getReservas(request):
    return render(request, "getReservas.html")

@login_required()
def setReservas(request):
    Reservaciones = ReservasMesa.objects.all()

    if request.method == 'POST':
        miReserva = reservacionFormularios(request.POST)
        if miReserva.is_valid():
            data = miReserva.cleaned_data
            reserva = ReservasMesa(nombre=data["nombre"], apellido=data["apellido"], fechaSolicitud=data["fechaSolicitud"], fechaReserva=data["fechaReserva"], horaReserva=data["horaReserva"], numeroPersonas=data["numeroPersonas"], telefono=data["telefono"], email=data["email"], estado=data["estado"], anotaciones=data["anotaciones"])
            reserva.save()
            miReserva = reservacionFormularios()
            return redirect('reservaciones')
            return render(request, "reservaciones.html", {"miReserva": miReserva, "Reservaciones": Reservaciones})
    else:
        miReserva = reservacionFormularios()

    return render(request, "reservaciones.html", {"miReserva": miReserva, "Reservaciones": Reservaciones})

@login_required()
def buscarReservas(request):
    nombre = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    if nombre and apellido:
        reservas = ReservasMesa.objects.filter(nombre=nombre, apellido=apellido)
    elif nombre:
        reservas = ReservasMesa.objects.filter(nombre=nombre)
    elif apellido:
        reservas = ReservasMesa.objects.filter(apellido=apellido)
    return render(request, "getReservas.html", {"reservas": reservas})

@login_required()
def deleteReserva(request, id):
    reserva = ReservasMesa.objects.get(id=id)
    reserva.delete()
    return redirect('reservaciones')

@login_required
def editarReserva(request, id):
    reserva = ReservasMesa.objects.get(id=id)
    if request.method == 'GET':
        form = reservacionFormularios(instance=reserva)
        return render(request, 'editarReservas.html', {"formulario": form, "id_reserva": id})
    elif request.method == 'POST':
        miReserva = reservacionFormularios(request.POST)
        if miReserva.is_valid():
            data = miReserva.cleaned_data
            reserva.nombre = data["nombre"]
            reserva.apellido = data["apellido"]
            reserva.fechaSolicitud = data["fechaSolicitud"]
            reserva.fechaReserva = data["fechaReserva"]
            reserva.horaReserva = data["horaReserva"]
            reserva.numeroPersonas = data["numeroPersonas"]
            reserva.telefono = data["telefono"]
            reserva.email = data["email"]
            reserva.estado = data["estado"]
            reserva.anotaciones = data["anotaciones"]
            reserva.save()

            return redirect('reservaciones')



# Bodas y Eventos -----------------------------------------------------------------------------------------------------------------------------------------------------


@login_required()
def bodasEventos(request):
    Eventos = Evento.objects.all()
    miEvento = eventoFormularios()

    if request.GET:
        nombre = request.GET["nombre"]
        Eventos = Evento.objects.filter(nombre__icontains=nombre)
        if not Eventos:
            Eventos = Evento.objects.filter(apellido__icontains=nombre)
    return render(request, "bodasEventos.html", {"Eventos": Eventos, "miEvento": miEvento})

@login_required()
def getBodasEventos(request):
    return render(request, "getBodasEventos.html")

@login_required()
def setBodasEventos(request):
    Eventos = Evento.objects.all()
    if request.method == 'POST':
        miEvento = eventoFormularios(request.POST)
        print(miEvento)
        if miEvento.is_valid():
            data = miEvento.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            tipoEvento = data["tipoEvento"]
            privado = data["privado"]
            fechaSolicitud = data["fechaSolicitud"]
            fechaEvento = data["fechaEvento"]
            horaEvento = data["horaEvento"]
            numeroInvitados = data["numeroInvitados"]
            telefono = data["telefono"]
            email = data["email"]
            duracion = data["duracion"]
            costo = data["costo"]
            estado = data["estado"]
            anotaciones = data["anotaciones"]
            evento = Evento(nombre=nombre, apellido=apellido, tipoEvento=tipoEvento, privado=privado, fechaSolicitud=fechaSolicitud, fechaEvento=fechaEvento, horaEvento=horaEvento, numeroInvitados=numeroInvitados, telefono=telefono, email=email, duracion=duracion, costo=costo, estado=estado, anotaciones=anotaciones)
            evento.save()
            miEvento = eventoFormularios()
            return redirect('bodasEventos')
            #return render(request, "bodasEventos.html", {"miEvento": miEvento, "Eventos": Eventos})
        else:
            print(miEvento.errors)
    miEvento = eventoFormularios()
    return render(request, "bodasEventos.html", {"miEvento": miEvento, "Eventos": Eventos})

@login_required()
def buscarBodasEventos(request):
    nombre = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    if nombre and apellido:
        eventos = Evento.objects.filter(nombre=nombre, apellido=apellido)
    elif nombre:
        eventos = Evento.objects.filter(nombre=nombre)
    elif apellido:
        eventos = Evento.objects.filter(apellido=apellido)
    return render(request, "getBodasEventos.html", {"eventos": eventos})

@login_required()
def deleteBodasEventos(request,id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('bodasEventos')
    
@login_required
def editarBodasEventos(request, id):
    evento = Evento.objects.get(id=id)
    if request.method == "GET":
        form = eventoFormularios(instance=evento)
        return render(request, 'editarBodasEventos.html', {"formulario": form, "id_evento": id})
    elif request.method == "POST":
        miEvento = eventoFormularios(request.POST)
        if miEvento.is_valid():
            data = miEvento.cleaned_data
            evento.nombre = data["nombre"]
            evento.apellido = data["apellido"]
            evento.tipoEvento = data["tipoEvento"]
            evento.privado = data["privado"]
            evento.fechaSolicitud = data["fechaSolicitud"]
            evento.fechaEvento = data["fechaEvento"]
            evento.horaEvento = data["horaEvento"]
            evento.numeroInvitados = data["numeroInvitados"]
            evento.telefono = data["telefono"]
            evento.email = data["email"]
            evento.duracion = data["duracion"]
            evento.costo = data["costo"]
            evento.estado = data["estado"]
            evento.anotaciones = data["anotaciones"]
            evento.save()

            return redirect('bodasEventos')


# Trabajadores --------------------------------------------------------------------------------------------------------------------------------------------------


@login_required()
def trabajadores(request):
    Trabajadores = Trabajadore.objects.all()
    miTrabajador = trabajadorFormularios()

    if request.GET:
        nombre = request.GET["nombre"]
        Trabajadores = Trabajadore.objects.filter(nombre__icontains=nombre)
        if not Trabajadores:
            Trabajadores = Trabajadore.objects.filter(apellido__icontains=nombre)


    return render(request, "trabajadores.html", {"Trabajadores": Trabajadores, "miTrabajador": miTrabajador})

@login_required()
def getTrabajadores(request):
    return render(request, "getTrabajadores.html")

@login_required()
def setTrabajadores(request):
    Trabajadores = Trabajadore.objects.all()
    if request.method == 'POST':
        miTrabajador = trabajadorFormularios(request.POST, request.FILES)
        if miTrabajador.is_valid():
            data = miTrabajador.cleaned_data
            trabajador = Trabajadore(nombre=data["nombre"], apellido=data["apellido"], sector=data["sector"], telefono=data["telefono"], email=data["email"], fechaContratacion=data["fechaContratacion"], salario=data["salario"], foto_id=data["foto_id"], anotaciones=data["anotaciones"])
            trabajador.save()
            miTrabajador = trabajadorFormularios()
            return redirect('trabajadores')
            #return render(request, "trabajadores.html", {"miTrabajador": miTrabajador, "Trabajadores": Trabajadores})
    else:
        miTrabajador = trabajadorFormularios()

    return render(request, "trabajadores.html", {"miTrabajador": miTrabajador, "Trabajadores": Trabajadores})

@login_required()
def buscarTrabajadores(request):
    nombre = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    if nombre and apellido:
        trabajadores = Trabajadore.objects.filter(nombre=nombre, apellido=apellido)
    elif nombre:
        trabajadores = Trabajadore.objects.filter(nombre=nombre)
    elif apellido:
        trabajadores = Trabajadore.objects.filter(apellido=apellido)
    return render(request, "getTrabajadores.html", {"trabajadores": trabajadores})

@login_required()
def deleteTrabajadores(request, id):
    trabajadores = Trabajadore.objects.get(id=id)
    trabajadores.delete()
    return redirect('trabajadores')

@login_required
def editarTrabajadores(request, id):
    try:
        trabajador = Trabajadore.objects.get(id=id)

        if request.method == "POST":
            form = trabajadorFormularios(request.POST, instance=trabajador)
            if form.is_valid():
                form.save()
                return redirect('trabajadores')
        else:
            form = trabajadorFormularios(instance=trabajador)

        return render(request, 'editarTrabajadores.html', {"formulario": form, "id_trabajador": id})
    except Exception as e:
        return HttpResponseServerError(f"Error al editar trabajador: {str(e)}")

# Login y Registro ---------------------------------------------------------------------------------------------------------------------------------------------------


def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['user'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')


def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return redirect('login')
    else:
        return render(request, 'registro.html')


# Email ------------------------------------------------------------------------------------------------------------------------------------------------------------


@login_required()
def contactar(request): # Vista del mail
    return render(request, "contactar.html")

@login_required()
def contactarExitoso(request): # Vista del mail enviado
    
    return render(request, "contactarExitoso.html")


# Perfil ------------------------------------------------------------------------------------------------------------------------------------------------------------


@login_required
def perfilview(request):
    print(request.user)
    try:
        perfil = EditPerfil.objects.get(user=request.user)
    except EditPerfil.DoesNotExist:
        edit_perfil = EditPerfil(user=request.user)
        form = UserEditForm(instance=request.user)
        perfil_form = EditPerfilForm(instance=edit_perfil)
        return render(request, 'perfil/editarPerfil.html', {"form": form, "perfil_form": perfil_form})
    return render(request, 'perfil/perfil.html',{'usuario':perfil})


@login_required
def editarPerfil(request):
    usuario = request.user
    try:
        edit_perfil = EditPerfil.objects.get(user=usuario)
    except EditPerfil.DoesNotExist:
        edit_perfil = EditPerfil(user=usuario)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        perfil_form = EditPerfilForm(request.POST, instance=edit_perfil)
        if form.is_valid() and perfil_form.is_valid():
            usuario = form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = usuario
            perfil.save()
            return redirect('perfil')
    else:
        form = UserEditForm(instance=usuario)
        perfil_form = EditPerfilForm(instance=edit_perfil)
    return render(request, 'perfil/editarPerfil.html', {"form": form, "perfil_form": perfil_form})


@login_required()
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
                return render(request, "perfil/changePasswordExitoso.html")
            else:
                return HttpResponse("Las contraseñas no coinciden")
    else:
        form = ChangePasswordForm(user=usuario)
    return render(request, 'perfil/changePassword.html', {"form": form})


@login_required()
def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username=request.user)
            avatar = Avatar(user=user, image=form.cleaned_data['avatar'], id=request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user=request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "perfil/perfil.html", {'form': form, 'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user=request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "perfil/avatar.html", {'form': form, 'avatar': avatar})


@login_required()
def changePasswordExitoso(request):
    return render(request, "perfil/changePasswordExitoso.html")


@login_required()
def getavatar(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar


# Blog ------------------------------------------------------------------------------------------------------------------------


@login_required
def listaBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            #evitamos el envio del form, y restructuramos el id del autor
            form2 = form.save(commit=False)
            form2.autor_id = request.user.id
            form2.save()
            return redirect('listaBlog')
    else:
        form = BlogForm()

    blogs = Blog.objects.all()
    return render(request, 'blog/listaBlog.html', {'blogs': blogs, 'form': form})


@login_required()
def crearBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listaBlog')
    else:
        form = BlogForm()
    return render(request, 'blog/crearBlog.html', {'form': form})


@login_required
def editarBlog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog/detalle')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/editarBlog.html', {'form': form})


@login_required
def editarBlogExitoso(request, blog_id):
    return render(request, "blog/editarBlogExitoso.html", {'blog_id': blog_id})


@login_required
def comentarBlog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = ComentarioBlogForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.autor = request.user
            comment.save()
            return redirect('detalleBlog', blog_id=blog_id)
    else:
        form = ComentarioBlogForm()
    return render(request, 'blog/comentarBlog.html', {'form': form})


@login_required
def eliminarBlog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('listaBlog')

    return render(request, 'blog/eliminarBlog.html', {'blog': blog})


@login_required
def detalleBlog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comentarios = Comentario.objects.filter(post=blog)  # Obtener los comentarios
    print('detalle', blog.fechaPublicacion)
    return render(request, 'blog/detalleBlog.html', {'blog': blog, 'comentarios': comentarios})


@login_required
def buscarBlogs(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        date = request.GET.get('date')
        blogs = Blog.objects.all()
        '''
        query = Q(titulo__icontains=keyword)
        query.add(Q(subtitulo__icontains=keyword),Q.OR)
        query.add(Q(cuerpo__icontains=keyword),Q.OR)
        blogs = blogs.filter(query)
        
        query.add(Q(fechaPublicacion__date=date),Q.AND)
        '''
        print('fecha', date)
        if keyword:
            blogs = blogs.filter(Q(titulo__icontains=keyword) | Q(subtitulo__icontains=keyword) | Q(cuerpo__icontains=keyword))
        if date:
            blogs = blogs.filter(fechaPublicacion__date=date)

        return render(request, 'blog/buscarBlog.html', {'blogs': blogs})





# Chat en otra App -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

