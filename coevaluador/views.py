from django.shortcuts import render


def index(request):
    return render(request, 'coevaluador/index.html')


def lpnp(request):
    return render(request, 'coevaluador/main_np.html')
