---
title: "MoS Lab - Home"
layout: homelay
excerpt: "MoS Lab"
sitemap: false
permalink: /
---

{% assign journal_count = site.data.publist | where: "type", 2 | size %}

{::nomarkdown}
<section class="lab-hero">
  <img class="lab-hero-bg" src="{{ '/images/hero/urban_network.jpg' | relative_url }}" alt="">
  <div class="lab-hero-copy">
    <p class="eyebrow">MoS Lab</p>
    <h1>Mobility Science Lab at Tsinghua University</h1>
    <p class="hero-lede">MoS Lab develops models, algorithms, and data-driven tools for public transit operations, passenger behavior, mobility demand, urban resilience, and sustainable transportation policy.</p>
    <div class="hero-actions">
      <a class="hero-button primary" href="{{ '/research/' | relative_url }}">Explore Research</a>
      <a class="hero-button" href="{{ '/research/' | relative_url }}">View Publications</a>
    </div>
  </div>
</section>

<section class="metric-strip" aria-label="MoS Lab highlights">
  <div class="metric-item">
    <strong>{{ site.data.publist.size }}</strong>
    <span>publications and working papers</span>
  </div>
  <div class="metric-item">
    <strong>{{ journal_count }}</strong>
    <span>journal articles</span>
  </div>
  <div class="metric-item">
    <strong>4</strong>
    <span>research directions</span>
  </div>
</section>

<section class="section-heading">
  <p class="eyebrow">Featured Research</p>
  <h2>From passenger-level behavior to city-scale resilience.</h2>
</section>

<div class="featured-grid">
{% for item in site.data.featured_research %}
  <article class="feature-card">
    <a class="feature-image" href="{{ item.paper_url | relative_url }}">
      <img src="{{ item.image | relative_url }}" alt="{{ item.alt }}">
    </a>
    <div class="feature-body">
      <span>{{ item.theme }}</span>
      <h3>{{ item.title }}</h3>
      <p>{{ item.description }}</p>
      <a class="text-link" href="{{ item.paper_url | relative_url }}">Read paper</a>
    </div>
  </article>
{% endfor %}
</div>

<section class="home-band">
  <div>
    <p class="eyebrow">Research Areas</p>
    <h2>Mobility science for systems that can adapt.</h2>
  </div>
  <div class="area-list">
    <p><strong>Public transit resilience</strong> Disruption management, passenger response inference, path recommendation, and resilient operations.</p>
    <p><strong>Travel behavior and demand</strong> Route choice, mode choice, smart card analytics, and policy response modeling.</p>
    <p><strong>AI for mobility and logistics</strong> Robust learning, interpretable prediction, ETA, last-mile delivery, and time-series models.</p>
    <p><strong>Sustainable urban systems</strong> Commuting emissions, public health risk, housing mobility, and cyber-physical-social resilience.</p>
  </div>
</section>

<section class="support-note">
  <p class="eyebrow">Research Support</p>
  <div class="funding-logos">
    <img src="{{ '/images/funding/nsfc.png' | relative_url }}" alt="National Natural Science Foundation of China">
    <img src="{{ '/images/funding/bytedance.png' | relative_url }}" alt="ByteDance">
  </div>
</section>
{:/nomarkdown}
