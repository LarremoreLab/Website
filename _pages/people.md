---
title: The Team
---

<section class="portfolio">
	<div class="content-wrap portfolio-wrap">
		{% for person in site.data.people.people %}
		<div class="portfolio-item">
      {% if person.url %}
			<a class="portfolio-item__link" href="{{ person.url }}">
      {% else %}
			<a class="portfolio-item__link" href=".">
      {% endif %}
				<div class="portfolio-item__image">
					<img style="margin: 0 auto; max-width: 250px; max-height: 250px;" src="{{ person.pic  }}" alt="{{ person.name }}">
				</div>
				<div class="portfolio-item__content">
					<div class="portfolio-item__info">
						<h2 class="portfolio-item__title">{{ person.name }}</h2>
					</div>
				</div>
			</a>{{person.name}}<br>{{person.title}}<br>{{person.subject}}
		</div>
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