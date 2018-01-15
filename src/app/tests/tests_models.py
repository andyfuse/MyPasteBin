from django.test import TestCase

from app.models import Post, Syntax


class PostTest(TestCase):

	def setUp(self):
		Post.objects.create(title='test1', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		Post.objects.create(title='test2', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name2"))

	def test_posts_created(self):
		self.assertEqual(Post.objects.all().count(), 2)
		post_obj = Post.objects.get(title="test1")
		self.assertTrue(isinstance(post_obj, Post))