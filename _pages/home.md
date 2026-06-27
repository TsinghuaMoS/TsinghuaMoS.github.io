---
title: "MoS Lab — Mobility Science Lab at Tsinghua University"
layout: homelay
excerpt: "Mobility Science (MoS) Lab at Tsinghua University — resilient, intelligent, and sustainable transportation systems. 清华大学交通科学实验室。"
sitemap: true
hreflang: true
permalink: /en/
alt_en: "/en/"
alt_zh: "/"
---

{% assign journal_count = site.data.publist | where: "type", 2 | size %}

{::nomarkdown}
<a class="notice-banner" href="{{ '/admission/' | relative_url }}">📢 We're hiring! MoS Lab 2027 级招生进行中 —— 查看招生信息 →</a>

<section class="lab-hero">
  <img class="lab-hero-bg" src="{{ '/images/hero/urban_network.jpg' | relative_url }}" alt="">
  <div class="lab-hero-copy">
    <p class="eyebrow">MoS Lab</p>
    <h1>Mobility Science Lab at Tsinghua University</h1>
    <p class="hero-lede">MoS Lab studies how optimization theory and machine learning can support transportation systems, with research in system resilience, AI for Transportation, travel behavior and demand modeling, and sustainable urban systems.</p>
    <div class="hero-actions">
      <a class="hero-button primary" href="{{ '/en/research/' | relative_url }}">Explore Research</a>
      <a class="hero-button" href="{{ '/en/publications/' | relative_url }}">View Publications</a>
      <a class="hero-button" href="{{ '/en/contact/' | relative_url }}">Join Us</a>
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
      <a class="text-link" href="{{ flink }}">Read paper</a>
    </div>
  </article>
{% assign featured_count = featured_count | plus: 1 %}
{% endif %}
{% endfor %}
</div>

<section class="home-band">
  <div>
    <p class="eyebrow">Research Areas</p>
    <h2>Mobility science for systems that can adapt.</h2>
  </div>
  <div class="area-list">
    <p><strong>Transportation system resilience</strong> When incidents disrupt transportation systems, we develop efficient optimization and machine learning algorithms to adjust operations, guide passengers, and help systems recover quickly.</p>
    <p><strong>AI for Transportation:</strong> We study real-time decision-making with reinforcement learning, time-series foundation models, and transportation management agents across public transit, shared mobility, and supply-chain logistics.</p>
    <p><strong>Travel behavior and demand modeling</strong> We combine policy analysis, surveys, econometric models, machine learning, and optimization to improve traditional behavioral and demand models.</p>
    <p><strong>Sustainable urban systems</strong> We study commuting carbon emissions, public health risk, housing mobility, and urban cyber-physical-social system resilience for top interdisciplinary venues.</p>
  </div>
</section>

<section class="support-note">
  <p class="eyebrow">Research Support</p>
  <div class="funding-logos">
    <a href="https://www.nsfc.gov.cn/" target="_blank" rel="noopener" title="National Natural Science Foundation of China"><img src="{{ '/images/funding/nsfc.png' | relative_url }}" alt="National Natural Science Foundation of China"></a>
    <a href="https://www.bytedance.com/" target="_blank" rel="noopener" title="ByteDance"><img src="{{ '/images/funding/bytedance.png' | relative_url }}" alt="ByteDance"></a>
  </div>
</section>

<section class="support-note">
  <p class="eyebrow">Collaborating Institutions</p>
  <div class="partner-logos">
    <a href="https://www.mit.edu/" target="_blank" rel="noopener" title="Massachusetts Institute of Technology"><img src="{{ '/images/partners/mit.png' | relative_url }}" alt="Massachusetts Institute of Technology"></a>
    <a href="https://www.northeastern.edu/" target="_blank" rel="noopener" title="Northeastern University"><img src="{{ '/images/partners/northeastern.png' | relative_url }}" alt="Northeastern University"></a>
    <a href="https://www.berkeley.edu/" target="_blank" rel="noopener" title="University of California, Berkeley"><img src="{{ '/images/partners/uc_berkeley.png' | relative_url }}" alt="UC Berkeley"></a>
    <a href="https://www.hku.hk/" target="_blank" rel="noopener" title="The University of Hong Kong"><img src="{{ '/images/partners/hku.png' | relative_url }}" alt="The University of Hong Kong"></a>
    <a href="https://www.pku.edu.cn/" target="_blank" rel="noopener" title="Peking University"><img src="{{ '/images/partners/pku.png' | relative_url }}" alt="Peking University"></a>
    <a href="https://www.tongji.edu.cn/" target="_blank" rel="noopener" title="Tongji University"><img src="{{ '/images/partners/tongji.png' | relative_url }}" alt="Tongji University"></a>
    <a href="https://www.kth.se/" target="_blank" rel="noopener" title="KTH Royal Institute of Technology"><img src="{{ '/images/partners/kth.png' | relative_url }}" alt="KTH Royal Institute of Technology"></a>
    <a href="https://www.zju.edu.cn/" target="_blank" rel="noopener" title="Zhejiang University"><img src="{{ '/images/partners/zhejiang.png' | relative_url }}" alt="Zhejiang University"></a>
    <a href="https://nus.edu.sg/" target="_blank" rel="noopener" title="National University of Singapore"><img src="{{ '/images/partners/nus.png' | relative_url }}" alt="National University of Singapore"></a>
    <a href="https://www.cnu.edu.cn/" target="_blank" rel="noopener" title="Capital Normal University"><img src="{{ '/images/partners/cnu.png' | relative_url }}" alt="Capital Normal University"></a>
  </div>
</section>
{:/nomarkdown}
