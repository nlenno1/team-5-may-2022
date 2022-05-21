from django.shortcuts import render
from .forms import ConnectionRequestForm


def send_connection_request(request):
    """ A view to return the connection request page """

    form = ConnectionRequestForm()

    context = {
        'form': form,
    }

    return render(request, 'connectionrequest/send-request.html', context)
