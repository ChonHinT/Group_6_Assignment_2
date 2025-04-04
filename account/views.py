from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from orders.views import user_orders
from .forms import RegistrationForm, UserEditForm
from .models import UserBase
from .tokens import account_activation_token
from django.contrib.auth import authenticate, login
from axes.decorators import axes_dispatch
from django.contrib.auth.views import LoginView
from .forms import AuthenticationFormWithCaptcha




@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request,
                  'account/user/dashboard.html',
                  {'section': 'profile', 'orders': orders})


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request) # use django's logout method to clear the user's session data
    return redirect('account:delete_confirmation')


def account_register(request):

    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
        else:
            error_message = "The password you provided is too common or does not meet the requirement. Please choose a different one."
            return render(request, 'account/registration/register.html', {'form': registerForm, 'error_message':error_message})
    else:
        registerForm = RegistrationForm()
        
    return render(request, 'account/registration/register.html', {'form': registerForm})



def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')

@axes_dispatch
def login_view(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, user_name=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
    return render(request, 'account/login.html')

 
class LoginViewWithCaptcha(LoginView):
    form_class = AuthenticationFormWithCaptcha




