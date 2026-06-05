---
title: "MoS Lab - Research"
layout: gridlay
excerpt: "MoS Lab -- Research"
sitemap: true
permalink: /research/
hreflang: true
alt_en: "/research/"
alt_zh: "/zh/research/"
---

{::nomarkdown}
<section class="pub-page-head research-head">
  <p class="eyebrow">Research</p>
  <h1>Models and algorithms for adaptive mobility systems.</h1>
  <p>The Tsinghua Mobility Science (MoS) Lab studies how people, infrastructure, and policy interact across transportation systems, especially under uncertainty, disruption, and rapid urban change.</p>
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
{:/nomarkdown}
