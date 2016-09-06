from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from .form import PostForm


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()
        # mensaje de aprobacion
        return HttpResponseRedirect(instance.get_absolute_url())

    # if request.method == 'POST':
        # print request.POST.get('title')
        # print request.POST.get('content')
        # title = request.POST.get('title')
        # Post.objects.create(title=title)
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': 'Detail'
    }
    return render(request, 'post_detail.html', context)
    # return HttpResponse("<h1>Detail</h1>")

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'
    }

    # if request.user.is_authenticated():
    #     context = {
    #         'title': 'My user List'
    #         }
    # else:
    #     context = {
    #         'title': 'List'
    #         }

    return render(request, 'index.html', context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # mensaje de aprobacion
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'instance': instance,
        'title': instance.title,
        'form': form,
    }
    return render(request, 'post_form.html', context)

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
