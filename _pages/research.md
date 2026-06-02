---
title: "MoS Lab - Research"
layout: textlay
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
    <h2>Travel Behavior and Demand Modeling</h2>
    <p>We build interpretable and predictive models of mobility behavior using smart card data, license plate recognition data, surveys, and operational data. Topics include route choice, mode choice, individual mobility prediction, and the interactions between public transit and emerging mobility services.</p>
  </article>
  <article>
    <span>03</span>
    <h2>AI for Mobility and Logistics</h2>
    <p>We apply machine learning, deep learning, robust optimization, and decision models to transportation problems such as estimated time of arrival, last-mile delivery route prediction, time-series forecasting, and classification under data uncertainty.</p>
  </article>
  <article>
    <span>04</span>
    <h2>Sustainable and Resilient Urban Systems</h2>
    <p>We analyze transportation as part of broader cyber-physical-social urban systems, with applications in commuting emissions, extreme weather resilience, public health risk during commuting, housing mobility, and policy evaluation.</p>
  </article>
</section>
{:/nomarkdown}
