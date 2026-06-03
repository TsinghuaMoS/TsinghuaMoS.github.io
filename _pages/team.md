---
title: "MoS Lab - Team"
layout: gridlay
excerpt: "MoS Lab: Team members"
sitemap: false
permalink: /team/
---

{::nomarkdown}
<section class="pub-page-head">
  <p class="eyebrow">People</p>
  <h1>Team</h1>
  <p>MoS Lab strives to build a warm, inclusive, and supportive team grounded in collaboration, mutual respect, and innovation.</p>
</section>

{% assign groups = "0,7,1,2,3,4,8" | split: "," %}
{% assign group_names = "Principal Investigator,Researchers,PhD Students,MSc Students,Undergraduate Students,Interns,Alumni" | split: "," %}

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
    <article class="team-card">
      <a class="team-photo" href="{{ member.url }}">
        <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" alt="{{ member.name }}">
      </a>
      <div class="team-card-body">
        <h3><a href="{{ member.url }}">{{ member.name }}</a></h3>
        <p>{{ member.info }}</p>
        {% if member.affiliation %}<p class="team-affil">{{ member.affiliation }}</p>{% endif %}
      </div>
      {% if member.cv_en != nil and member.cv_en != "" or member.cv_cn != nil and member.cv_cn != "" %}
      <p class="team-cv">
        {% if member.cv_en and member.cv_en != "" %}<a href="{{ member.cv_en | relative_url }}" target="_blank" rel="noopener" title="View CV (English)"><i class="fa fa-file-pdf"></i> CV (EN)</a>{% endif %}
        {% if member.cv_cn and member.cv_cn != "" %}<a href="{{ member.cv_cn | relative_url }}" target="_blank" rel="noopener" title="查看简历（中文）"><i class="fa fa-file-pdf"></i> CV (中文)</a>{% endif %}
      </p>
      {% endif %}
    </article>
  {% endif %}
  {% endfor %}
  </div>
  {% else %}
  <p class="team-empty">We are recruiting. See the <a href="{{ '/contact/' | relative_url }}">Join Us</a> section.</p>
  {% endif %}
</section>
{% endfor %}
{:/nomarkdown}
