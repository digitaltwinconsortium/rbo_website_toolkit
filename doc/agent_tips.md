# Agent Tips

Practical tips for AI agents maintaining this site.

## Image Management

### Resizing Images with ImageMagick

Always resize user-provided images to the correct dimensions:

```bash
# Banner images (1200x500) - resize and crop to fit
magick original.png -resize 1200x500^ -gravity center -extent 1200x500 output.png

# Keep original for reference
mv original.png original-backup.png
```

### Standard Image Sizes

| Image Type | Dimensions | Location |
|------------|------------|----------|
| Hero/Event banners | 1200×500 | `assets/images/events/` |
| Contact banner | 1200×500 | `assets/images/` |
| Speaker photos | 200×200 | `assets/images/team/` |
| Sponsor logos | ~450×112 | `assets/images/sponsors/` |
| Site logo (SVG preferred) | Variable | `assets/images/` |

### Creating Placeholder Images

```bash
# Gradient banner placeholder
magick -size 1200x500 gradient:'#034ea2'-'#f7941d' placeholder-banner.png

# Solid color placeholder for logos
magick -size 450x112 xc:'#ffffff' placeholder-logo.png

# Speaker photo placeholder
magick -size 200x200 gradient:'#034ea2'-'#023a7a' placeholder-speaker.png
```

### Checking Image Dimensions

```bash
identify image.png
# Output: image.png PNG 1200x500 1200x500+0+0 8-bit sRGB ...
```

## Content Updates

### Adding a New Event

1. Create file: `content/en-SG/events/YYYY-MM-event-slug.html`
2. Add front matter with required fields (see QUICKSTART_AGENT.md)
3. Add event banner to `assets/images/events/`
4. Optionally add to navigation in `content/config.json`
5. Rebuild: `python toolkit/build.py`

### Updating Navigation

Edit `content/config.json` → `navigation` array:

```json
{"label": "New Page", "url": "/new-page/"}
```

For dropdowns:
```json
{
  "label": "Dropdown",
  "url": "#",
  "children": [
    {"label": "Child 1", "url": "https://example.com"}
  ]
}
```

## Build & Deploy

### Local Development

```bash
# Build and serve
python toolkit/build.py
python -m http.server -d site 8888
# Visit http://localhost:8888
```

### Verify Changes

```bash
# Check specific content in built pages
curl -s http://localhost:8888/ | grep "search term"

# List built files
ls -la site/
```

## CSS Overlay Adjustments

Banner overlays are controlled in `assets/css/style.css`:

```css
.banner-overlay {
    background-color: rgba(3, 78, 162, 0.75);  /* 75% opacity blue */
}
```

Adjust opacity (0.0 to 1.0) as needed for readability.

## Common Issues

### Build Errors

- **TemplateNotFound**: Run build from project root, not subdirectories
- **YAML parse errors**: Check front matter syntax in content files

### Image Issues

- Always use absolute paths starting with `/assets/...`
- SVG preferred for logos (scalable, smaller file size)
- Keep original high-res images as `*-original.png` backups

## Git Workflow

```bash
# After changes, rebuild and commit
python toolkit/build.py

# Commit content changes (not site/ - it's gitignored)
git add -A
git commit -m "Description of changes"
git push

# For toolkit submodule changes
cd toolkit
git add -A
git commit -m "Toolkit update"
git push
cd ..
git add toolkit
git commit -m "Update toolkit submodule"
git push
```

