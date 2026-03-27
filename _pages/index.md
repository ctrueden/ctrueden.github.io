---
title: ctrue.name
layout: default
nav: Blog
nav_order: 1
---

{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
## {{ year.name }}

{% for post in year.items %}
- <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d" }}</time> &mdash; [{{ post.title }}]({{ post.url }})
{% endfor %}
{% endfor %}
