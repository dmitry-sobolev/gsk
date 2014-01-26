# Create your views here.
from django.views.generic import TemplateView, ListView
from gsk.models import Garage


class RootView(ListView):
    template_name = 'gsk/root.html'
    model = Garage
    context_object_name = 'garages'