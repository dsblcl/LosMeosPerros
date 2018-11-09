from django.conf.urls import url,include
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete,logout,register
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
from django.conf.urls import url, include
from django.urls import path
from . import views

    

urlpatterns = [
     path('index/',index,name='index'),
    url(r'^nuevo$',mascota_view, name='mascota_crear'),
    url(r'^listar$',mascota_list, name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
    url(r'^login/', LoginView.as_view(template_name='index.html'), name="login"),
    path('logout/',logout,name='logout'),
    url(r'^register/', views.register, name= "register"),
]
