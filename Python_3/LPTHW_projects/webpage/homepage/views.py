from django.views.generic.edit import CreateView

from .models import Name


class HomepageView(CreateView):
    model = Name
    template_name = "home.html"
    fields = ["name"]