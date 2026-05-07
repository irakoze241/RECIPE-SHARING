from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
