from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)
from .models import UserBase
import re
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator

Common_password = ['123456', 'password', '123456789', '12345', '12345678', 'qwerty',
    '1234567', '111111', '1234567890', '123123', 'abc123', '1234', 'password1',
    'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx', 'dragon',
    'sunshine', 'princess', 'letmein', '654321', 'monkey', '27653',
    '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))
    captcha = ReCaptchaField()


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(
        label='Enter Username', min_length=4, max_length=10, help_text='Required (maximum length: 10 characters)',
        error_messages = {'max_length': 'Username must be 10 characters or fewer.'})
    
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'},validators=[RegexValidator('[;&|$<>!\()]', inverse_match=True)])
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    password2 = forms.CharField(
        label='Confirm your password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name
    
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if password.lower() in [common.lower() for common in Common_password]:
            raise forms.ValidationError('Error')
        elif not re.search(r'[A-Z]', password):
            raise forms.ValidationError('Error')
        elif not re.search(r'[a-z]', password):
            raise forms.ValidationError('Error')
        elif not re.search(r'[0-9]', password):
            raise forms.ValidationError('Error')
        elif not re.search(r'[!@#%^&*()_+{}|:"<>?]', password):
            raise forms.ValidationError('Error')
        elif len(password) < 10:
            raise forms.ValidationError('Error')
        return password
    

    def clean_password2(self):
        cd = self.cleaned_data
        password = cd.get('password')
        password2 = cd.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Password do not match.')
        
        return password2
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}))

    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True

class AuthenticationFormWithCaptcha(AuthenticationForm):
    captcha = ReCaptchaField()

