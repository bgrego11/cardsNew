from django import forms
class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class NewGameForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = 'name',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    host = forms.IntegerField(
        required = True,
        label = 'host',
        
    )

class JoinGameForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = 'name',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    player = forms.IntegerField(
        required = True,
        label = 'player',
        
    )