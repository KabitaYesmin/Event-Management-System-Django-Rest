# Create your models herre

from django.db import models
from django.utils.timezone import now


class Event(models.Model):
     class StateChoice(models.TextChoices):
         Alabama = 'Alabama, AL'
Tennessee = 'Tennessee, TN'
Texas = 'Texas, TX'
Utah = 'Utah, UT'
Vermont = 'Vermont, VT'
Virginia = 'Virginia, VA'
Washington = 'Washington, WA'
West_Virginia = 'West Virginia, WV'
Wisconsin = 'Wisconsin, WI'
Wyoming = 'Wyoming, WY'
Alabama = 'Alabama, AL'
Alaska = 'Alaska, AK'
Arizona = 'Arizona, AZ'
Arkansas = 'Arkansas, AR'
California = 'California, CA'
Colorado = 'Colorado, CO'
Connecticut = 'Connecticut, CT'


title = models.CharField(max_length=50)
place = models.CharField(max_length=50)
city = models.CharField(max_length=10)


class StateChoice:
    choices = None
    Alabama = None


state = models.CharField(max_length=50,
                         choices=StateChoice.choices, default=StateChoice.Alabama)
zipcode = models.CharField(max_length=10)
other = models.CharField(max_length=50)
start_date = models.CharField(max_length=25)
end_date = models.CharField(max_length=25)
category = models.CharField(max_length=25)
list_date = models.DateTimeField(default=now, blank=True)


class Meta: verbose_name_plural = 'events'


def str_(self):
    return self.title

# from django.contrib.auth.models import User
# from django.db import models
#
#
# class Event(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=200)
#     organizer = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#
# class Attendee(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.user.username} - {self.event.title}"
#
#
# class Meta:
#     db_table = "dt_table"
