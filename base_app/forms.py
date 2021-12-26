from django import forms
from .models import ModelFormRegistration, ModelFormMessage


class FormRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "name", 'class': "form-control", 'id': "name",
                               'placeholder': "Your Name", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars"
                           }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "email", 'class': "form-control", 'name': "email", 'id': "email", 'placeholder': "Your Email",
        'data-rule': "email", 'data-msg': "Please enter a valid email"
    }))

    count_of_people = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': "number", 'class': "form-control", 'name': "people", 'id': "people", 'placeholder': "# of people",
        'data-rule': "minlen:1", 'data-msg': "Please enter at least 1 chars"
    }))
    message = forms.CharField(max_length=150, widget=forms.Textarea(attrs={
        'class': "form-control", 'name': "message", 'rows': "5", 'placeholder': "Message"
    }))

    class Meta:
        model = ModelFormRegistration
        fields = ['name', 'email', 'count_of_people', 'message', 'date']
        widget = {
            'date': forms.DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': "date"
            })
        }


class FormMessage(forms.ModelForm):
    name = forms.CharField(max_length=15,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "name", 'class': "form-control", 'id': "name", 'placeholder': "Your Name",
                           }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "email", 'class': "form-control", 'name': "email", 'id': "email", 'placeholder': "Your Email",
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control", 'name': "subject", 'id': "subject", 'placeholder': "Subject",
    }))
    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'class': "form-control", 'name': "message", 'rows': "5", 'placeholder': "Message",
    }))
    class Meta:
        model = ModelFormMessage
        fields = ['name', 'email', 'subject', 'message']