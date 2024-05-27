from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import TransacaoForm

import datetime
from .models import Transacao


# Create your views here.
def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)  # HttpResponse(html)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()  # objects é um Manager
    return render(request, 'contas/listagem.html', data)


# Manager :: uma classe que o Django implementa para todos os models, trazendo operacoes de BD:
# all(), filter(), last(), first().

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
        # return listagem(request)
        # return render(request, 'contas/listagem.html')

    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    # Get the transaction from BD
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)  # Inicia um formulário com um objeto da preenchido

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    # data['transacao'] = transacao
    return render(request, 'contas/form.html', {'form': form, 'transacao': transacao})  # data || {'form': form} || {'transacao': transacao}


def delete(request, pk):
    # Get the transaction from BD
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')  # send user again to the listing page
