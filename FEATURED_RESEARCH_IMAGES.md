# Featured Research image workflow

Use this workflow whenever updating the images shown in the Featured Research / 代表性研究 cards.

## Goal

Each `feature_image` should be a screenshot of the title area from the paper PDF, cropped to the same card ratio used by the site.

- Output directory: `images/featured/`
- Output format: `.png`
- Output size: `1200 x 750`
- Aspect ratio: `16:10`
- Source: the paper PDF in `documents/publication/`
- For `Transportation Science` papers: use page 2, because page 1 is the INFORMS information / cover page.
- For other papers: use page 1 unless the real article title starts on a later page.

## Site data

The homepage and research-page cards are generated from `_data/publist.yml`.

A publication appears as a card only when both are true:

```yml
featured: true
feature_image: '/images/featured/<name>.png'
```

Also keep `feature_alt` consistent with the page used:

```yml
feature_alt: 'Title area screenshot from the first page of the Nature Sustainability paper'
feature_alt: 'Title area screenshot from the second page of the Transportation Science paper'
```

## Current featured images

These are the current four featured-card images:

| File | Source PDF | Page |
| --- | --- | --- |
| `images/featured/housing_commute.png` | `documents/publication/Housing exchange framework to reduce carbon emissions from commuting.pdf` | 1 |
| `images/featured/path_recommendation.png` | `documents/publication/Individual path recommendation under public transit service disruptions considering behavior uncertainty.pdf` | 2 |
| `images/featured/lastmile_delivery.png` | `documents/publication/Predicting drivers'' route trajectories in last-mile delivery using a pair-wise attention-based pointer neural network.pdf` | 1 |
| `images/featured/path_choice_hypernetwork.png` | `documents/publication/Ex post path choice estimation for urban rail systems using smart card data - An aggregated time-space hypernetwork approach.pdf` | 2 |

## Render PDF pages

Render the relevant page with Poppler. The bundled runtime usually has `pdftoppm` here:

```bash
PDFTOPPM="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm"
mkdir -p /private/tmp/mos_feature_titles

"$PDFTOPPM" -f 1 -l 1 -r 180 -png \
  "documents/publication/Housing exchange framework to reduce carbon emissions from commuting.pdf" \
  /private/tmp/mos_feature_titles/housing

"$PDFTOPPM" -f 2 -l 2 -r 180 -png \
  "documents/publication/Individual path recommendation under public transit service disruptions considering behavior uncertainty.pdf" \
  /private/tmp/mos_feature_titles/path_recommendation

"$PDFTOPPM" -f 1 -l 1 -r 180 -png \
  "documents/publication/Predicting drivers'' route trajectories in last-mile delivery using a pair-wise attention-based pointer neural network.pdf" \
  /private/tmp/mos_feature_titles/lastmile

"$PDFTOPPM" -f 2 -l 2 -r 180 -png \
  "documents/publication/Ex post path choice estimation for urban rail systems using smart card data - An aggregated time-space hypernetwork approach.pdf" \
  /private/tmp/mos_feature_titles/path_choice
```

Fontconfig cache warnings are common in the sandbox. They are okay if the PNG files are produced and the rendered preview looks correct.

## Crop to card images

Use the following Python pattern. Adjust `x`, `y`, and `w` if a new PDF has a different title layout. The crop height is computed as `w * 10 / 16`.

```bash
python3 - <<'PY'
from PIL import Image, ImageDraw
from pathlib import Path

base = Path("/private/tmp/mos_feature_titles")
out = base / "crops"
out.mkdir(exist_ok=True)

crops = {
    # output file: (rendered PNG, x, y, width)
    "housing_commute.png": ("housing-01.png", 80, 90, 1320),
    "path_recommendation.png": ("path_recommendation-02.png", 100, 80, 1330),
    "lastmile_delivery.png": ("lastmile-01.png", 70, 120, 1220),
    "path_choice_hypernetwork.png": ("path_choice-02.png", 100, 80, 1330),
}

thumbs = []
for name, (src, x, y, w) in crops.items():
    im = Image.open(base / src).convert("RGB")
    h = round(w * 10 / 16)
    crop = im.crop((x, y, x + w, y + h))
    crop = crop.resize((1200, 750), Image.Resampling.LANCZOS)
    crop.save(out / name, optimize=True)

    preview = crop.copy()
    preview.thumbnail((520, 325))
    canvas = Image.new("RGB", (560, 380), "white")
    canvas.paste(preview, (20, 15))
    ImageDraw.Draw(canvas).text((20, 350), name, fill=(0, 0, 0))
    thumbs.append(canvas)

montage = Image.new("RGB", (1120, 760), "white")
for i, thumb in enumerate(thumbs):
    montage.paste(thumb, ((i % 2) * 560, (i // 2) * 380))
montage.save(base / "feature_crop_montage.png")
PY
```

Visually inspect the montage before copying the images into the repo.

## Replace repo images

After the crop looks good:

```bash
cp /private/tmp/mos_feature_titles/crops/housing_commute.png images/featured/housing_commute.png
cp /private/tmp/mos_feature_titles/crops/path_recommendation.png images/featured/path_recommendation.png
cp /private/tmp/mos_feature_titles/crops/lastmile_delivery.png images/featured/lastmile_delivery.png
cp /private/tmp/mos_feature_titles/crops/path_choice_hypernetwork.png images/featured/path_choice_hypernetwork.png
```

If replacing an old featured image with a new filename, update `_data/publist.yml` and delete the unused old file from `images/featured/`.

## Final checks

Run:

```bash
JEKYLL_NO_BUNDLER_REQUIRE=true ~/.gem/ruby/2.6.0/bin/jekyll build
```

Then check:

```bash
rg -n "feature-citation|images/featured|Title area screenshot" _site/index.html _site/en/index.html _site/research/index.html _site/en/research/index.html
```

Confirm:

- Featured-card images load from `images/featured/*.png`.
- The card image shows the paper title area, not a figure from the paper.
- `Transportation Science` cards use page 2.
- The card citation line appears under the description.
- No old unused images remain in `images/featured/`.
