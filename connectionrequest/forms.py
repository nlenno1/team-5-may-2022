from django import forms
from .models import ConnectionRequest


class ConnectionRequestForm(forms.ModelForm):
    """Class for all Orders"""

    class Meta:
        """Update Class Meta Data"""

        model = ConnectionRequest
        fields = (
            "recipient_name",
            "recipient_email",
            "connection_reason",
            "custom_message",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "recipient_name": "Contact Name",
            "recipient_email": "Email Address",
            "connection_reason": "Why are you reaching out",
            "custom_message": "Add a custom message if you like",
        }

        self.fields["recipient_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False
