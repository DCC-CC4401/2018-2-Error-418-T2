from django.urls import path

from . import views

app_name = 'coevaluador'

urlpatterns = [
    path('', views.index, name='index'),
    path('LPPN', views.LandingPagePersonaNat, name='LandingPagePersonaNat'),
    path('LPED', views.LandingPageEqD, name='LandingPageEqD'),
    path('AdminLog', views.indexadmi, name='indexadmi'),
    path('SP', views.StudentProfile, name='StudentProfile'),
]
