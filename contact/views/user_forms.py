from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdtateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect("contact:login")

    return render(
        request,
        "contact/register.html",
        {
            "form": form,
        }
    )


def user_update(request):
    form = RegisterUpdtateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            "contact/register.html",
            {
                "form": form,
            }
        )

    form = RegisterUpdtateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            "contact/register.html",
            {
                "form": form,
            }
        )

    form.save()
    return render(
        request,
        "contact/register.html",
        {
            "form": form,
        }
    )
    # messages.success(request, "Atualização efetuada com sucesso")


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Login efetuado com sucesso")
            return redirect("contact:index")

        messages.error(request, "Usuário ou senha inválidos")

    return render(
        request,
        "contact/login.html",
        {
            "form": form,
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect("contact:index")
