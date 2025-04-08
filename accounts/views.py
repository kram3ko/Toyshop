import logging
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from django.views import View, generic

from accounts.services.token_service import account_activation_token
from customers.forms import CustomCustomerCreationForm
from customers.models import User

logger = logging.getLogger(__name__)


# class SignUpView(View):
#     def get(self, request: HttpRequest) -> HttpResponse:
#         return render(request, "registration/signup.html")
#
#     def post(self, request: HttpRequest) -> HttpResponse:
#         username = request.POST.get("username", "").strip()
#         email = request.POST.get("email", "").strip()
#         password1 = request.POST.get("password1", "")
#         password2 = request.POST.get("password2", "")
#
#         errors = []
#
#         if not username:
#             errors.append("Username is required.")
#         elif User.objects.filter(username=username).exists():
#             errors.append("Username is already taken.")
#
#         if not email:
#             errors.append("Email is required.")
#         else:
#             try:
#                 validate_email(email)
#
#                 if User.objects.filter(email=email).exists():
#                     errors.append("Email is already registered.")
#             except ValidationError:
#                 errors.append("Enter a valid email address.")
#
#         try:
#             validate_password(password1)
#         except ValidationError as e:
#             errors.extend(e.messages)
#
#         if password1 != password2:
#             errors.append("Passwords do not match.")
#
#         if errors:
#             return render(request, "registration/signup.html", {"errors": errors})
#
#         try:
#             with transaction.atomic():
#                 user = User.objects.create_user(
#                     username=username, email=email, password=password1, is_active=False
#                 )
#
#                 current_site = get_current_site(request)
#                 mail_subject = "Activate your account."
#                 message = render_to_string(
#                     "registration/emails/acc_active_email.html",
#                     {
#                         "user": user,
#                         "domain": current_site.domain,
#                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                         "token": account_activation_token.make_token(user),
#                     },
#                 )
#                 email = EmailMessage(mail_subject, message, to=[user.email])
#                 email.content_subtype = "html"
#                 email.send()
#
#                 # send message in a separate thread
#                 # threading.Thread(target=email.send).start()
#         except Exception as e:
#             logging.error(f"Error sending email: {e}")
#
#             return render(request, "registration/signup.html")
#
#         return render(request, "registration/email_confirmation_sent.html")


class CustomerSignUpView(generic.CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = CustomCustomerCreationForm
    success_url = reverse_lazy("login")

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
            email.send()

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
                "Thank you for confirming your email. You can now login to your account.",
            )
            return redirect("accounts:login")
        else:
            return render(request, "registration/activation_invalid.html")
