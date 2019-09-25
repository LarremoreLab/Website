---
title: The Team
---

<section class="portfolio">
	<div class="content-wrap portfolio-wrap">
		{% for person in site.data.people.people %}
      {% include person.html %}
		{% endfor %}
	</div>
</section>
<section>
	Alumni
	<ul>
	{% for person in site.data.people.alumni %}
		<li>{{person.name}}</li>
	{% endfor %}
	</ul>
</section>
