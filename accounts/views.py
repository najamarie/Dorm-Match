# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from dormmatch.models import UserProfile

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()

        # Check if the UserProfile already exists; create one if it doesn't
        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'gender': form.cleaned_data.get('gender', ''),
                'school': form.cleaned_data['school'],
                'degree_program': form.cleaned_data['degree_program'],
                'birthday': form.cleaned_data['birthday'],
            }
        )
        if not created:
            # Optional: Update existing profile fields if necessary
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.email = form.cleaned_data['email']
            profile.gender = form.cleaned_data.get('gender', '') 
            profile.school = form.cleaned_data['school']
            profile.degree_program = form.cleaned_data['degree_program']
            profile.birthday = form.cleaned_data['birthday']
            profile.save()

        return super().form_valid(form)
