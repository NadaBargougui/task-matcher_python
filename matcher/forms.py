from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
