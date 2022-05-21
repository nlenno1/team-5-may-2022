from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ConnectionRequest
from .forms import (ConnectionRequestForm, ConnectionSearchForm, 
                    ConnectionResponseForm)
from .utils import send_connection_email, send_response_email


@login_required
def send_connection_request(request):
    """ A view to send a connection request """

    form = ConnectionRequestForm()

    if request.method == "POST":
        form = ConnectionRequestForm(request.POST)
        if form.is_valid():
            exisiting_request = ConnectionRequest.objects.filter(
                recipient_email=form.cleaned_data['recipient_email'],
                sender_email=request.user.email
            )
            if len(exisiting_request) == 0:
                new_connection_request = form.save()
                new_connection_request.sender_email = request.user.email
                new_connection_request.save()
                send_connection_email(new_connection_request)
                messages.success(
                    request,
                    f"Connection Request sent to  \
                    {new_connection_request.recipient_email}",
                )
            else:
                messages.error(
                    request,
                    "You have already sent an email to that person. You can't \
                        send more than 1 connection request to every email address",
                )
        else:
            messages.error(
                request,
                "Unable to send Connection Request. Please check \
                that the form is valid",
            )
        return redirect(reverse("send_connection_request"))

    context = {
        'form': form,
    }

    return render(request, 'connectionrequest/send-request.html', context)


def connection_request_search(request):
    """ A view to find a specific connection request """

    form = ConnectionSearchForm()

    if request.method == "POST":
        form = ConnectionSearchForm(request.POST)
        if form.is_valid():
            connection_code = form.cleaned_data.get("search_uuid")
            connection_request = get_object_or_404(ConnectionRequest, 
                                                   request_id=connection_code)
            if connection_request:
                if connection_request.response_decision is None:
                    messages.success(
                        request,
                        f"Connection Request {connection_code} Found",
                    )
                    return redirect("respond_to_connection_request",
                                    connection_code)
                else:
                    messages.error(
                        request,
                        f"Connection Request {connection_code} has already had a responce",
                    )
            else:
                messages.error(
                    request,
                    f"Unable to to find Connection Request {connection_code}",
                )
        else:
            messages.error(
                request,
                "Unable to send a Connection Request. Please check \
                that the form is valid",
            )
        return redirect(reverse("connection_request_search"))

    context = {
        'form': form,
    }

    return render(request, 'connectionrequest/search-for-request.html',
                  context)


def respond_to_connection_request(request, connection_code):
    """ A view to respond to a connection request """
    connection_request = get_object_or_404(ConnectionRequest, request_id=connection_code)
    form = ConnectionResponseForm()

    if request.method == "POST":
        form = ConnectionResponseForm(request.POST)

        if form.is_valid():
            connection_request.response_decision = form.cleaned_data.get("response_decision")
            connection_request.custom_response_text = form.cleaned_data.get("custom_response_text")
            connection_request.save()
            send_response_email(connection_request)
            messages.success(
                request,
                f"Connection response sent for Request \
                    {connection_request.request_id}. Thank you for \
                        using this service",
            )
            return redirect("home")
        else:
            messages.error(
                request,
                "Unable to send the Connection Request response. If this message \
                    persists then please get in touch",
            )

        return redirect(reverse("respond_to_connection_request", connection_code))

    context = {
        'form': form,
        'data': connection_request,
    }

    return render(request, 'connectionrequest/respond-to-connection-request.html', context)
