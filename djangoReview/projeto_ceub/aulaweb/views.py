from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    return render(request, 'aulaweb/index.html', {})

def sobre(request):
    return render(request, 'aulaweb/sobre.html', {'nome_projeto':'Teste'})

def list_produtos(request):
    i = Produto.objects.all()
    return render(request, 'aulaweb/produtos.html', {'list_produtos':i})

def infoP(request):
    return render(request, 'aulaweb/infoP.html', {})

def mostra_detalhes(request, id):
    produto = None
    msg = None
    try: 
        produto = Produto.objects.get(pk=id)
    except:
        msg = 'produto nao encontrado'
    return render(request, 'aulaweb/infoP.html', {'produto':produto, 'msg': msg})