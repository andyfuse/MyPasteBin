from django.test import TestCase

from app.forms import PostForm
from app.models import Post, Syntax


class PostFormTest(TestCase):

	def test_form_valid(self):
		Syntax.objects.create(syntax_name="syntax_name1")
		post_obj_data = {
			u'title': u'title', 
			u'code': u'code', 
			u'ttl_option': u'minutes=10',
			u'syntax': "1"
		}
		post_form = PostForm(data=post_obj_data)

		self.assertTrue(post_form.is_valid())

	def test_form_invalid(self):
		Syntax.objects.create(syntax_name="syntax_name1")
		post_obj_data = {
			u'title': u'', 
			u'code': u'', 
			u'ttl_option': u'minutes=10',
			u'syntax': "1"
		}
		post_form = PostForm(data=post_obj_data)

		self.assertFalse(post_form.is_valid())

	def test_form_creates_model(self):
		Syntax.objects.create(syntax_name="syntax_name1")
		post_obj_data = {
			u'title': u'post_1', 
			u'code': u'code_1', 
			u'ttl_option': u'minutes=10',
			u'syntax': "1"
		}
		post_form = PostForm(data=post_obj_data)
		post_form.save()
		post_obj = Post.objects.get(title=post_obj_data['title'])

		self.assertTrue(isinstance(post_obj, Post))
		self.assertEqual(post_obj.title, post_obj_data['title'])