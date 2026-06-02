---
title: "MoS Lab - Publications"
layout: gridlay
excerpt: "MoS Lab -- Publications."
sitemap: false
permalink: /publications/
---

{::nomarkdown}
<section class="pub-page-head">
  <p class="eyebrow">Publications</p>
  <h1>Selected work from MoS Lab and collaborators.</h1>
  <p>Research spanning public transit resilience, travel behavior, robust learning, mobility AI, and sustainable urban systems.</p>
  <div class="pub-legend">
    <span><strong>Baichuan Mo</strong> highlighted in author lists</span>
    <span><sup class="author-corresponding">*</sup> Corresponding author</span>
    <span><sup class="author-equal">&dagger;</sup> Equal contribution</span>
  </div>
</section>

<section class="full-list-note">
  <p>For citation counts and the most current indexing, please visit <a class="regtext" href="https://scholar.google.com/citations?user=ORhrfXoAAAAJ&hl=en">Google Scholar</a>.</p>
</section>

<section class="section-heading compact">
  <p class="eyebrow">Featured Research</p>
  <h2>Representative themes</h2>
</section>

<div class="featured-grid compact">
{% for item in site.data.featured_research %}
  <article class="feature-card mini">
    <a class="feature-image" href="{{ item.paper_url | relative_url }}">
      <img src="{{ item.image | relative_url }}" alt="{{ item.alt }}">
    </a>
    <div class="feature-body">
      <span>{{ item.theme }}</span>
      <h3>{{ item.title }}</h3>
    </div>
  </article>
{% endfor %}
</div>

{% assign years = "2026,2025,2024,2023,2022,2021,2020,2019,2018,2017" | split: "," %}

<!-- Journal Articles first, grouped by year -->
<section class="publication-list">
  <h2 class="pub-section-title">Journal Articles</h2>
{% for year in years %}
{% assign date = year | plus: 0 %}
{% assign containsJournal = false %}
{% for publi in site.data.publist %}
{% if publi.year == date and publi.type == 2 %}
{% assign containsJournal = true %}
{% endif %}
{% endfor %}
{% if containsJournal %}
  <h3 class="pub-year">{{ year }}</h3>
  {% for publi in site.data.publist %}
  {% if publi.year == date and publi.type == 2 %}
  {% include publication_card.html pub=publi %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
</section>

<!-- Conference Papers and Working Papers grouped together at the back -->
<section class="publication-list">
  <h2 class="pub-section-title">Conference Papers</h2>
{% for year in years %}
{% assign date = year | plus: 0 %}
{% assign containsConference = false %}
{% for publi in site.data.publist %}
{% if publi.year == date and publi.type == 1 %}
{% assign containsConference = true %}
{% endif %}
{% endfor %}
{% if containsConference %}
  <h3 class="pub-year">{{ year }}</h3>
  {% for publi in site.data.publist %}
  {% if publi.year == date and publi.type == 1 %}
  {% include publication_card.html pub=publi %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
</section>

<section class="publication-list">
  <h2 class="pub-section-title">Preprints and Working Papers</h2>
{% for year in years %}
{% assign date = year | plus: 0 %}
{% assign containsWorking = false %}
{% for publi in site.data.publist %}
{% if publi.year == date and publi.type == 4 %}
{% assign containsWorking = true %}
{% endif %}
{% endfor %}
{% if containsWorking %}
  <h3 class="pub-year">{{ year }}</h3>
  {% for publi in site.data.publist %}
  {% if publi.year == date and publi.type == 4 %}
  {% include publication_card.html pub=publi %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
  {% for publi in site.data.publist %}
  {% if publi.type == 4 and publi.year == nil %}
  {% include publication_card.html pub=publi %}
  {% endif %}
  {% endfor %}
</section>
{:/nomarkdown}
