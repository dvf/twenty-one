import datetime
from django import forms
from django.forms import TextInput

from habit.models import Habit


class HabitCreateForm(forms.ModelForm):
    class Meta:
        model = Habit
        exclude = ['user', ]

    def __init__(self, *args, **kwargs):
        super(HabitCreateForm, self).__init__(*args, **kwargs)

        # Add Bootstrap's `form-control` to all input fields
        for k, v in self.fields.items():
            self.fields[k].widget.attrs.update({'class': 'form-control'})