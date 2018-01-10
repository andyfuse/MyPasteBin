from django.contrib import admin

from .models import Syntax, Post


class PostAdminPanel(admin.ModelAdmin):
	exclude = ("time_to_live",)
	readonly_fields = ("created",)
	fieldsets = [
		("About", {"fields": ["title"]}),
		("Date information", {"fields": ["created"]}),
		("Code", {"fields": ["syntax", "code"], "classes": ["collapse",]})
	]


admin.site.register(Syntax)
admin.site.register(Post, PostAdminPanel)