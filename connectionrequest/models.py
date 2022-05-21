import uuid
from django.db import models

CONNECTION_REASONS = {
    ("lonliness", 'Lonliness'),
    ("depression", 'Depression'),
}

CONNECTION_RESPONSES = {
    ("accept", "Yes"),
    ("deny", "No"),
}


class ConnectionRequest(models.Model):
    """Class for the Message Requests"""

    request_id = models.UUIDField(default=uuid.uuid4, editable=False)
    recipient_name = models.CharField(max_length=254, null=False, blank=False)
    recipient_email = models.EmailField(
        max_length=254, null=False, blank=False
    )
    connection_reason = models.CharField(
        max_length=30, choices=CONNECTION_REASONS, null=False, blank=False
    )
    custom_message = models.TextField(null=True, blank=True)
    sender_email = models.EmailField(max_length=254, null=False, blank=False)
    response_decision = models.CharField(
        max_length=30, choices=CONNECTION_RESPONSES, null=True, blank=True
    )
    custom_response_text = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return description string"""
        request_desc = f"Connection Request {self.request_id} \
            to {self.recipient_email}"
        return request_desc
