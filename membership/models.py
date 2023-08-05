from django.db import models


class Membership(models.Model):
    member_first_name = models.CharField(max_length=50, blank=False, null=False)
    member_last_name = models.CharField(max_length=50, blank=True, null=True)
    member_email_address = models.EmailField(blank=False, null=False)
    class_choice = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.member_first_name
