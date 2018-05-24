from django.views.generic import TemplateView
from blog.models import Category, Article


class IndexView(TemplateView):
    template_name = 'blog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        context.update({'categories': categories})
        return self.render_to_response(context)


class CategoryView(TemplateView):
    template_name = 'blog/category.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(id=kwargs.get('category_id'))
        articles = Article.objects.filter(category_id=category.id)

        context.update({
            'category': category,
            'articles': articles
        })

        return self.render_to_response(context)


class ArticleView(TemplateView):
    template_name = 'blog/article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(id=kwargs.get('article_id'))

        context.update({
            'article': article
        })

        return self.render_to_response(context)
