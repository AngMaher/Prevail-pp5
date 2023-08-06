from django import forms
from .models import Success_Stories


class StoryForm(forms.ModelForm):

    class Meta:
        model = Success_Stories
        fields = '__all__'
