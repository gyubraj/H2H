

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from user.email import EmailThread


def send_booking_confirmed_email(order):

    email_subject = "Booking in H2H"

    message = render_to_string(
        "customer/orderplaced.html", {"order": order}
    )

    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, [order.visitor.email]
    )
    EmailThread(email_message).start()



def send_booking_cancel_email(order):

    email_subject = "Booking Cancel in H2H"

    message = render_to_string(
        "customer/ordercancel.html", {"order": order}
    )

    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, [order.visitor.email]
    )
    EmailThread(email_message).start()


def send_booking_received_email(order):
    
    email_subject = f"Booking Received for {order.property.name}"

    message = render_to_string(
        "owner/orderreceived.html", {"order": order}
    )

    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, [order.property.owner.email]
    )
    EmailThread(email_message).start()