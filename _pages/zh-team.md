---
title: "团队 — 清华大学 MoS Lab"
layout: gridlay
excerpt: "MoS Lab 团队成员。"
sitemap: true
lang: zh
hreflang: true
alt_en: "/en/team/"
alt_zh: "/team/"
permalink: /team/
---

{::nomarkdown}
<section class="pub-page-head">
  <p class="eyebrow">团队</p>
  <h1>团队成员</h1>
  <p>MoS Lab 希望建立一个温暖、包容、互助的团队，以协作、相互尊重与创新为根基。</p>
</section>

{% assign groups = "0,7,1,2,3,4,8" | split: "," %}
{% assign group_names = "实验室负责人,研究人员,博士生,硕士生,本科生,实习生,毕业成员" | split: "," %}

{% for g in groups %}
{% assign gid = g | plus: 0 %}
{% assign has_members = false %}
{% for member in site.data.team_members %}{% if member.group == gid %}{% assign has_members = true %}{% endif %}{% endfor %}
<section class="team-section">
  <h2 class="pub-section-title">{{ group_names[forloop.index0] }}</h2>
  {% if has_members %}
  <div class="team-grid">
  {% for member in site.data.team_members %}
  {% if member.group == gid %}
  {% case member.info %}{% when 'Assistant Professor' %}{% assign role_zh = '助理教授' %}{% when 'Research Affiliate' %}{% assign role_zh = '合作研究员' %}{% when 'MSc Student' %}{% assign role_zh = '硕士生' %}{% when 'Intern' %}{% assign role_zh = '实习生' %}{% else %}{% assign role_zh = member.info %}{% endcase %}
  {% if member.group == 0 %}{% assign mlink = '/team/baichuan_mo/' | relative_url %}{% elsif member.name == 'Yahui Li' %}{% assign mlink = '/team/yahui_li/' | relative_url %}{% else %}{% assign mlink = member.url %}{% endif %}
    <article class="team-card">
      {% if mlink and mlink != "" %}
      <a class="team-photo" href="{{ mlink }}">
        <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }}">
      </a>
      {% else %}
      <span class="team-photo">
        <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }}">
      </span>
      {% endif %}
      <div class="team-card-body">
        {% assign display_name = member.name_zh | default: member.name %}
        <h3>{% if mlink and mlink != "" %}<a href="{{ mlink }}">{{ display_name }}</a>{% else %}{{ display_name }}{% endif %}</h3>
        <p>{{ role_zh }}</p>
        {% if member.affiliation %}<p class="team-affil">{{ member.affiliation }}</p>{% endif %}
        {% if member.cv_en != nil and member.cv_en != "" or member.cv_cn != nil and member.cv_cn != "" %}
        <p class="team-cv">
          {% if member.cv_en and member.cv_en != "" %}<a href="{{ member.cv_en | relative_url }}" target="_blank" rel="noopener" title="查看英文简历"><i class="fa fa-file-pdf"></i> CV (EN)</a>{% endif %}
          {% if member.cv_cn and member.cv_cn != "" %}<a href="{{ member.cv_cn | relative_url }}" target="_blank" rel="noopener" title="查看中文简历"><i class="fa fa-file-pdf"></i> CV (中文)</a>{% endif %}
        </p>
        {% endif %}
      </div>
    </article>
  {% endif %}
  {% endfor %}
  </div>
  {% else %}
  <p class="team-empty">招生中，详见 <a href="{{ '/admission/' | relative_url }}">2027 级招生</a>。</p>
  {% endif %}
</section>
{% endfor %}
{:/nomarkdown}
