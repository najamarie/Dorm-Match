from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class WaitlistPageView(TemplateView):
    template_name = "waitlist.html"

class SolodormPageView(TemplateView):
    template_name = 'solodorm.html'

class AboutusPageView(TemplateView):
    template_name = 'aboutus.html'