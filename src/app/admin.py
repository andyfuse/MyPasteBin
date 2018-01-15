from django.contrib import admin

from .models import Syntax, Post


class PostAdminPanel(admin.ModelAdmin):
	readonly_fields = ("created",)
	fieldsets = [
		("About", {"fields": ["title"]}),
		("Date information", {"fields": ["created", "time_to_live", "ttl_option"], "classes": ["collapse",]}),
		("Code", {"fields": ["syntax", "code"]})
	]


admin.site.register(Syntax)
admin.site.register(Post, PostAdminPanel)