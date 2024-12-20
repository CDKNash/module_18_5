from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def django_app(request):
    return render(request, 'class_template.html')

class func_app(TemplateView):
    template_name = 'func_template.html'