from django.db import models
from classes.models import Classes


class Success_Stories(models.Model):
    class_attended = models.ForeignKey(
        Classes, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='success_stories')
    title = models.CharField(max_length=254, blank=False)
    weight_loss = models.IntegerField(null=False, blank=False)
    start_weight = models.IntegerField(null=False, blank=False)
    weight_now = models.IntegerField(null=False, blank=False)
    image_before = models.ImageField(null=True, blank=True)
    image_after = models.ImageField(null=True, blank=True)
    content = models.TextField()
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
