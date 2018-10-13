from django.urls import path

from . import views

app_name = 'coevaluador'

urlpatterns = [
    path('', views.index, name='index'),
    path('lpnp/', views.lpnp, name='lpnp'),
]