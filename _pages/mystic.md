---
layout: page
title: Mystic Magic
permalink: /mystic/
category: rules
snippet: A flexible alternative D&D magic system.
---
Mystic magic is a flexible alternative magic system for any D&D campaign
world. It can coexist with standard arcane and divine magic or replace
it altogether.

* * *

## Contents
{% for page in site.pages %}
  {% if page.category == 'mystic1' %}  
* [{{ page.title }}](#{{ page.url }})
  {% endif %}
  {% if page.category == 'mystic2' %}  
    * [{{ page.title }}](#{{ page.url }})
  {% endif %}
{% endfor %}

{% for page in site.pages %}
  {% if page.category == 'mystic1' %}  
<a name="{{ page.url }}"></a>
* * *
## {{ page.title }}
{{ page.content }}
  {% endif %}
  {% if page.category == 'mystic2' %}  
<a name="{{ page.url }}"></a>
* * *
### {{ page.title }}
{{ page.content }}
  {% endif %}
{% endfor %}
