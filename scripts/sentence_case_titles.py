#!/usr/bin/env python3
"""
Rewrite all publication titles in _data/publist.yml to sentence case.

Rule: lowercase every word except the first word, the first word after a
colon, and proper nouns / acronyms. Run after adding/editing publications:
    python3 scripts/sentence_case_titles.py
"""
import os, re, sys
try:
    import yaml
except ImportError:
    sys.exit("pyyaml required")

# Proper nouns that must stay capitalized (single words the acronym test misses)
PROPER = {"singapore","beijing","nanning","china","markov","bayesian","nature","european"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIST = os.path.join(ROOT, "_data", "publist.yml")

def is_acronym(part):
    core = re.sub(r"[^A-Za-z0-9+]", "", part)
    if not core:
        return False
    if any(c.isdigit() for c in core):           # V2I, COVID-19
        return True
    if core.isupper() and len(core) >= 2:         # IEEE, SCOPE
        return True
    if any(c.isupper() for c in core[1:]):        # MoE, TimeMixer (internal caps)
        return True
    return False

def fix_part(part, force_cap):
    if is_acronym(part):
        return part
    if part.lower().strip("().,:;") in PROPER:
        return part[0].upper() + part[1:].lower() if part[:1].isalpha() else part
    low = part.lower()
    if force_cap:
        for i,ch in enumerate(low):
            if ch.isalpha():
                return low[:i] + ch.upper() + low[i+1:]
    return low

def fix_word(word, starts_clause):
    parts = word.split("-")
    out = []
    for j, p in enumerate(parts):
        out.append(fix_part(p, force_cap=(starts_clause and j == 0)))
    return "-".join(out)

def sentence_case(title):
    toks = title.split()
    res = []
    after_colon = True  # first word starts a clause
    for w in toks:
        res.append(fix_word(w, after_colon))
        after_colon = w.endswith(":")
    return " ".join(res)

data = yaml.safe_load(open(PUBLIST, encoding="utf-8"))
raw = open(PUBLIST, encoding="utf-8").read()
changes = 0
for p in data:
    old = p["title"]; new = sentence_case(old)
    if new != old:
        changes += 1
        print(f"- {old}\n+ {new}\n")
        # replace the exact title value in the raw text (single-quoted, escaping '')
        raw = raw.replace(f"title: '{old.replace(chr(39), chr(39)*2)}'",
                          f"title: '{new.replace(chr(39), chr(39)*2)}'", 1)
open(PUBLIST, "w", encoding="utf-8").write(raw)
print(f"Updated {changes} title(s).")
