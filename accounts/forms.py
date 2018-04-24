from django import forms
from django.contrib.auth.models import User
from .models import Profile, Logro

class NewLogroForm(forms.ModelForm):
	class Meta:
		model = Logro
		fields = '__all__'
		#exclude = ['user']


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={}))
	password2 = forms.CharField(label='Repite tu contraseña',
		widget=forms.PasswordInput(attrs={}))
	username = forms.CharField(label='Nombre de Usuario',widget=forms.TextInput(attrs={}))
	email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={}))
	
	class Meta:
		model = User
		fields = ('username', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd ['password2']:
			raise forms.ValidationError('Los passwords no coinciden')
		return cd['password2']

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']