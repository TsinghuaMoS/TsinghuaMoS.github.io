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
  <p>Click a name to view a member profile.</p>
</section>

{% assign groups = "0,7,1,2,3,4,8" | split: "," %}
{% assign group_names = "Principal Investigator,Researchers,PhD Students,MSc Students,Undergraduate Students,Interns,Alumni" | split: "," %}

{% for g in groups %}
{% assign gid = g | plus: 0 %}
{% assign has_members = false %}
{% for member in site.data.team_members %}{% if member.group == gid %}{% assign has_members = true %}{% endif %}{% endfor %}
{% if has_members %}
<section class="team-section">
  <h2 class="pub-section-title">{{ group_names[forloop.index0] }}</h2>
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
      </div>
    </article>
  {% endif %}
  {% endfor %}
  </div>
</section>
{% endif %}
{% endfor %}
{:/nomarkdown}
