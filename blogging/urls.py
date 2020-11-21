from django.urls import path

# from blogging.views import stub_view, list_view
from django.conf import settings
from django.conf.urls.static import static
from blogging.views import BlogListView
from blogging.views import BlogDetailView

"""
Assignment 8
After converting from FBV to CBV, this urlpatterns variable was removed

urlpatterns = [
    # path('', stub_view, name="blog_index"),
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', list_view, name="blog_detail"),
]
"""

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
