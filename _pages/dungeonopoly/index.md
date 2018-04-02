---
layout: page
title: Dungeonopoly
permalink: /rules/dungeonopoly/index
category: rules
snippet: A horrific Monopoly/D&amp;D crossbreed.
---
Dungeonopoly is a horrific Monopoly/D&D crossbreed. The game is an extension of Monopoly, played with the same basic rules. However, each character on the board takes on a classic D&D class, and uses her powers to thwart her enemies.

* * *

## Contents
{% for page in site.pages %}
  {% if page.category == 'dungeonopoly1' %}  
* [{{ page.title }}](#{{ page.url }})
  {% endif %}
  {% if page.category == 'dungeonopoly2' %}  
    * [{{ page.title }}](#{{ page.url }})
  {% endif %}
{% endfor %}

{% for page in site.pages %}
  {% if page.category == 'dungeonopoly1' %}  
<a name="{{ page.url }}"></a>
* * *
## {{ page.title }}
{{ page.content }}
  {% endif %}
  {% if page.category == 'dungeonopoly2' %}  
<a name="{{ page.url }}"></a>
* * *
### {{ page.title }}
{{ page.content }}
  {% endif %}
{% endfor %}
