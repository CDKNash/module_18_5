from django.shortcuts import render, HttpResponse
from .forms import UserRegister

# Create your views here.

users = ["Vulkan", "Noname", "Miller"]
info = {}


def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info_error(username, password, repeat_password, age)
        info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        info_error(username, password, repeat_password, age)
    return render(request, 'fifth_task/registration_page.html', info)


def info_error(username, password, repeat_password, age):
    if password != repeat_password:
        info['error'] = "Пароли не совпадают"
    elif age < 18:
        info['error'] = "Вы должны быть старше 18"
    elif username in users:
        info['error'] = "Пользователь уже существует"
    else:
        info['error'] = f'Приветствуем, {username}!'
        users.append(username)
        return info, users
