
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_connection_email(data, auto_website_url, website_url):
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
            "auto_website_link": auto_website_url + str(data.request_id),
            "website_link": website_url,
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


def send_response_email(data):
    """Send the user a class cancellation email"""

    subject = render_to_string(
        "connectionrequest/response-email/response-email-subject.txt",
    )
    body = render_to_string(
        "connectionrequest/response-email/response-email-body.txt",
        {
            "data": data,
        },
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [
            data.sender_email,
        ],
    )
