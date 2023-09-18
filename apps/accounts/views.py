from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages
from apps.accounts.forms import CustomPasswordChangeForm, LoginForm


class CustomLogoutView(LogoutView):
    """ Custom logout view """
    next_page = settings.LOGOUT_REDIRECT_URL


@method_decorator(never_cache, name="dispatch")
class CustomLoginView(LoginView):
    """ Custom login View """
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Logged in as {user.email}')
        return super().form_valid(form)


class CustomPasswordChangeView(PasswordChangeView):
    """ Custom Password Change View """
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/change_password.html'  # Replace with your template name
    success_url = reverse_lazy("core:index")
