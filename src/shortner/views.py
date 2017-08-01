from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from. forms import SubmitUrlForm 
from .models import ShortItURL

from analytics.models import ClickEvent

'''
    You can set only template and context variables for any method.
    View class will automatically call render.
'''
class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        return render(request, "shortner/home.html", {"form": form})

    def post(self, request, *args, **kwargs):
        #url = request.POST.get('url')
        form = SubmitUrlForm(request.POST)
        context = {"form": form}
        template = "shortner/home.html"

        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortItURL.objects.get_or_create(url=new_url)
            context = {
                "object" : obj,
                "created" : created,
            }
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/already-exists.html"

        return render(request, template, context)

class RedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print("r", shortcode)
        obj = get_object_or_404(ShortItURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect('http://'+obj.url)
