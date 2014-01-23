# Create your views here.
from django.views.generic import TemplateView


class RootView(TemplateView):
    template_name = 'gsk/root.html'