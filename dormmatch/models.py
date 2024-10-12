from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('CF', 'Cisgender Female'),
        ('CM', 'Cisgender Male'),
        ('TM', 'Transgender Male'),
        ('TF', 'Transgender Female'),
        ('NB', 'Non-Binary'),
    ]

    user_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    school = models.CharField(max_length=255)
    degree_program = models.CharField(max_length=255)

    def __str__(self):
        return f"User-{self.user_id} --{self.first_name} {self.last_name}"

class DormAccommodation(models.Model):
    DORM_CLASS_CHOICES = [
        ('A', 'Class A'),
        ('B', 'Class B'),
    ]

    ROOM_TYPE_CHOICES = [
        ('Solo', 'Solo'),
        ('Shared', 'Shared'),
    ]

    OCCUPIED_STATUS_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]

    dorm_id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    dorm_class = models.CharField(max_length=1, choices=DORM_CLASS_CHOICES)
    room_type = models.CharField(max_length=6, choices=ROOM_TYPE_CHOICES)
    no_of_occupied = models.IntegerField()
    occupied_status = models.CharField(max_length=3, choices=OCCUPIED_STATUS_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.room_type == 'Solo':
            self.no_of_occupied = 1
            self.occupied_status = 'YES'
        elif self.room_type == 'Shared':
            if self.no_of_occupied == 4:
                self.occupied_status = 'YES'
            else:
                self.occupied_status = 'NO'

        if self.dorm_class == 'A' and self.room_type == 'Solo':
            self.price = 16000
            self.description = "40 square meters room with a private bathroom and balcony."
        elif self.dorm_class == 'A' and self.room_type == 'Shared':
            self.price = 18000
            self.description = "40 square meters room divided into four sections, each with a bed, and featuring two bathrooms, and a balcony."
        elif self.dorm_class == 'B' and self.room_type == 'Solo':
            self.price = 12000
            self.description = "35 square meters rooms with private bathroom."
        elif self.dorm_class == 'B' and self.room_type == 'Shared':
            self.price = 14000
            self.description = "35 square meters room divided into four sections, each with a bed, and featuring two bathrooms."


        if not self.dorm_id:
            last_dorm = DormAccommodation.objects.order_by('-dorm_id').first()
            if last_dorm and last_dorm.dorm_id[3:].isdigit():
                last_id = int(last_dorm.dorm_id[3:]) 
                self.dorm_id = f"DRM{last_id + 1:04d}"
            else:
                self.dorm_id = "DRM0001"

        super(DormAccommodation, self).save(*args, **kwargs)

    def __str__(self):
        return f"Dorm {self.dorm_id} - {self.dorm_class} {self.room_type}"

class BookingStatus(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('ForPayment', 'For Payment'),
        ('Paid', 'Paid'),
    ]

    book_id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dorm_id = models.ForeignKey(DormAccommodation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)  # Amount based on the price in DormAccommodation
    book_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.book_id:
            last_booking = BookingStatus.objects.order_by('-book_id').first()
            if last_booking and last_booking.book_id[4:].isdigit():
                last_id = int(last_booking.book_id[4:])
                self.book_id = f"BOOK{last_id + 1}" 
            else:
                self.book_id = "BOOK1"

        if self.dorm_id:
            self.amount = self.dorm_id.price

        super(BookingStatus, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.book_id} - User {self.user_id} - Dorm {self.dorm_id}"