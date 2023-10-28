from django.db import models

class Ticket(models.Model):
    datetime = models.DateTimeField()
    location = models.CharField(max_length=200)

    # def __str__(self):
    #     return f"{self.datetime.strftime('%A')} {self.datetime.strftime('%m-%d-%Y')} {self.datetime.strftime('%H:%M')} - {self.location}"
