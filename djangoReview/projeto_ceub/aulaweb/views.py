from django.shortcuts import render

# Create your views here.
def index(request):
    print('oi')
    return render(request, 'aulaweb/index.html', {})

def sobre(request):
    print('oi')
    return render(request, 'aulaweb/sobre.html', {'nome_projeto':'Teste'})