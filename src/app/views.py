# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic import DeleteView

from app.models import Post
from app.forms import PostForm


def index(request):  
    if request.method == "POST":
        post_pk = request.POST.get("post_id", 0)
        post_obj = Post.objects.filter(pk=post_pk).first()
        form = PostForm(request.POST, instance=post_obj)   
        
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse('post-view', 
                                                args=(post.pk,)))
        else:  
            form.add_error(None,forms.ValidationError(
                                _(u"Кожне поле повинно бути заповненим!")))

    elif request.method == "GET":
        post_pk = request.GET.get("post_id", 0)
        post_obj = Post.objects.filter(pk=post_pk).first()
        
        form = PostForm(instance=post_obj)

    context = {
        "latest_posts": Post.objects.all().order_by('-created')[:5],
        "form": form,
        "post_on_edit": (post_pk 
                         if request.GET.get("mark") 
                         else 0)
    }
    return render(request, "app/index.html", context)


class delete_post(DeleteView):     
    model = Post
    template_name = 'app/delete_dialog.html'

    def get_success_url(self):
        return reverse('successful_delete')