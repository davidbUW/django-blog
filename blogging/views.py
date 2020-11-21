from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")


"""
Assignment 8
After converting from FBV to CBV, this view function was removed

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    # template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    # body = template.render(context)
    return render(request, 'blogging/list.html', context)
"""

"""
Assignment 8
This CBV works by the assignement says to use a `queryset` class attribute in 
your list view instead of a `model` class attribute

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = '-published_date'
    template_name = 'blogging/list.html'

"""


class BlogListView(ListView):
    """
    Assignment 8
     when no context_object_name variable is used, a default object_list is
     created

     context_object_name = 'posts'
    """

    queryset = Post.objects.exclude(published_date=None).order_by("-published_date")
    paginate_by = 3
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
