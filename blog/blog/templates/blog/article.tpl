{% extends "core/base.tpl" %}

{% block title %}{{ article.title }}{% endblock %}

{% block content %}
    <h1>{{ article.title }}</h1>
    <br>
    <img src="{{ article.image.url }}">
    <p>{{ article.content }}</p>
{% endblock %}