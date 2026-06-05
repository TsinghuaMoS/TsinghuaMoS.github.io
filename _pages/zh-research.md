---
title: "研究 — 清华大学 MoS Lab"
layout: gridlay
excerpt: "MoS Lab 研究方向：公共交通韧性、出行行为与需求、交通智能、可持续城市系统。"
sitemap: true
lang: zh
hreflang: true
alt_en: "/research/"
alt_zh: "/zh/research/"
permalink: /zh/research/
---

{::nomarkdown}
<section class="pub-page-head research-head">
  <p class="eyebrow">研究</p>
  <h1>面向自适应交通系统的模型与算法。</h1>
  <p>清华大学出行科学（MoS）实验室研究人、基础设施与政策如何在交通系统中相互作用，尤其关注不确定性、突发中断与快速城市化下的系统行为。</p>
</section>

<h2 class="pub-section-title">代表性研究</h2>
<div class="featured-grid research-featured">
{% assign featured_count = 0 %}
{% assign sorted_pubs = site.data.publist | sort: "year" | reverse %}
{% for item in sorted_pubs %}
{% if item.featured and item.feature_image and item.feature_image != "" and featured_count < 4 %}
{% if item.pdf_url and item.pdf_url != "" %}{% assign flink = item.pdf_url | relative_url %}{% else %}{% assign flink = item.external_url %}{% endif %}
{% case item.category %}{% when 'Public Transit Resilience' %}{% assign cat_zh = '公共交通韧性' %}{% when 'Travel Behavior & Demand' %}{% assign cat_zh = '出行行为与需求' %}{% when 'Mobility AI' %}{% assign cat_zh = '交通智能' %}{% when 'Sustainable Urban Systems' %}{% assign cat_zh = '可持续城市系统' %}{% else %}{% assign cat_zh = item.category %}{% endcase %}
  <article class="feature-card">
    <a class="feature-image" href="{{ flink }}">
      <img src="{{ item.feature_image | relative_url }}" alt="{{ item.feature_alt | default: item.title }}">
    </a>
    <div class="feature-body">
      <span>{{ cat_zh }}</span>
      <h3>{{ item.feature_title_zh | default: item.feature_title | default: item.title }}</h3>
      <p>{{ item.feature_description_zh | default: item.feature_description }}</p>
    </div>
  </article>
{% assign featured_count = featured_count | plus: 1 %}
{% endif %}
{% endfor %}
</div>

<h2 class="pub-section-title">研究方向</h2>
<section class="research-pillars">
  <article>
    <span>01</span>
    <h2>公共交通韧性</h2>
    <p>研究交通系统与乘客如何应对计划内与计划外的中断，包括事故感知的乘客行为推断、鲁棒路径推荐、网络性能建模，以及降低拥堵、提升服务可靠性的控制策略。</p>
  </article>
  <article>
    <span>02</span>
    <h2>出行行为与需求建模</h2>
    <p>利用刷卡数据、车牌识别数据、问卷与运营数据，构建可解释、可预测的出行行为模型；研究路径选择、方式选择、个体出行预测，以及公共交通与新兴出行方式之间的相互作用。</p>
  </article>
  <article>
    <span>03</span>
    <h2>交通智能（AI for Transportation）</h2>
    <p>将机器学习、深度学习、鲁棒优化与决策模型应用于交通问题，如到达时间估计、末端配送路径预测、时序预测大模型，以及数据不确定性下的分类问题。</p>
  </article>
  <article>
    <span>04</span>
    <h2>可持续城市系统</h2>
    <p>将交通置于更广义的城市信息物理社会系统中研究，应用包括通勤碳排放、极端天气韧性、通勤中的公共健康风险、住房流动性与政策评估。</p>
  </article>
</section>
{:/nomarkdown}
