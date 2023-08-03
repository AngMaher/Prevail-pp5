from django.db import models
from classes.models import Classes


class Membership(models.Model):

    class_choice = models.ForeignKey(Classes, on_delete=models.SET_NULL),
    first_name = models.CharField(max_length=50, blank=False, null=False),
    last_name = models.CharField(max_length=50, blank=True, null=True),
    email_address = models.EmailField(blank=False, null=False),

    def __str__(self):
        return self.email_address
