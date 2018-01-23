from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from app.forms import PostForm
from app.models import Post, Syntax


class PostViewTest(TestCase):

	def test_home_view(self):
		user_info = dict(username='testuser', password='12345')
		user = User.objects.create_user(**user_info)
		login = self.client.login(**user_info)

		Post.objects.create(title='test1', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		Post.objects.create(title='test2', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name2"))

		response = self.client.get(reverse("index"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['latest_posts']), 2)
		self.assertEqual(response.context['user'].username, user_info["username"])

	def test_post_creating_new_post(self):
		Syntax.objects.create(syntax_name="syntax_name1")
		post_obj_data = {
			u'title': u'title', 
			u'code': u'code', 
			u'ttl_option': u'minutes=10',
			u'syntax': "1"
		}
		response = self.client.post(reverse('index'), data=post_obj_data)

		self.assertEqual(response.status_code, 302)

		post_obj = Post.objects.get(title=post_obj_data["title"])
		
		self.assertEqual(response.url,
						 "http://testserver" + reverse("post-view", 
												kwargs={'slug': post_obj.slug}))

	def test_invalid_post_request(self):
		Syntax.objects.create(syntax_name="syntax_name1")
		post_obj_data = {
			u'title': u'', 
			u'code': u'code', 
			u'ttl_option': u'minutes=10',
			u'syntax': "1"
		}
		response = self.client.post(reverse('index'), data=post_obj_data)

		self.assertFalse(response.context['form'].is_valid())
		self.assertTrue("title" in response.context['form'].errors.keys())

	def test_post_list_api_call(self):
		user_info = dict(username='testuser', password='12345')
		user = User.objects.create_user(**user_info)
		user.is_staff = True
		user.save()
		self.client.login(**user_info)
		Post.objects.create(title='test1', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name1"))
		Post.objects.create(title='test2', code='code',
							syntax=Syntax.objects.create(syntax_name="syntax_name2"))
		response = self.client.get(reverse("api-list-post"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.data), 2)

	def test_post_create_api_call(self):
		Syntax.objects.create(syntax_name="syntax_name1")
		user_info = dict(username='testuser', password='12345')
		user = User.objects.create_user(**user_info)
		user.is_staff = True
		user.save()
		self.client.login(**user_info)
		post_obj_data = {
			'title': 'title',
			'code': 'code',
			'ttl_option': 'minutes=10',
			'syntax': "1"
		}
		response = self.client.post(reverse('api-list-post'), data=post_obj_data)

		self.assertEqual(response.status_code, 201)
		self.assertTrue(Post.objects.filter(title=post_obj_data["title"]).exists())