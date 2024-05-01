from django.shortcuts import render # type: ignore
from django.views.generic import TemplateView # type: ignore

# Create your views here.
class Index(TemplateView):
    template_name = "inventory/index.html"
