---
title: "研究 — 清华大学 MoS Lab"
layout: gridlay
excerpt: "MoS Lab 研究方向：交通系统韧性、AI for Transportation、出行行为与需求建模、可持续城市系统。"
sitemap: true
lang: zh
hreflang: true
alt_en: "/en/research/"
alt_zh: "/research/"
permalink: /research/
---

{::nomarkdown}
<section class="pub-page-head research-head">
  <p class="eyebrow">研究</p>
  <h1>优化理论与机器学习驱动的交通系统研究。</h1>
  <p>MoS Lab 关注模型、算法与数据如何帮助交通系统在不确定性、突发事故和快速城市化环境下更高效、更智能、更可持续地运行。</p>
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
    <h2>交通系统韧性</h2>
    <p>在交通系统发生事故时，研究如何通过高效的优化与机器学习算法，调整运营、指导乘客，让系统快速恢复。具体包括事故感知的乘客行为推断、鲁棒路径推荐、网络性能建模与韧性运营控制。</p>
  </article>
  <article>
    <span>02</span>
    <h2>AI for Transportation</h2>
    <p>将人工智能应用于公共交通、共享出行、供应链物流等多个场景，包括基于强化学习的实时决策、时序预测大模型、交通管理 Agent、ETA 预测与末端配送路径预测等。</p>
  </article>
  <article>
    <span>03</span>
    <h2>出行行为与需求建模</h2>
    <p>围绕政策分析与问卷调研、计量经济学模型应用、刷卡与车牌识别等多源数据分析，研究如何用现代机器学习与优化理论改良传统计量经济学模型。</p>
  </article>
  <article>
    <span>04</span>
    <h2>可持续城市系统</h2>
    <p>研究通勤碳排放、公共健康风险、住房流动性与城市信息物理社会系统韧性，并将交通系统放在更广义的城市可持续发展和跨学科政策评估框架中理解。</p>
  </article>
</section>
{:/nomarkdown}
