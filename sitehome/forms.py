from django import forms

class LoginForm(forms.Form):
    user_email = forms.EmailField(label='Your Email', max_length=500)
    user_password = forms.CharField(label='Your Password',max_length=500, widget=forms.PasswordInput)
    