from django.shortcuts import render
from .models import EthereumTransaction
# Create your views here.


def fetch_ethereum(request):
    if request.method == 'POST':
        address = request.POST['address']
        # Fetch the Ethereum balance and recent transactions using web3 library
        # Store the data in the database
        # Retrieve the data for display
        transactions = EthereumTransaction.objects.filter(address=address).order_by('-timestamp')[:5]
        context = {'transactions': transactions}
        return render(request, 'fetch_app/results.html', context)
    else:
        return render(request, 'fetch_app/fetch.html')
