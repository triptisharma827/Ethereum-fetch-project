from django.shortcuts import render
from myapp.ethereum_api import get_balance, get_balance_inr, get_recent_transactions

# Create your views here.
def home(request):
    return render(request, 'myapp/base.html')

def fetch_ethereum(request):
    if request.method == 'POST':
        ethereum_address = request.POST.get('ethereum_address')
        # Process the Ethereum address and retrieve the desired information
        # Prepare the data to be displayed in the template

        # Call the `result` view and pass the processed data
        return result(request)
    else:
        # If the request method is not POST, render the form template
        return render(request, 'fetch.html')

def result(request):
    if request.method == 'POST':
        # Retrieve the necessary data for the template
        ethereum_address = request.POST.get('ethereum_address')
        balance = get_balance(ethereum_address)
        transactions = get_recent_transactions(ethereum_address)
        balance_inr, conversion_rate = get_balance_inr(ethereum_address)

        # Prepare the context data to pass to the template
        context = {
            'ethereum_address': ethereum_address,
            'balance': balance,
            'transactions': transactions,
            'balance_inr': balance_inr,
            'conversion_rate': conversion_rate,
        }

        # Render the result.html template with the context data
        return render(request, 'result.html', context)
    else:
        # If the request method is not POST, redirect to the fetch_ethereum view
        return fetch_ethereum(request)
