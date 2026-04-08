from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('/bem-vindo/')
        else:
            return render(request, 'index.html', {
                'erro': 'Usuário ou senha inválidos'
            })

    return render(request, 'index.html')


def cadastro_view(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # 1. Evita usuário duplicado
        if User.objects.filter(username=usuario).exists():
            return render(request, 'TelaCadastro.html', {
                'erro': 'Este nome de usuário já está em uso.'
            })

        # 2. NOVA VERIFICAÇÃO: Evita e-mail duplicado
        if User.objects.filter(email=email).exists():
            return render(request, 'TelaCadastro.html', {
                'erro': 'Este e-mail já está cadastrado em outra conta.'
            })

        # Se passou pelas verificações, cria o usuário
        User.objects.create_user(
            username=usuario,
            email=email,
            password=senha
        )
        
        messages.success(request, "Cadastro concluído com sucesso!")
        return redirect('/')

    return render(request, 'TelaCadastro.html')


from django.contrib.auth.models import User

def recuperar_senha_view(request):
    if request.method == "POST":
        # O .strip() remove espaços vazios acidentais
        email = request.POST.get("email", "").strip()
        
        # Busca ignorando maiúsculas/minúsculas
        user = User.objects.filter(email__iexact=email).first()

        if user:
            # Envia o 'username' para a próxima tela saber de quem mudar a senha
            return render(request, 'NovaSenha.html', {
                'usuario': user.username
            })
        else:
            return render(request, 'TelaEsqueciSenha.html', {
                'erro': 'Email não encontrado em nossa base de dados.'
            })

    return render(request, 'TelaEsqueciSenha.html')

def nova_senha_view(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        try:
            user = User.objects.get(username=usuario)
            user.set_password(senha) # Criptografa a nova senha
            user.save()
            return redirect('/') # Sucesso: volta para o login
        except User.DoesNotExist:
            return redirect('/') 
            
    return render(request, 'NovaSenha.html')

def bem_vindo_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    return render(request, 'Bem_Vindo.html')