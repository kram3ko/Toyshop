import logging
import threading

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db import transaction
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View, generic

from accounts.services.token_service import account_activation_token
from customers.forms import CustomCustomerCreationForm
from customers.models import User

logger = logging.getLogger(__name__)


class CustomerSignUpView(generic.CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = CustomCustomerCreationForm

    @transaction.atomic
    def form_valid(self, form):
        try:
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(self.request)
            mail_subject = "Activate your account."
            message = render_to_string(
                "registration/emails/acc_active_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            email = EmailMessage(mail_subject, message, to=[user.email])
            email.content_subtype = "html"
            # email.send()
            threading.Thread(target=email.send).start()
        except Exception as e:
            logging.error(f"Error sending email: {e}")
            return render(self.request, "registration/signup.html", {"form": form})
        return render(self.request, "registration/email_confirmation_sent.html")


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            # login(request, user)
            messages.success(
                request,
                "Thank you for confirming your email. You can now login to your account.",  # noqa E501
            )
            return redirect("accounts:login")
        else:
            return render(request, "registration/activation_invalid.html")
