import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class Syntax(models.Model):
	syntax_id = models.AutoField(primary_key=True)
	syntax_name = models.CharField(max_length=20)

	def __str__(self):
		return self.syntax_name


class Post(models.Model):
	TTL_OPTIONS = (
		(None, "----"),
		("minutes=10", "10 minutes"),
		("hours=1", "1 hour"),
		("days=1", "1 day"),
		("days=7", "1 week"),
		("days=30", "1 month"))

	title = models.CharField(max_length=40)
	slug = models.SlugField(max_length=50, unique=True)
	code = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	time_to_live = models.DateTimeField(blank=True)
	syntax = models.ForeignKey(Syntax)

	ttl_option = models.CharField(max_length=10,
								  choices=TTL_OPTIONS,
								  null=True,
								  blank=True)
	
	def make_slug(self, new_slug=None):
		slug = slugify(self.title)
		if new_slug is not None:
			slug = new_slug
		qs = Post.objects.filter(slug=slug).order_by("-id")
		if qs.exists():
			new_slug = "{}_{}".format(slug, qs.first().id)
			return 	self.make_slug(new_slug=new_slug)
		return slug

	def get_absolute_url(self):
		return reverse("post-view", kwargs={"slug": self.slug})

	def __str__(self):
		return "{} {}".format(self.syntax.syntax_name,
							  self.title)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self.make_slug()

		if self.ttl_option is None:
			self.time_to_live = datetime.datetime.now() + \
								datetime.timedelta(minutes=10)
		else:
			k, v = self.ttl_option.split("=")
			self.time_to_live = datetime.datetime.now() + \
								datetime.timedelta(**{k:int(v)})

		super(Post, self).save(*args, **kwargs)
