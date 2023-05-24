from django.shortcuts import render
from myapp.ethereum_api import get_balance,  get_recent_transactions

def home(request):
    return render(request, 'myapp/base.html')

def fetch_ethereum(request):
    if request.method == 'POST':
        ethereum_address = request.POST.get('ethereum_address')
        return result(request)
    else:
        return render(request, 'fetch.html')

def result(request):
    if request.method == 'POST':
        ethereum_address = request.POST.get('ethereum_address')
        balance = get_balance(ethereum_address)
        transactions = get_recent_transactions(ethereum_address)
        
        context = {
            'ethereum_address': ethereum_address,
            'balance': balance,
            'transactions': transactions,
        }
        return render(request, 'result.html', context)
    else:
        return fetch_ethereum(request)
