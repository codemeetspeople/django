from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view()),
    re_path(
        r'^(?P<category_id>[\d]+)/$',
        views.CategoryView.as_view()
    ),
    re_path(
        r'^(?P<category_id>[\d]+)/(?P<article_id>[\d]+)/$',
        views.ArticleView.as_view()
    ),
]
