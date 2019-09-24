---
title: Publications
<!-- subtitle: all the papers the Larremore Lab has made -->
featured_image: /images/demo/demo-landscape.jpg
---
<ol>
{% for paper in site.data.papers %}
  <li>{{paper.title}}.
  <!-- <ul class="publication_details"> -->
  <!-- <li> -->
  <br>
  {% for author in paper.authors %}
  	{% if forloop.last %}
    	{{author}}.
	{% else %}
  		{{author}},
	{% endif %}
  {% endfor %}
  {{paper.venue}}, 
  {% if paper.volumeissue %}
    {{paper.volumeissue}},
  {% endif %}
  ({{paper.year}}).
  <br>
  <!-- </li> -->
  <!-- <li> -->
  {% for link in paper.links %}
  [<a href="{{link.url}}">{{link.text}}</a>] 
  {% endfor %}
  <br><br>
  <!-- </li> -->
  <!-- </ul> -->
{% endfor %}
