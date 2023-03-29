from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from users.models import NewUser

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(UserCreationForm):
    # birthdate = forms.DateField()
    # discord_id = forms.CharField(max_length=100, help_text='Discord ID')
    # zoom_id = forms.CharField(max_length=100, help_text='Zoom ID')

    class Meta:
        model = NewUser
        fields = ["username", "password1", "password2", "email"]
        # fields = ["username", "password1", "password2", "birthdate", "email", "discord_id", "zoom_id"]


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = NewUser
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# class ItemsForm(forms.Form):
#     CHOICE_LIST = [
#         ('', '----'),  # replace the value '----' with whatever you want, it won't matter
#     ]
#     item = forms.ChoiceField(required=True)

