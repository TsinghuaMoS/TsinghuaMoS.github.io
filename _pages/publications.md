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

<!-- Journal Articles: cards grouped by year, with jump-nav and collapsible year groups -->
<section class="publication-list">
  <h2 class="pub-section-title">Journal Articles</h2>

  <nav class="pub-year-nav" aria-label="Jump to year">
    <span class="pub-year-nav-label">Jump to:</span>
{% for year in years %}
{% assign date = year | plus: 0 %}
{% assign containsJournal = false %}
{% for publi in site.data.publist %}
{% if publi.year == date and publi.type == 2 %}{% assign containsJournal = true %}{% endif %}
{% endfor %}
{% if containsJournal %}<a href="#journal-{{ year }}">{{ year }}</a>{% endif %}
{% endfor %}
  </nav>

{% for year in years %}
{% assign date = year | plus: 0 %}
{% assign containsJournal = false %}
{% for publi in site.data.publist %}
{% if publi.year == date and publi.type == 2 %}{% assign containsJournal = true %}{% endif %}
{% endfor %}
{% if containsJournal %}
  <div class="pub-year-group" id="journal-{{ year }}">
    <button type="button" class="pub-year pub-year-toggle" aria-expanded="true">
      <span class="pub-year-caret" aria-hidden="true">▾</span>{{ year }}
    </button>
    <div class="pub-year-body">
  {% for publi in site.data.publist %}
  {% if publi.year == date and publi.type == 2 %}
  {% include publication_card.html pub=publi %}
  {% endif %}
  {% endfor %}
    </div>
  </div>
{% endif %}
{% endfor %}
</section>

<!-- Conference Papers: plain stacked list (no boxes), grouped by year -->
<section class="publication-list">
  <h2 class="pub-section-title">Conference Papers</h2>
  <div class="pub-line-list">
{% for year in years %}
{% assign date = year | plus: 0 %}
{% assign containsConference = false %}
{% for publi in site.data.publist %}
{% if publi.year == date and publi.type == 1 %}{% assign containsConference = true %}{% endif %}
{% endfor %}
{% if containsConference %}
  <h3 class="pub-year-plain">{{ year }}</h3>
  {% for publi in site.data.publist %}
  {% if publi.year == date and publi.type == 1 %}
  {% include publication_line.html pub=publi %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
  </div>
</section>

<!-- Preprints and Working Papers: plain stacked list (no boxes), no year headings -->
<section class="publication-list">
  <h2 class="pub-section-title">Preprints and Working Papers</h2>
  <div class="pub-line-list">
{% for publi in site.data.publist %}
{% if publi.type == 4 %}
  {% include publication_line.html pub=publi %}
{% endif %}
{% endfor %}
  </div>
</section>

<script>
(function () {
  document.querySelectorAll('.pub-year-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var group = btn.closest('.pub-year-group');
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
      group.classList.toggle('is-collapsed', expanded);
    });
  });
})();
</script>
{:/nomarkdown}
