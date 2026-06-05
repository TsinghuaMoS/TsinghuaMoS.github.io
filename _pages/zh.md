---
title: "清华大学 MoS Lab｜出行科学与交通智能实验室"
layout: homelay
excerpt: "清华大学交通工程系 MoS Lab（出行科学实验室），由助理教授莫佰川负责，研究城市交通、公共交通韧性、出行行为与需求、交通机器学习与优化。"
sitemap: true
lang: zh
hreflang: true
alt_en: "/"
alt_zh: "/zh/"
permalink: /zh/
---

{% assign journal_count = site.data.publist | where: "type", 2 | size %}

{::nomarkdown}
<a class="notice-banner" href="{{ '/admission/' | relative_url }}">📢 实验室正在招生！MoS Lab 2027 级招生进行中 —— 查看招生信息 →</a>

<section class="lab-hero">
  <img class="lab-hero-bg" src="{{ '/images/hero/urban_network.jpg' | relative_url }}" alt="">
  <div class="lab-hero-copy">
    <p class="eyebrow">清华大学 · MoS Lab</p>
    <h1>清华大学出行科学实验室</h1>
    <p class="hero-lede">MoS Lab 致力于为公共交通运营、乘客行为、出行需求、城市韧性与可持续交通政策，研发模型、算法与数据驱动的决策工具。</p>
    <div class="hero-actions">
      <a class="hero-button primary" href="{{ '/zh/research/' | relative_url }}">研究方向</a>
      <a class="hero-button" href="{{ '/zh/publications/' | relative_url }}">论文发表</a>
      <a class="hero-button" href="{{ '/admission/' | relative_url }}">加入我们</a>
    </div>
  </div>
</section>

<section class="metric-strip" aria-label="MoS Lab 概览">
  <div class="metric-item">
    <strong>{{ site.data.publist.size }}</strong>
    <span>论文与工作论文</span>
  </div>
  <div class="metric-item">
    <strong>{{ journal_count }}</strong>
    <span>期刊论文</span>
  </div>
  <div class="metric-item">
    <strong>4</strong>
    <span>研究方向</span>
  </div>
</section>

<section class="section-heading">
  <p class="eyebrow">代表性研究</p>
  <h2>从乘客行为到城市尺度的系统韧性。</h2>
</section>

<div class="featured-grid">
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
      <a class="text-link" href="{{ flink }}">查看论文</a>
    </div>
  </article>
{% assign featured_count = featured_count | plus: 1 %}
{% endif %}
{% endfor %}
</div>

<section class="home-band">
  <div>
    <p class="eyebrow">研究方向</p>
    <h2>面向能够自适应的交通系统的出行科学。</h2>
  </div>
  <div class="area-list">
    <p><strong>公共交通韧性</strong> 中断管理、乘客响应推断、路径推荐与韧性运营。</p>
    <p><strong>出行行为与需求</strong> 路径选择、方式选择、刷卡数据分析与政策响应建模。</p>
    <p><strong>交通智能（AI for Transportation）</strong> 鲁棒学习、可解释预测、到达时间估计、末端配送与时序模型。</p>
    <p><strong>可持续城市系统</strong> 通勤碳排放、公共健康风险、住房流动性与城市信息物理社会系统韧性。</p>
  </div>
</section>

<section class="support-note">
  <p class="eyebrow">科研支持</p>
  <div class="funding-logos">
    <a href="https://www.nsfc.gov.cn/" target="_blank" rel="noopener" title="国家自然科学基金委员会"><img src="{{ '/images/funding/nsfc.png' | relative_url }}" alt="国家自然科学基金委员会"></a>
    <a href="https://www.bytedance.com/" target="_blank" rel="noopener" title="字节跳动"><img src="{{ '/images/funding/bytedance.png' | relative_url }}" alt="字节跳动"></a>
  </div>
</section>

<section class="support-note">
  <p class="eyebrow">合作院校</p>
  <div class="partner-logos">
    <a href="https://www.mit.edu/" target="_blank" rel="noopener" title="麻省理工学院"><img src="{{ '/images/partners/mit.png' | relative_url }}" alt="麻省理工学院"></a>
    <a href="https://www.northeastern.edu/" target="_blank" rel="noopener" title="东北大学（美国）"><img src="{{ '/images/partners/northeastern.png' | relative_url }}" alt="Northeastern University"></a>
    <a href="https://www.berkeley.edu/" target="_blank" rel="noopener" title="加州大学伯克利分校"><img src="{{ '/images/partners/uc_berkeley.png' | relative_url }}" alt="UC Berkeley"></a>
    <a href="https://www.hku.hk/" target="_blank" rel="noopener" title="香港大学"><img src="{{ '/images/partners/hku.png' | relative_url }}" alt="The University of Hong Kong"></a>
    <a href="https://www.pku.edu.cn/" target="_blank" rel="noopener" title="北京大学"><img src="{{ '/images/partners/pku.png' | relative_url }}" alt="Peking University"></a>
    <a href="https://www.tongji.edu.cn/" target="_blank" rel="noopener" title="同济大学"><img src="{{ '/images/partners/tongji.png' | relative_url }}" alt="Tongji University"></a>
    <a href="https://www.kth.se/" target="_blank" rel="noopener" title="瑞典皇家理工学院（KTH）"><img src="{{ '/images/partners/kth.png' | relative_url }}" alt="KTH Royal Institute of Technology"></a>
    <a href="https://www.zju.edu.cn/" target="_blank" rel="noopener" title="浙江大学"><img src="{{ '/images/partners/zhejiang.png' | relative_url }}" alt="Zhejiang University"></a>
    <a href="https://nus.edu.sg/" target="_blank" rel="noopener" title="新加坡国立大学"><img src="{{ '/images/partners/nus.png' | relative_url }}" alt="National University of Singapore"></a>
    <a href="https://www.cnu.edu.cn/" target="_blank" rel="noopener" title="首都师范大学"><img src="{{ '/images/partners/cnu.png' | relative_url }}" alt="Capital Normal University"></a>
  </div>
</section>
{:/nomarkdown}
