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
            "recipient_name": "Contact Name ",
            "recipient_email": "Email Address",
            "connection_reason": "What are you struggling with? ",
            "custom_message": "Add a custom message if you like ",
        }

        self.fields["recipient_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].label = placeholder


class ConnectionSearchForm(forms.Form):
    """Class for Connection Request Search"""

    search_uuid = forms.UUIDField(
        label="Connection Code "
    )


class ConnectionResponseForm(forms.ModelForm):
    """Class Connection Response"""

    class Meta:
        """Update Class Meta Data"""

        model = ConnectionRequest
        fields = (
            "response_decision",
            "custom_response_text",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "response_decision": "Are you willing to talk about this subject",
            "custom_response_text": "You can add a personalised response if you would like",
        }

        self.fields["response_decision"].widget.attrs["autofocus"] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].label = placeholder
