---
title: "MoS Lab - Research"
layout: gridlay
excerpt: "MoS Lab -- Research"
sitemap: false
permalink: /research/
---

{::nomarkdown}
<section class="pub-page-head research-head">
  <p class="eyebrow">Research</p>
  <h1>Models and algorithms for adaptive mobility systems.</h1>
  <p>The Tsinghua Mobility Science (MoS) Lab studies how people, infrastructure, and policy interact across transportation systems, especially under uncertainty, disruption, and rapid urban change.</p>
</section>

<div class="featured-grid research-featured">
{% for item in site.data.featured_research %}
  <article class="feature-card">
    <a class="feature-image" href="{{ item.paper_url | relative_url }}">
      <img src="{{ item.image | relative_url }}" alt="{{ item.alt }}">
    </a>
    <div class="feature-body">
      <span>{{ item.theme }}</span>
      <h3>{{ item.title }}</h3>
      <p>{{ item.description }}</p>
    </div>
  </article>
{% endfor %}
</div>

<section class="research-pillars">
  <article>
    <span>01</span>
    <h2>Public Transit Resilience</h2>
    <p>We study how transit systems and passengers respond to planned and unplanned disruptions. Our work includes incident-aware passenger behavior inference, robust path recommendation, network performance modeling, and control strategies that reduce congestion and improve service reliability.</p>
  </article>
  <article>
    <span>02</span>
    <h2>Travel Behavior &amp; Demand</h2>
    <p>We build interpretable and predictive models of mobility behavior using smart card data, license plate recognition data, surveys, and operational data. Topics include route choice, mode choice, individual mobility prediction, and the interactions between public transit and emerging mobility services.</p>
  </article>
  <article>
    <span>03</span>
    <h2>Mobility AI</h2>
    <p>We apply machine learning, deep learning, robust optimization, and decision models to transportation problems such as estimated time of arrival, last-mile delivery route prediction, time-series forecasting, and classification under data uncertainty.</p>
  </article>
  <article>
    <span>04</span>
    <h2>Sustainable Urban Systems</h2>
    <p>We analyze transportation as part of broader cyber-physical-social urban systems, with applications in commuting emissions, extreme weather resilience, public health risk during commuting, housing mobility, and policy evaluation.</p>
  </article>
</section>

<section class="section-heading">
  <p class="eyebrow">Publications</p>
  <h2>Selected work from MoS Lab and collaborators.</h2>
</section>
<div class="pub-legend">
  <span><sup class="author-corresponding">*</sup> Corresponding author</span>
  <span><sup class="author-equal">&dagger;</sup> Equal contribution</span>
</div>
<section class="full-list-note">
  <p>For citation counts and the most current indexing, please visit <a class="regtext" href="https://scholar.google.com/citations?user=ORhrfXoAAAAJ&hl=en">Google Scholar</a>.</p>
</section>

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
    <a class="pub-year-nav-section" href="#conference">Conference Papers ↓</a>
    <a class="pub-year-nav-section" href="#working">Preprints &amp; Working Papers ↓</a>
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
<section class="publication-list" id="conference">
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
<section class="publication-list" id="working">
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
