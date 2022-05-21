from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .models import ConnectionRequest
from .forms import (ConnectionRequestForm, ConnectionSearchForm, 
                    ConnectionResponseForm)


def send_connection_email(data):
    """Send the user a class cancellation email"""

    subject = render_to_string(
        "connectionrequest/connection-email/connection-email-subject.txt",
        {
            "name": data.recipient_name
        },
    )
    body = render_to_string(
        "connectionrequest/connection-email/connection-email-body.txt",
        {
            "data": data,
        },
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [
            data.recipient_email,
        ],
    )


def send_connection_request(request):
    """ A view to return the connection request page """

    form = ConnectionRequestForm()

    if request.method == "POST":
        form = ConnectionRequestForm(request.POST)
        if form.is_valid():
            new_connection_request = form.save()
            send_connection_email(new_connection_request)
            messages.success(
                request,
                f"Connection Request sent to  \
                {new_connection_request.recipient_email}",
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
    """ A view to return the connection request page """

    form = ConnectionSearchForm()

    if request.method == "POST":
        form = ConnectionSearchForm(request.POST)
        if form.is_valid():
            connection_code = form.cleaned_data.get("search_uuid")
            connection_request = get_object_or_404(ConnectionRequest, 
                                                   request_id=connection_code)
            if connection_request:
                messages.success(
                    request,
                    f"Connection Request {connection_code} Found",
                )
                return redirect("respond_to_connection_request",
                                connection_code)
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
