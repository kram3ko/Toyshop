# import logging
#
# from allauth.account.views import SignupView
# from django.contrib import messages
# from django.db import transaction
# from django.shortcuts import redirect, render
# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_decode
# from django.views import View, generic
#
# from accounts.services.email_service import EmailService
# from accounts.services.token_service import account_activation_token
# from customers.forms import CustomCustomerCreationForm
# from customers.models import User
#
# logger = logging.getLogger(__name__)
#
#
# class CustomerSignUpView(SignupView):
#     # model = User
#     # template_name = "account/signup.html"
#     form_class = CustomCustomerCreationForm
#
#     # @transaction.atomic
#     # def form_valid(self, form):
#     #     try:
#     #         EmailService.create_user_and_send_email(self.request, form)
#     #     except Exception as e:
#     #         logging.error(f"Error during signup/email: {e}")
#     #         form.add_error(None, "Something went wrong during sign-up.")
#     #         return self.form_invalid(form)
#     #     return render(self.request, "account/email_confirmation_sent.html")
#
#
# class ActivateAccountView(View):
#     def get(self, request, uidb64, token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
#
#         if user is not None and account_activation_token.check_token(user, token):
#             user.is_active = True
#             user.save()
#             # login(request, user)
#             messages.success(
#                 request,
#                 "Thank you for confirming your email. You can now login to your account.",  # noqa E501
#             )
#             return redirect("account_login")
#         else:
#             return render(request, "account/activation_invalid.html", status=400)
