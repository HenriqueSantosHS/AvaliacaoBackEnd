from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        if usuario == "admin" and senha == "123":
            return HttpResponse("Login realizado com sucesso!")
        else:
            return HttpResponse("Usuário ou senha inválidos")

    return render(request, 'index.html')