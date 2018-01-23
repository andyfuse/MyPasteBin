from rest_framework import serializers

from .models import Post, Syntax


class SyntaxSerializer(serializers.ModelSerializer):
	class Meta:
		model = Syntax
		fields = ('syntax_name',)


class PostListViewSerializer(serializers.ModelSerializer):
	syntax = serializers.SlugRelatedField(slug_field="syntax_name", read_only=True)
	post_detail = serializers.HyperlinkedIdentityField(view_name="api-post")
	
	class Meta:
		model = Post
		fields = ('title', 'code', 'syntax', 'ttl_option', 'post_detail')


class PostSerializer(serializers.ModelSerializer):
	class  Meta:
		model = Post
		fields = ('title', 'code', 'syntax', 'ttl_option')
