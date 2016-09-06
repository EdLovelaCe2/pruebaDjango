from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Post
from .form import PostForm


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
		messages.error(request, "Not Successfully Created")

    context = {
        'form': form,
        }
    return render(request, 'post_form.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': instance.title,
    }
    return render(request, 'post_detail.html', context)
    # return HttpResponse("<h1>Detail</h1>")

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'
    }

    return render(request, 'post_list.html', context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'instance': instance,
        'title': instance.title,
        'form': form,
    }
    return render(request, 'post_form.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete
    messages.success(request, "Successfully Deleted")
    return redirect('posts:list')
