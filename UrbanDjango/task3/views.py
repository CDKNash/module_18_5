from django.shortcuts import render
from django.template.defaultfilters import title
from django.views.generic import TemplateView

# Create your views here.
def main_list(request):
    title = "Главная страница"
    main = "Главная"
    game = "Магазин"
    basket = "Корзина"
    context = {
        'title': title,
        'main': main,
        'game': game,
        'basket': basket,
    }
    return render(request, 'cart.html', context)

class game(TemplateView):
    template_name = 'games.html'
    title_g = "Игры"


    context = {
        'title_g': title_g,

    }

def basket(request):
    title_p = "Это всё иллюзия и ничего не купите (:"

    context = {
        "title_p": title_p
    }
    return render(request, 'platform.html', context)