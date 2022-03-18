
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from user.email import EmailThread


def send_property_added_email(property):
    
    email_subject = "Property Listed on H2H"

    message = render_to_string(
        "propertyadded.html", {"order": property}
    )

    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, [property.user.email]
    )
    EmailThread(email_message).start()

