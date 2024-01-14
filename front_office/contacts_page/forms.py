from django import forms
from django.core.validators import EmailValidator, RegexValidator, validate_email
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'phone', 'message', 'created_at')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == '':
            raise forms.ValidationError('Name is required')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            # Use Django's built-in validate_email for email validation
            validate_email(email)
        except forms.ValidationError as e:
            raise forms.ValidationError('Enter a valid email address') from e

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Apply RegexValidator directly to the phone field
        validator = RegexValidator(
            '^[0-9]{10}$', message='Enter a valid phone number')
        validator(phone)
        return phone

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message == '':
            raise forms.ValidationError('Message is required')
        return message
