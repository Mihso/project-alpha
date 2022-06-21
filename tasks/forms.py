from django import forms
from tasks.models import Task

class is_complete_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["is_completed"]