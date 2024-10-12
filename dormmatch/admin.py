from django.contrib import admin
from .models import UserProfile, DormAccommodation, BookingStatus

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'email', 'gender', 'school', 'degree_program')

class DormAccommodationAdmin(admin.ModelAdmin):
    list_display = ('dorm_id', 'dorm_class', 'room_type', 'no_of_occupied', 'occupied_status', 'price')

class BookingStatusAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'user_id', 'dorm_id', 'amount', 'book_status')


admin.site.register(DormAccommodation, DormAccommodationAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BookingStatus, BookingStatusAdmin)