from django import forms

class TodoForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.CharField(label="Email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),  max_length=100)
    password.widget.attrs['value'] = '' #For no auto complete in password field
