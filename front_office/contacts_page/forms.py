from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            raise forms.ValidationError('Please enter your name.')

        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Please enter your email address.')

        if not email.endswith('@example.com'):
            raise forms.ValidationError(
                'Please enter a valid email address (e.g., johndoe@example.com).')

        return email

    def clean_message(self):
        message = self.cleaned_data['message']
        if not message:
            raise forms.ValidationError('Please enter your message.')

        return message
