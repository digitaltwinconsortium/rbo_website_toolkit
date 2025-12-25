# Agent Quickstart

Quick reference for AI agents working on this codebase.

> **See also**: [Agent Tips](agent_tips.md) for practical tips on image management, common issues, and workflows.

## Project Structure

```
rbo_website_sg/
├── content/
│   ├── config.json          # Site configuration
│   └── en-SG/
│       ├── pages/           # Static pages (index, contact)
│       └── events/          # Event pages
├── assets/
│   ├── css/                 # Stylesheets (DTC branded)
│   ├── js/                  # JavaScript
│   └── images/              # Images
│       ├── events/          # Event banners
│       ├── sponsors/        # Sponsor logos
│       └── team/            # Speaker/team photos
├── toolkit/
│   ├── build.py             # Build script
│   ├── requirements.txt     # Python dependencies
│   └── templates/           # Jinja2 templates
└── site/                    # Generated output (gitignored)
```

## Key Commands

```bash
# Build site
python toolkit/build.py

# Preview locally
python -m http.server -d site 8888
```

## Design System

The site follows DTC branding from the ANZ Regional Branch:
- **Primary Color**: #034ea2 (DTC Blue)
- **Secondary Color**: #f7941d (DTC Orange)
- **Font**: Poppins (Google Fonts)
- **Layout**: 1250px max-width container

## Content Format

Content files use HTML with YAML front matter in comments:

```html
<!--
title: Page Title
description: Page description for SEO
-->

<p>Page content here...</p>
```

## Event Front Matter

Events support full metadata including speakers and sponsors:

```html
<!--
title: Event Title
date: 2026-01-28
date_iso: 2026-01-28T14:00:00+08:00
date_display: January 28, 2026
status: upcoming
location: Singapore
format: In-Person
time: 2:00 PM - 5:00 PM
timezone: SGT
description: Event description
registration_url: https://example.com/register
registration_platform: LinkedIn Events
image: /assets/images/events/my-event.png
speakers:
  - name: Speaker Name
    title: Job Title
    organization: Company
    image: /assets/images/team/speaker.png
    remote: false
sponsors:
  - name: Sponsor Name
    logo: /assets/images/sponsors/sponsor.png
    url: https://sponsor.com
    tier: gold
-->
```

## Adding New Content

1. **New Page**: Add to `content/en-SG/pages/`
2. **New Event**: Add to `content/en-SG/events/`
3. **Update Nav**: Edit `content/config.json` navigation array

## Creating Placeholder Images

Use ImageMagick to create placeholder images:

```bash
# Event banner (1200x500)
magick -size 1200x500 gradient:'#034ea2'-'#f7941d' events/my-event.png

# Speaker photo (200x200)
magick -size 200x200 gradient:'#034ea2'-'#023a7a' team/speaker.png

# Sponsor logo (450x112)
magick -size 450x112 xc:'#ffffff' sponsors/sponsor.png
```

## Templates

| Template | Used For |
|----------|----------|
| home.html | Home page (index.html) |
| event.html | Event detail pages |
| events_list.html | Events listing (/events/) |
| contact.html | Contact page |
| page.html | Generic pages |

## Configuration

Edit `content/config.json` for:
- Site name and branding
- Navigation items
- Social links (LinkedIn)
- Feature flags
- Organization details (RBO name, DTC parent org)
