from django.db import models


class Classes(models.Model):
    leader_name = models.CharField(max_length=200, unique=True)
    class_address = models.CharField(max_length=200)
    class_day = models.CharField(max_length=200)
    class_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.leader_name
