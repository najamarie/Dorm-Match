from django.contrib import admin
from .models import UserProfile, DormAccommodation, BookingStatus

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'gender','contact_number', 'school', 'degree_program')
    fields = ('contact_number', 'school','degree_program')  # Only these fields will be editable

    def has_add_permission(self, request):
        """Disable the add button in the admin for UserProfile."""
        return False

class DormAccommodationAdmin(admin.ModelAdmin):
    list_display = ('dorm_id', 'dorm_class', 'room_type', 'no_of_occupied', 'occupied_status', 'price')

class BookingStatusAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'user_id', 'dorm_id', 'amount', 'book_status')


admin.site.register(DormAccommodation, DormAccommodationAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BookingStatus, BookingStatusAdmin)