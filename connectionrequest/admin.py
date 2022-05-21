from django.contrib import admin

from .models import ConnectionRequest


class ConnectionRequestAdmin(admin.ModelAdmin):
    """Edit Class for Admin pages"""

    list_display = (
        "request_date",
        "request_id",
        "response_decision",
    )

    ordering = ("request_date",)


admin.site.register(ConnectionRequest, ConnectionRequestAdmin)
