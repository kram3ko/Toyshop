import threading

from django.core.mail import EmailMessage
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site

from accounts.services.token_service import account_activation_token


class EmailService:
    @staticmethod
    @transaction.atomic
    def create_user_and_send_email(request, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        subject = "Activate your account."
        message = render_to_string(
            "registration/emails/acc_active_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
            },
        )
        email = EmailMessage(subject, message, to=[user.email])
        email.content_subtype = "html"
        threading.Thread(target=email.send).start()
        return user
