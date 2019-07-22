---
title: People
---

## PI

<section class="portfolio">
	<div class="content-wrap portfolio-wrap">
    <div class="portfolio-item">
      <a class="portfolio-item__link" href="http://danlarremore.com">
        <div class="portfolio-item__image">
          <img style="margin: 0 auto; max-width: 367px; max-height: 367px;" src="{{ site.data.people.dan.pic }}" alt="{{ site.data.people.dan.name }}">
        </div>
				<div class="portfolio-item__content">
					<div class="portfolio-item__info">
						<h2 class="portfolio-item__title">{{ site.data.people.dan.name }}</h2>
					</div>
				</div>
      </a>
    </div>
  </div>
</section>

## PhD Students

<section class="portfolio">
	<div class="content-wrap portfolio-wrap">
		{% for person in site.data.people.phd_students %}
		<div class="portfolio-item">
      {% if person.url %}
			<a class="portfolio-item__link" href="{{ person.url }}">
      {% else %}
			<a class="portfolio-item__link" href=".">
      {% endif %}
				<div class="portfolio-item__image">
					<img style="margin: 0 auto; max-width: 367px; max-height: 367px;" src="{{ person.pic  }}" alt="{{ person.name }}">
				</div>

				<div class="portfolio-item__content">
					<div class="portfolio-item__info">
						<h2 class="portfolio-item__title">{{ person.name }}</h2>
					</div>
				</div>
			</a>

		</div>
		{% endfor %}
	</div>
</section>

## Undergraduates

<section class="portfolio">
	<div class="content-wrap portfolio-wrap">
		{% for person in site.data.people.undergraduate_students %}
		<div class="portfolio-item">
      {% if person.url %}
			<a class="portfolio-item__link" href="{{ person.url }}">
      {% else %}
			<a class="portfolio-item__link" href=".">
      {% endif %}
				<div class="portfolio-item__image">
					<img style="margin: 0 auto; max-width: 367px; max-height: 367px;" src="{{ person.pic  }}" alt="{{ person.name }}">
				</div>

				<div class="portfolio-item__content">
					<div class="portfolio-item__info">
						<h2 class="portfolio-item__title">{{ person.name }}</h2>
					</div>
				</div>
			</a>
      hunter!

		</div>
		{% endfor %}
	</div>
</section>
