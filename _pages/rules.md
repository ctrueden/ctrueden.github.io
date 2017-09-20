---
layout: page
title: Rules
permalink: /rules
category: menu
---

Here you'll find homebrew D&D and other gaming materials.

{% for page in site.pages %}
  {% if page.category == 'rules' %}  
* [{{ page.title }}]({{ page.url }}) - {{ page.snippet }}
  {% endif %}
{% endfor %}
