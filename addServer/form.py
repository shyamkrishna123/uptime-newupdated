from django import forms

from .models import addServer

class PostForm(forms.ModelForm):

    class Meta:
        model = addServer
        fields = ('user', 'details' ,'created_date', 'server','ipAddress',)