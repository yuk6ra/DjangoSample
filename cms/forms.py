from django.forms import ModelForm
from cms.models import Habit, Record


class HabitForm(ModelForm):

    class Meta:
        model = Habit
        fields = ('habit_name', 'goal', 'start_date',)

class RecordForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Record
        fields = ('comment', 'name', 'date')
