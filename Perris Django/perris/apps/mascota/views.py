from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.mascota.forms import forms, MascotaForms
from apps.mascota.models import Mascota
from django.views.generic import ListView
from django.contrib import auth
from .forms import MascotaForms
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm
# Create your views here.

def index(request):
    return render(request,'mascota/index.html')
def logout(request):
    auth.logout(request)
    return render (request,'index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForms(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('http://localhost:8000/mascota/listar')

    else:
        form = MascotaForms

    return render(request, 'mascota/mascota_form.html',{'form':form})
def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForms(instance=mascota)
	else:
		form = MascotaForms(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('http://localhost:8000/mascota/listar')
	return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('http://localhost:8000/mascota/listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

def form(request):
    return render(request, 'registration/form.html',{})

def register(request):
    
    variables = {
        'form':CustomCreationForm
    }

    if request.POST:
        #le pasamos todos los campos que vienen
        #desde el navegador al formulario
        form = CustomCreationForm(request.POST)

        if form.is_valid():
            #el formulario se encarga de guardar
            #los datos en la BBDD
            form.save()
            variables['mensaje'] = "Usuario creado"
        else:
            variables['mensaje'] = "No se ha registrado el usuario"
            variables['form'] = form

    return render(request, 'register/register.html', variables)