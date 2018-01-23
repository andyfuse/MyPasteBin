from django.test import TestCase

from app.serializers import PostSerializer, SyntaxSerializer
from app.models import Post, Syntax


class PostSerializerTest(TestCase):

	def test_post_serializer_is_valid(self):
		Syntax.objects.create(syntax_name="syntax_name1")
		post_obj_data = {
			u'title': u'title', 
			u'code': u'code', 
			u'ttl_option': u'minutes=10',
			u'syntax': "1"
		}
		post_serializer = PostSerializer(data=post_obj_data)
		
		self.assertTrue(post_serializer.is_valid())


	def test_post_serializer_is_invalid(self):
		post_obj_data = {
			u'title': u'title', 
			u'code': u'code', 
			u'ttl_option': u'minutes=10',
			u'syntax': "1"
		}
		post_serializer = PostSerializer(data=post_obj_data)
		
		self.assertFalse(post_serializer.is_valid())