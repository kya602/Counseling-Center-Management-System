from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Counselor(models.Model):
    name = models.CharField(max_length=250)
    nsu_id = models.CharField(max_length=12, null=True)
    designation = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000, null=True)
    mobile_no = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=70, null=True)
    password = models.CharField(max_length=20)
    photo = models.ImageField(default='download.png')

    def get_absolute_url(self):
        return reverse('counselor:profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(default=False)
    date = models.DateField(blank=True)

    SLOT_1 = 1
    SLOT_2 = 2
    SLOT_3 = 3
    SLOT_4 = 4
    SLOT_5 = 5
    SLOT_6 = 6
    SLOT_7 = 7
    SLOT_8 = 8
    SLOT_9 = 9
    SLOT_10 = 10
    SLOT_11 = 11

    SLOTS = (
        (SLOT_1, '09:00 AM - 10:00 AM'),
        (SLOT_2, '10:00 AM - 11:00 AM'),
        (SLOT_3, '11:00 AM - 12:00 PM'),
        (SLOT_4, '12:00 PM - 01:00 PM'),
        (SLOT_5, '02:00 PM - 03:00 PM'),
        (SLOT_6, '03:00 PM - 04:00 PM'),
        (SLOT_7, '04:00 PM - 05:00 PM'),
        (SLOT_8, '05:00 PM - 06:00 PM'),
        (SLOT_9, '06:00 PM - 07:00 PM'),
        (SLOT_10, '07:00 PM - 08:00 PM'),
        (SLOT_11, '08:00 PM - 09:00 PM')
    )
    slot = models.IntegerField(choices=SLOTS, default=SLOT_1)


    def __str__(self):
        return "%s at %s" %(self.date, self.slot)
