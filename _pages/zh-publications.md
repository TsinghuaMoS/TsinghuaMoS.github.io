---
title: "论文 — 清华大学 MoS Lab"
layout: gridlay
excerpt: "MoS Lab 论文发表列表。"
sitemap: true
lang: zh
hreflang: true
alt_en: "/publications/"
alt_zh: "/zh/publications/"
permalink: /zh/publications/
---

{::nomarkdown}
<section class="pub-page-head">
  <p class="eyebrow">论文</p>
  <h1>MoS Lab 及合作者的代表性工作。</h1>
  <p>研究涵盖公共交通韧性、出行行为、交通智能与可持续城市系统。</p>
  <div class="pub-legend">
    <span><sup class="author-corresponding">*</sup> 通讯作者</span>
    <span><sup class="author-equal">&dagger;</sup> 同等贡献</span>
  </div>
</section>

<section class="full-list-note">
  <p>最新论文列表请见 <a href="https://scholar.google.com/citations?user=ORhrfXoAAAAJ&hl=en"><strong><i class="ai ai-google-scholar"></i> Google Scholar</strong></a>。</p>
</section>

{% assign years = "2026,2025,2024,2023,2022,2021,2020,2019,2018,2017" | split: "," %}

<!-- 期刊论文 -->
{% assign journal_total = site.data.publist | where: "type", 2 | size %}
{% assign jnum = journal_total %}
<section class="publication-list">
  <h2 class="pub-section-title">期刊论文</h2>

  <nav class="pub-year-nav" aria-label="按年份跳转">
    <span class="pub-year-nav-label">跳转：</span>
    <button type="button" class="pub-year-nav-section pub-featured-toggle" id="featured-toggle" aria-pressed="false">★ 仅看代表作</button>
{% for year in years %}
{% assign date = year | plus: 0 %}
{% assign containsJournal = false %}
{% for publi in site.data.publist %}
{% if publi.year == date and publi.type == 2 %}{% assign containsJournal = true %}{% endif %}
{% endfor %}
{% if containsJournal %}<a href="#journal-{{ year }}">{{ year }}</a>{% endif %}
{% endfor %}
    <a class="pub-year-nav-section" href="#conference">会议论文 ↓</a>
    <a class="pub-year-nav-section" href="#working">预印本与工作论文 ↓</a>
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
  {% include publication_card.html pub=publi num=jnum %}
  {% assign jnum = jnum | minus: 1 %}
  {% endif %}
  {% endfor %}
    </div>
  </div>
{% endif %}
{% endfor %}
</section>

<!-- 会议论文 -->
<section class="publication-list" id="conference">
  <h2 class="pub-section-title">会议论文</h2>
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

<!-- 预印本与工作论文 -->
<section class="publication-list" id="working">
  <h2 class="pub-section-title">预印本与工作论文</h2>
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

  var toggle = document.getElementById('featured-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var on = !document.body.classList.contains('show-featured-only');
      document.body.classList.toggle('show-featured-only', on);
      toggle.setAttribute('aria-pressed', String(on));
      toggle.textContent = on ? '★ 正在显示代表作 ✕' : '★ 仅看代表作';
      document.querySelectorAll('.pub-card').forEach(function (c) {
        c.style.display = (on && !c.classList.contains('pub-card-featured')) ? 'none' : '';
      });
      document.querySelectorAll('.pub-year-group').forEach(function (group) {
        var hasFeatured = group.querySelector('.pub-card-featured');
        group.style.display = (on && !hasFeatured) ? 'none' : '';
        if (on && hasFeatured) group.classList.remove('is-collapsed');
      });
      ['conference', 'working'].forEach(function (id) {
        var s = document.getElementById(id);
        if (s) s.style.display = on ? 'none' : '';
      });
    });
  }
})();
</script>
{:/nomarkdown}
