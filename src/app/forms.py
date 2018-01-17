# -*- encoding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

from app.models import Post, Syntax


class PostForm(forms.ModelForm):
	syntax = forms.ModelChoiceField(label=_(u"Оберіть мову:"),
									queryset=Syntax.objects.all().order_by('syntax_name'),
									widget=forms.Select(
												attrs={'class': "form-control"}))
	ttl_option = forms.ChoiceField(label=_(u"Оберіть час збереження"),
									choices=Post.TTL_OPTIONS,
									widget=forms.Select(attrs={'class': "form-control"}))
	
	class Meta:
		model = Post
		localized_fields = ('ttl_option', )
		fields = ("title", "syntax", "ttl_option", "code")
		labels = {
			"title": _(u"Заголовок:"),
			"code": _(u"Помістіть код тут:"),
		}
		widgets = {
			"title": forms.TextInput(attrs={'class': "form-control"}),
			"code": forms.Textarea(attrs={"class": "form-control",'rows': 25,
										 'cols': 70}),
		}