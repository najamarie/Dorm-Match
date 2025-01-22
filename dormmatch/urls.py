from django.urls import path
from .views import HomePageView, WaitlistPageView, SolodormPageView, AboutusPageView
 # Correct import statement

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("waitlist/", WaitlistPageView.as_view(), name="waitlist"),
    path("solodorm/", SolodormPageView.as_view(), name="solodorm"), 
    path("aboutus/", AboutusPageView.as_view(), name="aboutus"), 
]

