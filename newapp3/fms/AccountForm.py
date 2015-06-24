from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(
		required=True,
		label=u"username",
		error_messages={'required':'please enter your username'},
		widget=forms.TextInput(
			attrs={
				'placeholder' :u"username",
			}
		),
	)
	password = forms.CharField(
		required=True,
		label=u"password",
		error_messages={'required':u"please enter your password"},
		widget=forms.PasswordInput(
			attrs={
				'placeholder':u"password",
			}	
		),
	)
	
	email =forms.EmailField()
'''	
	def clean(self):
		if not self.is_vaild():
			raise forms.ValidationError(u"must enter username and password")
		else:
			cleaned_data = super(LoginForm, self).clean()
'''