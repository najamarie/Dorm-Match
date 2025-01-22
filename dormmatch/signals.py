# dormmatch/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

# Flag to avoid recursion
UPDATE_IN_PROGRESS = False

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    global UPDATE_IN_PROGRESS
    if UPDATE_IN_PROGRESS:
        return  # Skip if update is already in progress

    if created:
        # Create a new UserProfile if the User is created
        UserProfile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            gender=instance.gender,
            school=instance.school,
            degree_program=instance.degree_program,
            birthday=instance.birthday,
            contact_number=instance.contact_number,
        )
    else:
        # Update UserProfile when CustomUser changes
        profile = instance.profile
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.email = instance.email
        profile.gender = instance.gender
        profile.school = instance.school
        profile.degree_program = instance.degree_program
        profile.birthday = instance.birthday
        profile.contact_number = instance.contact_number

        # Set the flag to prevent recursion
        UPDATE_IN_PROGRESS = True
        profile.save()
        UPDATE_IN_PROGRESS = False

@receiver(post_save, sender=UserProfile)
def update_user_from_profile(sender, instance, **kwargs):
    global UPDATE_IN_PROGRESS
    if UPDATE_IN_PROGRESS:
        return  # Skip if update is already in progress

    user = instance.user
    user.first_name = instance.first_name
    user.last_name = instance.last_name
    user.email = instance.email
    user.gender = instance.gender
    user.school = instance.school
    user.degree_program = instance.degree_program
    user.birthday = instance.birthday
    user.contact_number = instance.contact_number

    # Set the flag to prevent recursion
    UPDATE_IN_PROGRESS = True
    user.save()
    UPDATE_IN_PROGRESS = False
