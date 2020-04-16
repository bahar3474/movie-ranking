from django import forms


from .models import Member


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Member
        fields = [
            'first_name',
            'username',
            'password'
        ]

