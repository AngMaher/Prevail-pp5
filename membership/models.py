from django.db import models


class Membership(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, default='name')  # noqa
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.EmailField(blank=False, null=False)
    Area = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name
