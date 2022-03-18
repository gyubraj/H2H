
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from user.email import EmailThread



def send_contact_email(contact):
    email_subject = "New Contact Query"

    message = render_to_string(
        "contact.html", {"name": contact.name, "email": contact.email, "query":contact.query}
    )

    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, ["gyubraj104@gmail.com"]
    )
    EmailThread(email_message).start()

