from django import forms
from django.core import validators

class FormName(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label="ReEnter Mail")
	text = forms.CharField(widget=forms.Textarea)
	#botcatcheer =forms.CharField(required=False,widget=forms.HiddenInput)

	def clean(self):
		all_clean_data = super.clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.Error("Enter mail correctly")
