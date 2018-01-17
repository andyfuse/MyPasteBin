from django.views.generic import DetailView, DeleteView, TemplateView
from django.conf.urls import i18n, patterns, include, url

from app import views
from app.models import Post

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^i18n/', include('django.conf.urls.i18n'), name="set_language"),
    url(r'^view/(?P<pk>\d+)/$', DetailView.as_view(model=Post,
    											   template_name="app/view.html"),
    							name='post-view'),
    url(r'^deleted/$',TemplateView.as_view(template_name="app/deleted.html"),
    	                                   name='successful_delete'),
    url(r'^del/(?P<pk>\d+)/$', views.delete_post.as_view(), name='post-delete'),
)