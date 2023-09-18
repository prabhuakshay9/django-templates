from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


class LoginForm(AuthenticationForm):
    """ Custom login form that extends the AuthenticationForm. """

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        # FormHelper instance for better form rendering control.
        self.helper = FormHelper()

        # layout for the form using Crispy Forms Layout.
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Login', css_class="btn")
        )


class CustomPasswordChangeForm(PasswordChangeForm):
    """ Custom Password Change Form that extends PassWordChangeForm """

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        # FormHelper instance for better form rendering control.
        self.helper = FormHelper()

        # layout for the form using Crispy Forms Layout.
        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
            Submit('submit', 'Change Password', css_class="btn")
        )
