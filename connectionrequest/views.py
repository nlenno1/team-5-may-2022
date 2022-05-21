from django.shortcuts import render


def send_connection_request(request):
    """ A view to return the connection request page """
    return render(request, 'connectionrequest/send-request.html')
