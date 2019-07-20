---
title: Publications
subtitle: all the papers the Larremore Lab has made
featured_image: /images/demo/demo-landscape.jpg
---

{% for paper in site.data.papers %}
  <p>{{paper.title}}</p>
  {% for link in paper.links %}
  <a href="{{link.url}}">{{link.text}}</a>
  {% endfor %}
{% endfor %}
