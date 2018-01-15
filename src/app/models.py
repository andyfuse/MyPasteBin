import datetime

from django.db import models


TTL_OPTION = (
	(None, "----"),
	("minutes=10", "10 minutes"),
	("hours=1", "1 hour"),
	("days=1", "1 day"),
	("days=7", "1 week"),
	("days=30", "1 month")
)


class Syntax(models.Model):
	syntax_id = models.AutoField(primary_key=True)
	syntax_name = models.CharField(max_length=20)

	def __str__(self):
		return self.syntax_name


class Post(models.Model):
	title = models.CharField(max_length=40)
	code = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	time_to_live = models.DateTimeField(blank=True)
	syntax = models.ForeignKey(Syntax)

	ttl_option = models.CharField(max_length=10,
								  choices=TTL_OPTION,
								  null=True,
								  blank=True)

	def __str__(self):
		return "{} {}".format(self.syntax.syntax_name,
							  self.title)

	def save(self, *args, **kwargs):
		if self.ttl_option is None:
			self.time_to_live = datetime.datetime.now() + \
								datetime.timedelta(minutes=10)
		else:
			k, v = self.ttl_option.split("=")
			self.time_to_live = datetime.datetime.now() + \
								datetime.timedelta(**{k:int(v)})

		super(Post, self).save(*args, **kwargs)
