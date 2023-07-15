from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm,ConversacionForm
from .models import Mensaje, Conversacion
from django.contrib.auth.models import User


@login_required()
def chatView(request):
    form = MensajeForm()
    users = User.objects.all()
    conversaciones = Conversacion.objects.all()
    ctx = {'form': form,'chat_users':users,'conversaciones':conversaciones}
    if request.method == 'POST':
        receptor= User.objects.get(id=request.POST['receptor'])
        emisor = request.user
        form_conv = Conversacion(receptor=receptor,emisor=emisor)
        try:
            id_conv = form_conv.save()
        except:
            print(form_conv)
        conversacion_id = id_conv #guarde el nro de conversacion
        form_msj = MensajeForm(request.POST)
        form_msj_2 = form_msj.save(commit=False)
        form_msj_2.conversacion = Conversacion.objects.get(id=1)#cual es la conversacion que corresponde
        form_msj_2.save()
        return redirect('chat')
    return render(request, "chat/templatePadreChat.html", ctx)
    
# Mensajes ------------------------------------------------------------------------------------------------------------------


@login_required()
def listaMensajes(request,id):
    mensajes = Mensaje.objects.all()
    return render(request,'chat/verMensajes.html',{'mensajes':mensajes})


@login_required()
def enviarMensajes(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            receptor_id = request.POST.get('receptor_id')
            contenido = form.cleaned_data['contenido']
            emisor = request.user  # Obtener el usuario emisor
            receptor = User.objects.get(id=receptor_id)  # Obtener el usuario receptor usando el ID

            mensaje = Mensaje(emisor=emisor, receptor=receptor, contenido=contenido)
            mensaje.save()
            return redirect('chat:listaConversaciones')  # Redirigir a la lista de conversaciones

    else:
        form = MensajeForm()

    return render(request, "chat/templatePadreChat.html", {'form': form})


@login_required()
def buscarMensajes(request):
    pass


@login_required()
def eliminarMensajes(request):
    pass





# Conversaciones ------------------------------------------------------------------------------------------------------------------


def listaConversaciones(request):
    pass

@login_required()
def buscarConversaciones(request):
    pass


@login_required()
def eliminarConversaciones(request):
    pass

