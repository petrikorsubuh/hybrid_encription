from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'username'
    }))
    password = forms.CharField(label='Password',widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'password',
        'placeholder':'password'
    }))

class RegisterFrom(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'first name'
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'last name'
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'username'
    }))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'email',
        'type':'email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'password',
        'type': 'password'
    }))
    password2 = forms.CharField(label='Conform Password', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'confirm password',
        'type': 'password'
    }))


class AES_Form(forms.Form):
    send_to = forms.CharField(label='Send To', widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'email',
        'placeholder':'email',

    }))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'message'
    }))
    key = forms.CharField(label='AES Key', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'key'
    }))


class Ntru_Form(forms.Form):
    key = forms.CharField(label='AES Key', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'key'
    }))
    pub_key = forms.CharField(label='Public Key', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'public key'
    }))
    priv_key = forms.CharField(label='Private Key', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'private key'
    }))



class Decript_NtruForm(forms.Form):
    msg_from = forms.CharField(label='Message From', widget=forms.TextInput(attrs={
        'class':'form-control',
        'type': 'email'
    }))
    msg_encript = forms.CharField(label='Message Encript', widget=forms.Textarea(attrs={
        'class':'form-control',

    }))
    priv_key = forms.FileField(label='Private Key')
    key_encript = forms.CharField(label='Key Encript', widget=forms.TextInput(attrs={
        'class':'form-control',

    }))

