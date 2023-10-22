from django import forms
from App.models import AppModel
class Form(forms.ModelForm):

    class Meta:
        model = AppModel
        fields = "__all__"
