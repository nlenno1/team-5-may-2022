from django.shortcuts import render
from .forms import ConnectionRequestForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


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
            print("NEW CONNECTION REQUEST CREATED")
            print(new_connection_request.request_id)
            send_connection_email(new_connection_request)
            # messages.success(
            #     request,
            #     f"Instructor Profile for \
            #                 {instructor.friendly_name} created",
            # )
        else:
            # messages.error(
            #     request,
            #     "Unable to Instructor Profile. Please check \
            #     that the form is valid",
            # )
            print("CONNECTION REQUEST FAILED")

        return redirect(reverse("send_connection_request"))

    context = {
        'form': form,
    }

    return render(request, 'connectionrequest/send-request.html', context)
