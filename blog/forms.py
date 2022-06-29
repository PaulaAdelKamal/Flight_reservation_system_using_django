from django import forms

from blog.models import Booking

class Class(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['classes', 'price', 'user', 'flight']