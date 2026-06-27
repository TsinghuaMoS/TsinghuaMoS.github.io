---
title: "MoS Lab - Research"
layout: gridlay
excerpt: "MoS Lab -- Research"
sitemap: true
permalink: /en/research/
hreflang: true
alt_en: "/en/research/"
alt_zh: "/research/"
---

{::nomarkdown}
<section class="pub-page-head research-head">
  <p class="eyebrow">Research</p>
  <h1>Transportation research powered by optimization and machine learning.</h1>
  <p>MoS Lab studies how models, algorithms, and data can help transportation systems operate more efficiently, intelligently, and sustainably under uncertainty, disruption, and rapid urban change.</p>
</section>

<h2 class="pub-section-title">Featured Research</h2>
<div class="featured-grid research-featured">
{% assign featured_count = 0 %}
{% assign sorted_pubs = site.data.publist | sort: "year" | reverse %}
{% for item in sorted_pubs %}
{% if item.featured and item.feature_image and item.feature_image != "" and featured_count < 4 %}
{% if item.pdf_url and item.pdf_url != "" %}{% assign flink = item.pdf_url | relative_url %}{% else %}{% assign flink = item.external_url %}{% endif %}
  <article class="feature-card">
    <a class="feature-image" href="{{ flink }}">
      <img src="{{ item.feature_image | relative_url }}" alt="{{ item.feature_alt | default: item.title }}">
    </a>
    <div class="feature-body">
      <span>{{ item.category }}</span>
      <h3>{{ item.feature_title | default: item.title }}</h3>
      <p>{{ item.feature_description }}</p>
    </div>
  </article>
{% assign featured_count = featured_count | plus: 1 %}
{% endif %}
{% endfor %}
</div>

<h2 class="pub-section-title">Research Areas</h2>
<section class="research-pillars">
  <article>
    <span>01</span>
    <h2>Transportation System Resilience</h2>
    <p>When incidents disrupt transportation systems, we study how efficient optimization and machine learning algorithms can adjust operations, guide passengers, and help systems recover quickly. Topics include incident-aware passenger behavior inference, robust path recommendation, network performance modeling, and resilient operations control.</p>
  </article>
  <article>
    <span>02</span>
    <h2>AI for Transportation</h2>
    <p>We apply AI to public transit, shared mobility, and supply-chain logistics, including reinforcement-learning-based real-time decisions, time-series foundation models, transportation management agents, ETA prediction, and last-mile delivery route prediction.</p>
  </article>
  <article>
    <span>03</span>
    <h2>Travel Behavior &amp; Demand Modeling</h2>
    <p>We combine policy analysis, surveys, econometric models, smart card data, license plate recognition data, machine learning, and optimization to improve traditional behavioral and demand models.</p>
  </article>
  <article>
    <span>04</span>
    <h2>Sustainable Urban Systems</h2>
    <p>We study commuting carbon emissions, public health risk, housing mobility, and urban cyber-physical-social system resilience, placing transportation in broader sustainability and interdisciplinary policy-evaluation frameworks.</p>
  </article>
</section>
{:/nomarkdown}
