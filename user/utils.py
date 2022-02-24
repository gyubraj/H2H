""""""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from six import text_type

from user.email import EmailThread

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int) -> str:
        return (
            text_type(user.pk)
            + text_type(timestamp)
            + text_type(user.is_verified)
            + text_type(user.is_active)
        )


generate_token = TokenGenerator()



def send_activate_email(user) -> None:
    """
    After user registration this function will send the activation mail to the user email.
    """

    current_site = "http://127.0.0.1:8000"
    email_subject = "Activate your Account on H2H."
    message = render_to_string(
        "activateAccount.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user),
        },
    )
    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, [user.email]
    )
    EmailThread(email_message).start()


def send_password_reset_email(user) -> None:
    """
    When user forget password this function will send mail to reset user password.
    """
    email_subject = "Reset your password on Securitypal."
    message = render_to_string(
        "resetPassword.html",
        {
            "user": user,
            "domain": "http://127.0.0.1:8000",
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": PasswordResetTokenGenerator().make_token(user),
        },
    )
    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, [user.email]
    )
    EmailThread(email_message).start()



def send_account_activated_email(email: str, name: str) -> None:
    """
    Once admin make the user is_active flag True this function will inform user about their account activation by mail
    """
    email_subject = "H2H Account Activated"
    message = render_to_string(
        "accountActivatedEmail.html", {"name": name, "email": email}
    )

    email_message = EmailMessage(
        email_subject, message, settings.EMAIL_HOST_USER, [email]
    )
    EmailThread(email_message).start()


def activate_account(uidb64: str, token: str) -> bool:
    """
    If token and uidb64 is valid then user will be verified
    """
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and generate_token.check_token(user, token):
        user.is_verified = True
        user.save()
        return True

    return False






