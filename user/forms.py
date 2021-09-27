from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    email=forms.EmailField(required=True, label="e-mail")
    password=forms.CharField(label="Parolanız", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm=forms.CharField(label="Parola Tekrar", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=["username","email","password","confirm"]

    def clean(self):
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        if password!=confirm:
            self.add_error("password", "parolalar eşleşmiyor")
            self.add_error("confirm", "parolalar eşleşmiyor")
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email sistemde kayıtlı")

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı")
    password=forms.CharField(label="parola", widget=forms.PasswordInput(attrs={'class':'form-control'}))
