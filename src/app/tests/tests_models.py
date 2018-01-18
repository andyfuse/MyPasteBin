import datetime

from django.test import TestCase
from django.utils import timezone

from app.models import Post, Syntax


class PostTest(TestCase):

	@staticmethod
	def validate_time_to_live(date_time):
		now_plus_10_min = timezone.now() + \
		 					   datetime.timedelta(minutes=10)
		if date_time <= now_plus_10_min:
			return True

		return False

	def test_posts_created(self):
		Post.objects.create(title='test1', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		Post.objects.create(title='test2', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name2"))
		post_obj = Post.objects.get(title="test1")
		self.assertTrue(isinstance(post_obj, Post))
		self.assertEqual(Post.objects.all().count(), 2)

	def test_setting_right_time_to_live_value(self):
		Post.objects.create(title='test1', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		post_obj = Post.objects.get(title="test1")
		self.assertEqual(post_obj.ttl_option, None)
		self.assertTrue(self.validate_time_to_live(post_obj.time_to_live), True)

	def test_making_slug_value(self):
		post_obj = Post.objects.create(title="making_test1", 
									   syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		self.assertEqual(post_obj.slug, "making_test1")
		post_obj_same_title = Post.objects.create(title="making_test1", 
									   syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		self.assertEqual(post_obj_same_title.slug, "making_test1_1")
		post_obj_same_title_again = Post.objects.create(title="making_test1", 
									   syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		self.assertEqual(post_obj_same_title_again.slug, "making_test1_1_2")