from django.shortcuts import render
from website.models import *

def index(request):
    if request.method =='POST':
        login = Login()
        login.email = request.POST['email']
        login.senha = request.POST['senha']
        login.save()

        args = {
            'sucesso':'parabéns'
        }
        return render(request, 'index.html', args)

    return render(request, 'index.html')
