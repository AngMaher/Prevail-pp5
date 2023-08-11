from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from django_summernote.widgets import SummernoteWidget


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'description': SummernoteWidget()
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)  # noqa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        widgets = {
            'description': SummernoteWidget()
        }

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'friendly_name')
