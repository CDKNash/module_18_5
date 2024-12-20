from django.shortcuts import render
from django.template.defaultfilters import title
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')


def game(request):
    title_g = "Игры"
    games = {"Atomic Heart", "Cyberpunk 2077", "PayDay 2"}
    context = {
        'title_g': title_g,
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    title_p = "Корзина"
    content_p = "Это всё иллюзия и ничего не купите (:"
    context = {
        "title_p": title_p,
        "content_p": content_p
    }
    return render(request, 'fourth_task/cart.html', context)


def menu(request):
    Title = "Главная страница"
    main = "Главная"
    game = "Магазин"
    cart = "Корзина"
    context = {
        'Title': Title,
        'main': main,
        'game': game,
        'cart': cart,
    }
    return render(request, "fourth_task/menu.html", context)
