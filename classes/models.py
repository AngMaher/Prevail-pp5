from django.db import models


class Classes(models.Model):
    """Model to hold information for each class"""
    leader_name = models.CharField(max_length=200)
    class_county = models.CharField(max_length=50)
    class_town = models.CharField(max_length=50)
    class_address = models.CharField(max_length=200)
    class_day = models.CharField(max_length=200)
    class_time = models.TimeField(blank=True, null=True)
    class_info = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.leader_name
