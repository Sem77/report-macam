from django import forms


class AuthenticationForm(forms.Form):

    username = forms.CharField(
        label="Nom d'utilisateur : ",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nom d\'utilisateur',
            }
        ),
        max_length=255,
        required=True,
    )

    password = forms.CharField(
        label="Mot de passe : ",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe'
            }
        ),
        required=True,
    )