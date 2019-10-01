---
title: Slides
---

<section class="portfolio">
	<div class="content-wrap portfolio-wrap">
		{% for deck in site.data.slides.slides %}
		{% include slide_deck.html %}
		{% endfor %}
	</div>
</section>
