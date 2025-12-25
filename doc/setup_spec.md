# RBO Website Toolkit - Technical Specification v2.0

## Project Overview

**Purpose**: Create a static website toolkit for Digital Twin Consortium (DTC) Regional Branch Organizers (RBOs) that enables GenAI-assisted website maintenance without requiring WordPress or database backends.

**Target Users**: RBOs in ANZ, Singapore, Japan, India, and other regions who need professional websites for DTC regional activities.

**Key Design Principles**:
1. Static HTML hosted on GitHub Pages
2. GenAI-maintainable (simple, clear patterns)
3. Forkable/submodule architecture for toolkit updates
4. Python-based build system
5. Azure OpenAI integration for image generation
6. Future-ready for internationalization
7. Accessible (WCAG 2.1 AA compliant)

---

## Framework Selection: Custom Python Static Site Generator

### Rationale

After evaluating Jekyll, Hugo, and other static site generators, we recommend a **lightweight custom Python-based solution** for the following reasons:

1. **GenAI Maintainability**: Simple Jinja2 templates are easier for AI tools to understand and modify than complex SSG-specific syntax
2. **Minimal Dependencies**: Only Python and a few pip packages required
3. **Explicit Behavior**: No "magic" - every step is visible and understandable
4. **Platform Compatibility**: Works on Windows, Linux, and macOS without Ruby/Go dependencies
5. **GitHub Pages Compatible**: Generates plain HTML that GitHub Pages serves directly

### Core Technologies

| Component | Technology | Purpose |
|-----------|------------|---------|
| Template Engine | Jinja2 | Header/footer includes, page layouts |
| Build Script | Python 3.8+ | Site compilation |
| Dev Server | Python + watchdog | Live reload development |
| Image Generation | Azure OpenAI DALL-E 3 | Event banners, hero images |
| Hosting | GitHub Pages | Static site hosting |
| Version Control | Git | Content management, collaboration |
| Validation | JSON Schema + custom | Content integrity |

---

## Repository Architecture

### Option A: Fork Model (Recommended for Most RBOs)

```
dtc-rbo-website-toolkit/          # Upstream toolkit repository
|
+-- [RBO forks this repo]
    |
    +-- digitaltwins-anz/         # Example: ANZ RBO site
    +-- digitaltwins-sg/          # Example: Singapore RBO site
```

### Option B: Submodule Model (For Advanced Users)

```
digitaltwins-anz/                  # RBO's website repo
|
+-- toolkit/                       # Submodule: dtc-rbo-website-toolkit
+-- content/                       # RBO-specific content
+-- site/                          # Generated output
```

### Directory Structure

```
dtc-rbo-website-toolkit/
|
+-- .github/
|   +-- workflows/
|       +-- deploy.yml            # GitHub Actions for auto-deploy
|       +-- validate.yml          # Content validation on PR
|
+-- toolkit/
|   +-- build.py                  # Main build script
|   +-- dev_server.py             # Development server with hot reload
|   +-- validate.py               # Content validation script
|   +-- image_generator.py        # Azure OpenAI DALL-E integration
|   +-- event_scraper.py          # BrightTalk/LinkedIn event parser
|   +-- requirements.txt          # Python dependencies
|   +-- schemas/
|   |   +-- config.schema.json    # JSON Schema for config validation
|   |   +-- event.schema.json     # Schema for event front matter
|   |   +-- page.schema.json      # Schema for page front matter
|   +-- templates/
|       +-- base.html             # Base layout template
|       +-- header.html           # Site header include
|       +-- footer.html           # Site footer include
|       +-- home.html             # Home page template
|       +-- event.html            # Event page template (handles all states)
|       +-- events_list.html      # Events listing template
|       +-- initiative.html       # Initiative page template
|       +-- team_member.html      # Team member profile template
|       +-- team_list.html        # Team listing template
|       +-- contact.html          # Contact page template
|       +-- newsletter.html       # Newsletter signup page template
|       +-- news_article.html     # News article template
|       +-- news_list.html        # News listing template
|       +-- page.html             # Generic page template
|       +-- 404.html              # Error page template
|
+-- agent_instructions/
|   +-- README.md                 # Overview for AI agents
|   +-- new_event_page.md         # Instructions for creating event pages
|   +-- update_event_post.md      # Instructions for post-event updates
|   +-- update_home_page.md       # Instructions for updating home page
|   +-- new_initiative.md         # Instructions for initiative pages
|   +-- new_news_article.md       # Instructions for news articles
|   +-- update_team.md            # Instructions for team updates
|   +-- generate_images.md        # Instructions for AI image generation
|   +-- deploy_site.md            # Instructions for deployment
|   +-- custom_domain.md          # Custom domain setup guide
|   +-- validate_content.md       # Content validation guide
|   +-- versioning_updates.md     # How to update toolkit from upstream
|
+-- content/
|   +-- config.json               # Site-wide configuration
|   +-- en-AU/                    # Default locale (configurable)
|   |   +-- pages/
|   |   |   +-- index.html        # Home page content
|   |   |   +-- contact.html      # Contact page content
|   |   |   +-- about.html        # About page content
|   |   |   +-- newsletter.html   # Newsletter/follow page
|   |   |   +-- 404.html          # Custom 404 page
|   |   +-- events/
|   |   |   +-- 2024-dan-isaacs-roundtable.html
|   |   |   +-- 2023-perth-natural-resources.html
|   |   +-- initiatives/
|   |   |   +-- healthcare-digital-twins.html
|   |   +-- news/                 # Optional - news articles
|   |   |   +-- .gitkeep          # Placeholder until news exists
|   |   +-- team/
|   |       +-- pieter-van-schalkwyk.html
|   |       +-- sean-whiteley.html
|   +-- ja-JP/                    # Future: Japanese locale
|       +-- .gitkeep              # Placeholder for future i18n
|
+-- assets/
|   +-- css/
|   |   +-- style.css             # Main stylesheet
|   |   +-- responsive.css        # Mobile responsive styles
|   |   +-- accessibility.css     # Accessibility enhancements
|   +-- js/
|   |   +-- main.js               # Main JavaScript
|   |   +-- accessibility.js      # Accessibility helpers
|   +-- images/
|   |   +-- dtc-logo.png          # DTC branding
|   |   +-- rbo-logo.png          # RBO-specific logo (customize)
|   |   +-- og-default.png        # Default Open Graph image
|   |   +-- events/               # Event-specific images
|   |   +-- team/                 # Team member photos
|   |   +-- sponsors/             # Sponsor/partner logos
|   |   +-- news/                 # News article images
|   +-- fonts/
|   +-- downloads/                # Downloadable resources (PDFs, slides)
|
+-- site/                         # Generated output (gitignored in toolkit)
|   +-- index.html
|   +-- sitemap.xml               # Auto-generated sitemap
|   +-- robots.txt                # Search engine instructions
|   +-- events/
|   +-- ...
|
+-- .env_template                 # Template for credentials
+-- .gitignore                    # Git ignore rules
+-- README.md                     # Project documentation
+-- CUSTOMIZATION.md              # Guide for RBO customizations
+-- UPDATING.md                   # How to update from upstream
+-- LICENSE                       # License file
```

---

## Configuration File Specification

### config.json

```json
{
  "site": {
    "name": "Digital Twins Consortium - ANZ",
    "short_name": "DTC ANZ",
    "tagline": "Regional Branch Australia & New Zealand",
    "description": "Facilitating local Digital Twin Consortium activities in Australia and New Zealand",
    "url": "https://www.digitaltwins-anz.org",
    "default_locale": "en-AU",
    "supported_locales": ["en-AU"],
    "timezone": "Australia/Sydney"
  },
  "organization": {
    "rbo_name": "XMPro",
    "rbo_website": "https://xmpro.com",
    "parent_org": "Digital Twin Consortium",
    "parent_website": "https://www.digitaltwinconsortium.org"
  },
  "contact": {
    "linkedin_page": "https://www.linkedin.com/company/digitaltwins-anz",
    "dtc_contact_page": "https://www.digitaltwinconsortium.org/contact/",
    "email": null
  },
  "social": {
    "linkedin": "https://www.linkedin.com/company/digitaltwins-anz",
    "twitter": null,
    "youtube": null
  },
  "branding": {
    "primary_color": "#0066CC",
    "secondary_color": "#003366",
    "accent_color": "#00AAFF",
    "logo": "/assets/images/dtc-anz-logo.png",
    "favicon": "/assets/images/favicon.ico"
  },
  "navigation": [
    {"label": "Home", "url": "/"},
    {"label": "Events", "url": "/events/"},
    {
      "label": "Initiatives",
      "url": "/initiatives/",
      "children": [
        {"label": "Healthcare Digital Twins", "url": "/initiatives/healthcare-digital-twins/"},
        {"label": "Natural Resources", "url": "/initiatives/natural-resources/"}
      ]
    },
    {"label": "News", "url": "/news/", "enabled": false},
    {"label": "Team", "url": "/team/"},
    {"label": "About", "url": "/about/"},
    {"label": "Contact", "url": "/contact/"}
  ],
  "sponsors": {
    "enabled": true,
    "title": "Our Partners",
    "show_on_homepage": true,
    "items": [
      {
        "name": "XMPro",
        "logo": "/assets/images/sponsors/xmpro.png",
        "url": "https://xmpro.com",
        "tier": "platinum"
      },
      {
        "name": "Dell Technologies",
        "logo": "/assets/images/sponsors/dell.png",
        "url": "https://www.dell.com",
        "tier": "gold"
      },
      {
        "name": "Microsoft",
        "logo": "/assets/images/sponsors/microsoft.png",
        "url": "https://www.microsoft.com",
        "tier": "gold"
      }
    ]
  },
  "features": {
    "enable_event_registration_links": true,
    "show_past_events": true,
    "enable_team_profiles": true,
    "enable_news_section": false,
    "enable_newsletter_page": true,
    "show_sponsors_footer": true
  },
  "seo": {
    "google_site_verification": null,
    "bing_site_verification": null
  },
  "analytics": {
    "google_analytics_id": null,
    "enable_cookie_consent": false
  },
  "accessibility": {
    "skip_to_content": true,
    "high_contrast_toggle": false,
    "font_size_toggle": false
  },
  "build": {
    "output_dir": "site",
    "content_dir": "content",
    "assets_dir": "assets",
    "templates_dir": "toolkit/templates",
    "generate_sitemap": true,
    "generate_robots_txt": true
  }
}
```

---

## Template Specifications

### base.html (Base Layout)

```html
<!DOCTYPE html>
<html lang="{{ config.site.default_locale }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ page.description | default(config.site.description) }}">
    <title>{{ page.title }} | {{ config.site.name }}</title>
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="stylesheet" href="/assets/css/responsive.css">
    <link rel="stylesheet" href="/assets/css/accessibility.css">
    <link rel="icon" href="{{ config.branding.favicon }}">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{{ page.title }} | {{ config.site.name }}">
    <meta property="og:description" content="{{ page.description | default(config.site.description) }}">
    <meta property="og:image" content="{{ config.site.url }}{{ page.image | default('/assets/images/og-default.png') }}">
    <meta property="og:url" content="{{ config.site.url }}{{ page.url }}">
    <meta property="og:type" content="{{ page.og_type | default('website') }}">
    <meta property="og:site_name" content="{{ config.site.name }}">
    
    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{{ page.title }} | {{ config.site.name }}">
    <meta name="twitter:description" content="{{ page.description | default(config.site.description) }}">
    <meta name="twitter:image" content="{{ config.site.url }}{{ page.image | default('/assets/images/og-default.png') }}">
    
    <!-- SEO Verification -->
    {% if config.seo.google_site_verification %}
    <meta name="google-site-verification" content="{{ config.seo.google_site_verification }}">
    {% endif %}
    {% if config.seo.bing_site_verification %}
    <meta name="msvalidate.01" content="{{ config.seo.bing_site_verification }}">
    {% endif %}
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{{ config.site.url }}{{ page.url }}">
    
    <!-- Analytics -->
    {% if config.analytics.google_analytics_id %}
    <script async src="https://www.googletagmanager.com/gtag/js?id={{ config.analytics.google_analytics_id }}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', '{{ config.analytics.google_analytics_id }}');
    </script>
    {% endif %}
</head>
<body>
    {% if config.accessibility.skip_to_content %}
    <a href="#main-content" class="skip-link">Skip to main content</a>
    {% endif %}
    
    {% include 'header.html' %}
    
    <main id="main-content" class="main-content" role="main">
        {% block content %}{% endblock %}
    </main>
    
    {% include 'footer.html' %}
    
    <script src="/assets/js/main.js"></script>
    <script src="/assets/js/accessibility.js"></script>
</body>
</html>
```

### header.html

```html
<header class="site-header" role="banner">
    <div class="header-container">
        <div class="logo-section">
            <a href="/" class="logo-link" aria-label="{{ config.site.name }} - Home">
                <img src="{{ config.branding.logo }}" alt="{{ config.site.name }}" class="site-logo">
            </a>
            <div class="site-title">
                <h1>{{ config.site.short_name }}</h1>
                <p class="tagline">{{ config.site.tagline }}</p>
            </div>
        </div>
        
        <nav class="main-navigation" aria-label="Main navigation" role="navigation">
            <button class="mobile-menu-toggle" 
                    aria-expanded="false" 
                    aria-controls="nav-menu"
                    aria-label="Toggle navigation menu">
                <span class="sr-only">Menu</span>
                <span class="hamburger" aria-hidden="true"></span>
            </button>
            <ul id="nav-menu" class="nav-menu">
                {% for item in config.navigation %}
                {% if item.enabled is not defined or item.enabled %}
                <li class="nav-item{% if item.children %} has-dropdown{% endif %}{% if page.url == item.url or page.url.startswith(item.url) %} active{% endif %}">
                    <a href="{{ item.url }}"{% if item.children %} aria-haspopup="true" aria-expanded="false"{% endif %}>
                        {{ item.label }}
                        {% if item.children %}<span class="dropdown-arrow" aria-hidden="true"></span>{% endif %}
                    </a>
                    {% if item.children %}
                    <ul class="dropdown-menu" role="menu">
                        {% for child in item.children %}
                        <li role="none">
                            <a href="{{ child.url }}" role="menuitem">{{ child.label }}</a>
                        </li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                </li>
                {% endif %}
                {% endfor %}
            </ul>
        </nav>
    </div>
</header>
```

### footer.html

```html
<footer class="site-footer" role="contentinfo">
    <div class="footer-container">
        <div class="footer-section">
            <h3>About {{ config.site.short_name }}</h3>
            <p>{{ config.site.description }}</p>
            <p>Regional Branch Organizer: <a href="{{ config.organization.rbo_website }}" target="_blank" rel="noopener">{{ config.organization.rbo_name }}</a></p>
        </div>
        
        <div class="footer-section">
            <h3>Connect</h3>
            <ul class="social-links">
                {% if config.social.linkedin %}
                <li><a href="{{ config.social.linkedin }}" target="_blank" rel="noopener" aria-label="Follow us on LinkedIn">LinkedIn</a></li>
                {% endif %}
                {% if config.social.twitter %}
                <li><a href="{{ config.social.twitter }}" target="_blank" rel="noopener" aria-label="Follow us on Twitter">Twitter/X</a></li>
                {% endif %}
                {% if config.social.youtube %}
                <li><a href="{{ config.social.youtube }}" target="_blank" rel="noopener" aria-label="Subscribe to our YouTube channel">YouTube</a></li>
                {% endif %}
            </ul>
            {% if config.features.enable_newsletter_page %}
            <p><a href="/newsletter/">Stay Updated</a></p>
            {% endif %}
        </div>
        
        <div class="footer-section">
            <h3>{{ config.organization.parent_org }}</h3>
            <p><a href="{{ config.organization.parent_website }}" target="_blank" rel="noopener">Visit DTC Website</a></p>
            <p><a href="{{ config.contact.dtc_contact_page }}" target="_blank" rel="noopener">Contact DTC</a></p>
        </div>
    </div>
    
    {% if config.features.show_sponsors_footer and config.sponsors.enabled and config.sponsors.items %}
    <div class="footer-sponsors">
        <h3>{{ config.sponsors.title }}</h3>
        <div class="sponsor-logos">
            {% for sponsor in config.sponsors.items %}
            <a href="{{ sponsor.url }}" target="_blank" rel="noopener" class="sponsor-link sponsor-{{ sponsor.tier }}" aria-label="{{ sponsor.name }}">
                <img src="{{ sponsor.logo }}" alt="{{ sponsor.name }}" class="sponsor-logo" loading="lazy">
            </a>
            {% endfor %}
        </div>
    </div>
    {% endif %}
    
    <div class="footer-bottom">
        <p>&copy; {{ current_year }} {{ config.site.name }}. Part of the <a href="{{ config.organization.parent_website }}">{{ config.organization.parent_org }}</a>.</p>
        <p>Digital Twin Consortium is a registered trademark of OMG.</p>
    </div>
</footer>
```

### event.html (Unified Event Template - Handles All States)

```html
{% extends 'base.html' %}

{% block content %}
<article class="event-page" itemscope itemtype="https://schema.org/Event">
    <header class="event-header">
        {% if event.image %}
        <div class="event-hero" style="background-image: url('{{ event.image }}');">
            <div class="hero-overlay">
                <h1 class="event-title" itemprop="name">{{ event.title }}</h1>
            </div>
        </div>
        {% else %}
        <h1 class="event-title" itemprop="name">{{ event.title }}</h1>
        {% endif %}
        
        <!-- Event Status Badge -->
        <div class="event-status-badge status-{{ event.status }}">
            {% if event.status == 'upcoming' %}
            <span class="badge badge-upcoming">Upcoming Event</span>
            {% elif event.status == 'past' %}
            <span class="badge badge-past">Past Event</span>
            {% endif %}
        </div>
        
        <div class="event-meta">
            <div class="event-date">
                <span class="icon" aria-hidden="true">&#128197;</span>
                <time datetime="{{ event.date_iso }}" itemprop="startDate" content="{{ event.date_iso }}">{{ event.date_display }}</time>
            </div>
            {% if event.time %}
            <div class="event-time">
                <span class="icon" aria-hidden="true">&#128336;</span>
                <span>{{ event.time }} {{ event.timezone }}</span>
            </div>
            {% endif %}
            {% if event.location %}
            <div class="event-location" itemprop="location" itemscope itemtype="https://schema.org/Place">
                <span class="icon" aria-hidden="true">&#128205;</span>
                <span itemprop="name">{{ event.location }}</span>
            </div>
            {% endif %}
            {% if event.format %}
            <div class="event-format">
                <span class="icon" aria-hidden="true">&#127760;</span>
                <span>{{ event.format }}</span>
            </div>
            {% endif %}
        </div>
    </header>
    
    <div class="event-content" itemprop="description">
        {{ content }}
    </div>
    
    <!-- UPCOMING EVENT: Registration CTA -->
    {% if event.status == 'upcoming' and event.registration_url %}
    <section class="event-cta event-registration">
        <h2>Register for This Event</h2>
        <a href="{{ event.registration_url }}" 
           class="btn btn-primary btn-large" 
           target="_blank" 
           rel="noopener"
           itemprop="url">
            Register Now
        </a>
        <p class="registration-note">Registration is handled via {{ event.registration_platform }}</p>
    </section>
    {% endif %}
    
    <!-- PAST EVENT: Recording Section -->
    {% if event.status == 'past' and event.recording_url %}
    <section class="event-recording">
        <h2>Event Recording</h2>
        <div class="recording-embed">
            {% if 'youtube.com' in event.recording_url or 'youtu.be' in event.recording_url %}
            <div class="video-container">
                <iframe src="{{ event.recording_embed_url }}" 
                        title="{{ event.title }} - Recording"
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen
                        loading="lazy"></iframe>
            </div>
            {% elif 'brighttalk.com' in event.recording_url %}
            <div class="brighttalk-embed">
                <a href="{{ event.recording_url }}" class="btn btn-secondary" target="_blank" rel="noopener">
                    Watch on BrightTalk
                </a>
            </div>
            {% else %}
            <a href="{{ event.recording_url }}" class="btn btn-secondary" target="_blank" rel="noopener">
                Watch Recording on {{ event.recording_platform | default('External Site') }}
            </a>
            {% endif %}
        </div>
    </section>
    {% endif %}
    
    <!-- PAST EVENT: Resources/Downloads Section -->
    {% if event.status == 'past' and (event.slides_url or event.resources) %}
    <section class="event-resources">
        <h2>Event Resources</h2>
        <ul class="resource-list">
            {% if event.slides_url %}
            <li>
                <a href="{{ event.slides_url }}" class="resource-link" target="_blank" rel="noopener">
                    <span class="icon" aria-hidden="true">&#128196;</span>
                    Presentation Slides (PDF)
                </a>
            </li>
            {% endif %}
            {% if event.resources %}
            {% for resource in event.resources %}
            <li>
                <a href="{{ resource.url }}" class="resource-link" target="_blank" rel="noopener">
                    <span class="icon" aria-hidden="true">&#128196;</span>
                    {{ resource.title }}
                </a>
            </li>
            {% endfor %}
            {% endif %}
        </ul>
    </section>
    {% endif %}
    
    <!-- PAST EVENT: Photo Gallery -->
    {% if event.status == 'past' and event.photos_gallery %}
    <section class="event-photos">
        <h2>Event Photos</h2>
        <div class="photo-gallery">
            {% for photo in event.photos %}
            <figure class="gallery-item">
                <img src="{{ photo.url }}" alt="{{ photo.caption | default('Event photo') }}" loading="lazy">
                {% if photo.caption %}
                <figcaption>{{ photo.caption }}</figcaption>
                {% endif %}
            </figure>
            {% endfor %}
        </div>
    </section>
    {% endif %}
    
    <!-- Speakers Section (All Events) -->
    {% if event.speakers %}
    <section class="event-speakers">
        <h2>Speakers</h2>
        <div class="speakers-grid">
            {% for speaker in event.speakers %}
            <div class="speaker-card" itemscope itemtype="https://schema.org/Person">
                {% if speaker.image %}
                <img src="{{ speaker.image }}" alt="{{ speaker.name }}" class="speaker-photo" itemprop="image" loading="lazy">
                {% endif %}
                <h3 itemprop="name">{{ speaker.name }}</h3>
                <p class="speaker-title" itemprop="jobTitle">{{ speaker.title }}</p>
                <p class="speaker-org" itemprop="worksFor">{{ speaker.organization }}</p>
            </div>
            {% endfor %}
        </div>
    </section>
    {% endif %}
    
    <div class="event-footer">
        <a href="/events/" class="back-link">&larr; Back to Events</a>
    </div>
</article>

<!-- JSON-LD Structured Data for SEO -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "{{ event.title }}",
  "description": "{{ event.description | default(page.description) }}",
  "startDate": "{{ event.date_iso }}",
  "eventStatus": "{% if event.status == 'upcoming' %}https://schema.org/EventScheduled{% else %}https://schema.org/EventMovedOnline{% endif %}",
  "eventAttendanceMode": "{% if 'online' in event.format|lower %}https://schema.org/OnlineEventAttendanceMode{% else %}https://schema.org/OfflineEventAttendanceMode{% endif %}",
  "location": {
    "@type": "{% if 'online' in event.format|lower %}VirtualLocation{% else %}Place{% endif %}",
    "name": "{{ event.location }}"
  },
  "image": "{{ config.site.url }}{{ event.image }}",
  "organizer": {
    "@type": "Organization",
    "name": "{{ config.site.name }}",
    "url": "{{ config.site.url }}"
  }
  {% if event.speakers %},
  "performer": [
    {% for speaker in event.speakers %}
    {
      "@type": "Person",
      "name": "{{ speaker.name }}",
      "jobTitle": "{{ speaker.title }}",
      "worksFor": "{{ speaker.organization }}"
    }{% if not loop.last %},{% endif %}
    {% endfor %}
  ]
  {% endif %}
}
</script>
{% endblock %}
```

### news_article.html (News Article Template)

```html
{% extends 'base.html' %}

{% block content %}
<article class="news-article" itemscope itemtype="https://schema.org/NewsArticle">
    <header class="article-header">
        {% if article.image %}
        <div class="article-hero">
            <img src="{{ article.image }}" alt="{{ article.title }}" itemprop="image">
        </div>
        {% endif %}
        
        <h1 class="article-title" itemprop="headline">{{ article.title }}</h1>
        
        <div class="article-meta">
            <time datetime="{{ article.date_iso }}" itemprop="datePublished">{{ article.date_display }}</time>
            {% if article.author %}
            <span class="article-author" itemprop="author">by {{ article.author }}</span>
            {% endif %}
            {% if article.category %}
            <span class="article-category">{{ article.category }}</span>
            {% endif %}
        </div>
    </header>
    
    <div class="article-content" itemprop="articleBody">
        {{ content }}
    </div>
    
    {% if article.source_url %}
    <div class="article-source">
        <p>Source: <a href="{{ article.source_url }}" target="_blank" rel="noopener">{{ article.source_name | default('Original Article') }}</a></p>
    </div>
    {% endif %}
    
    <div class="article-footer">
        <a href="/news/" class="back-link">&larr; Back to News</a>
    </div>
</article>
{% endblock %}
```

### news_list.html (News Listing Template)

```html
{% extends 'base.html' %}

{% block content %}
<section class="news-list">
    <header class="page-header">
        <h1>News & Announcements</h1>
        <p>Stay updated with the latest from {{ config.site.short_name }} and the Digital Twin Consortium.</p>
    </header>
    
    {% if news_articles %}
    <div class="news-grid">
        {% for article in news_articles %}
        <article class="news-card">
            {% if article.image %}
            <a href="{{ article.url }}" class="news-card-image-link">
                <img src="{{ article.image }}" alt="" class="news-card-image" loading="lazy">
            </a>
            {% endif %}
            <div class="news-card-content">
                <time datetime="{{ article.date_iso }}" class="news-card-date">{{ article.date_display }}</time>
                <h2 class="news-card-title">
                    <a href="{{ article.url }}">{{ article.title }}</a>
                </h2>
                <p class="news-card-excerpt">{{ article.excerpt | default(article.description) }}</p>
                <a href="{{ article.url }}" class="read-more">Read more &rarr;</a>
            </div>
        </article>
        {% endfor %}
    </div>
    {% else %}
    <div class="empty-state">
        <p>No news articles yet. Check back soon for updates!</p>
        <p>In the meantime, follow us on <a href="{{ config.social.linkedin }}" target="_blank" rel="noopener">LinkedIn</a> for the latest announcements.</p>
    </div>
    {% endif %}
</section>
{% endblock %}
```

### newsletter.html (Newsletter/Follow Page Template)

```html
{% extends 'base.html' %}

{% block content %}
<section class="newsletter-page">
    <header class="page-header">
        <h1>Stay Connected</h1>
        <p>Keep up with {{ config.site.short_name }} events, initiatives, and digital twin news.</p>
    </header>
    
    <div class="newsletter-content">
        {{ content }}
    </div>
    
    <div class="connect-options">
        <div class="connect-card primary-connect">
            <div class="connect-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
            </div>
            <h2>Follow Us on LinkedIn</h2>
            <p>Get event announcements, industry insights, and connect with the digital twin community in our region.</p>
            <a href="{{ config.social.linkedin }}" class="btn btn-primary btn-large" target="_blank" rel="noopener">
                Follow {{ config.site.short_name }}
            </a>
        </div>
        
        <div class="connect-card">
            <h2>Digital Twin Consortium</h2>
            <p>For global DTC updates, membership information, and worldwide events:</p>
            <a href="{{ config.organization.parent_website }}" class="btn btn-secondary" target="_blank" rel="noopener">
                Visit DTC Website
            </a>
        </div>
        
        {% if config.contact.email %}
        <div class="connect-card">
            <h2>Contact Us Directly</h2>
            <p>Have questions about our regional activities or want to get involved?</p>
            <a href="mailto:{{ config.contact.email }}" class="btn btn-secondary">
                Email Us
            </a>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
```

### 404.html (Error Page Template)

```html
{% extends 'base.html' %}

{% block content %}
<section class="error-page">
    <div class="error-content">
        <h1>Page Not Found</h1>
        <p class="error-code">404</p>
        <p>Sorry, the page you're looking for doesn't exist or has been moved.</p>
        
        <div class="error-actions">
            <a href="/" class="btn btn-primary">Go to Homepage</a>
            <a href="/events/" class="btn btn-secondary">View Events</a>
        </div>
        
        <div class="error-help">
            <h2>Looking for something specific?</h2>
            <ul>
                <li><a href="/events/">Upcoming and past events</a></li>
                <li><a href="/initiatives/">Our initiatives</a></li>
                <li><a href="/team/">Meet our team</a></li>
                <li><a href="/contact/">Contact us</a></li>
            </ul>
        </div>
    </div>
</section>
{% endblock %}
```

---

## Content Page Formats

### Event Content with Full Lifecycle Support

```html
<!--
title: The Future of Digital Twins - Exclusive Roundtable with Dan Isaacs
date: 2024-10-15
date_iso: 2024-10-15T09:00:00+10:00
date_display: October 15-16, 2024
time: 9:00 AM - 1:00 PM
timezone: AEST/AEDT
location: Sydney & Melbourne, Australia
format: In-Person Roundtable
status: past
image: /assets/images/events/dan-isaacs-2024.png
description: Join us for an exclusive executive roundtable featuring Dan Isaacs, CTO of Digital Twin Consortium.

# Registration (for upcoming events)
registration_url: https://www.brighttalk.com/webcast/xxxxx
registration_platform: BrightTalk

# Post-event content (for past events)
recording_url: https://www.youtube.com/watch?v=xxxxx
recording_embed_url: https://www.youtube.com/embed/xxxxx
recording_platform: YouTube
slides_url: /assets/downloads/dan-isaacs-roundtable-2024-slides.pdf
resources:
  - title: Workshop Materials
    url: /assets/downloads/workshop-materials.pdf
  - title: iBOS Framework Overview
    url: /assets/downloads/ibos-framework.pdf
photos_gallery: true
photos:
  - url: /assets/images/events/2024-roundtable/photo1.jpg
    caption: Dan Isaacs presenting on Digital Twin evolution
  - url: /assets/images/events/2024-roundtable/photo2.jpg
    caption: Interactive workshop session

speakers:
  - name: Dan Isaacs
    title: CTO and GM
    organization: Digital Twin Consortium
    image: /assets/images/team/dan-isaacs.jpg
  - name: Pieter van Schalkwyk
    title: CEO
    organization: XMPro
    image: /assets/images/team/pieter-van-schalkwyk.jpg
-->

<p>Join us for an exclusive executive roundtable featuring <strong>Dan Isaacs</strong>, CTO and GM of the Digital Twin Consortium, and <strong>Pieter van Schalkwyk</strong>, CEO of XMPro and Regional Branch Organiser for DTC ANZ.</p>

<h2>Agenda</h2>
<ul>
    <li><strong>1-hour presentation</strong> by Dan Isaacs on the evolution of Digital Twin Systems</li>
    <li><strong>30-minute presentation</strong> by Pieter van Schalkwyk on the iBOS Framework</li>
    <li><strong>1-hour interactive workshop</strong> on composing digital twins based on attendees' use cases</li>
</ul>

<h2>Who Should Attend</h2>
<p>This event is designed for:</p>
<ul>
    <li>C-level executives and decision-makers interested in digital twin technology</li>
    <li>Technology leaders exploring digital transformation initiatives</li>
    <li>Engineers and architects working on industrial IoT and digital twin projects</li>
</ul>

<h2>About Digital Twin Consortium</h2>
<p>Digital Twin Consortium is The Authority in Digital Twin. It coalesces industry, government, and academia to drive consistency in vocabulary, architecture, security, and interoperability of digital twin technology.</p>
```

### News Article Content

```html
<!--
title: Digital Twin Consortium Expands Regional Branch Program to Southeast Asia
date: 2023-04-18
date_iso: 2023-04-18
date_display: April 18, 2023
author: DTC Communications
category: Announcements
image: /assets/images/news/dtc-sea-expansion.png
description: DTC announces Axomem as inaugural Regional Branch Organizer for Southeast Asia.
source_url: https://www.digitaltwinconsortium.org/press-room/04-18-23/
source_name: Digital Twin Consortium
-->

<p>The Digital Twin Consortium (DTC) today announced it has expanded its Regional Branch Organizer (RBO) program to include Southeast Asia, a critical region for DTC and its parent company, the Object Management Group.</p>

<p>Axomem, a digital twin startup based in Singapore, will serve as the inaugural RBO for the region, facilitating local DTC engagements with regional industry, government, and academic institutions.</p>

<blockquote>
<p>"Axomem is looking forward to being the inaugural RBO for Southeast Asia. We're already collaborating on local projects using digital twin technologies to predict disease in acute-care hospitals."</p>
<cite>- Sean Whiteley, Founder of Axomem</cite>
</blockquote>
```

### Newsletter Page Content (Default)

```html
<!--
title: Stay Connected
description: Follow DTC ANZ for event updates, industry insights, and digital twin news.
-->

<p>The best way to stay informed about {{ config.site.short_name }} activities is to follow us on LinkedIn. We share:</p>

<ul>
    <li><strong>Event announcements</strong> - Be the first to know about upcoming roundtables, webinars, and conferences</li>
    <li><strong>Industry insights</strong> - Curated content about digital twin technology and applications</li>
    <li><strong>Community updates</strong> - News from our members and partners across the region</li>
    <li><strong>DTC resources</strong> - New publications, frameworks, and tools from the Digital Twin Consortium</li>
</ul>

<p>We typically post 2-4 times per week, keeping you informed without overwhelming your feed.</p>
```

### 404 Page Content (Default)

```html
<!--
title: Page Not Found
description: The requested page could not be found.
-->

<!-- Default 404 content is handled by the template -->
<!-- Customize this file to add additional helpful content -->
```

---

## Build Script with Full Features

### toolkit/build.py

```python
#!/usr/bin/env python3
"""
RBO Website Toolkit - Static Site Generator v2.0
Builds static HTML from templates and content files.
Includes sitemap generation, validation, and SEO features.
"""

import os
import sys
import json
import shutil
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml

# Configuration
DEFAULT_CONFIG = {
    "site": {
        "default_locale": "en-AU",
        "url": "https://example.com"
    },
    "build": {
        "output_dir": "site",
        "content_dir": "content",
        "assets_dir": "assets",
        "templates_dir": "toolkit/templates",
        "generate_sitemap": True,
        "generate_robots_txt": True
    },
    "features": {
        "enable_news_section": False
    }
}

class SiteBuilder:
    def __init__(self, config_path="content/config.json"):
        self.config = self.load_config(config_path)
        self.pages = []
        self.events = []
        self.news = []
        self.team = []
        self.initiatives = []
        
    def load_config(self, config_path):
        """Load site configuration from JSON file."""
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # Merge with defaults
                return self._merge_config(DEFAULT_CONFIG, config)
        return DEFAULT_CONFIG
    
    def _merge_config(self, default, override):
        """Deep merge configuration dictionaries."""
        result = default.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_config(result[key], value)
            else:
                result[key] = value
        return result

    def parse_front_matter(self, content):
        """Parse YAML-like front matter from HTML comment block."""
        pattern = r'<!--\s*(.*?)\s*-->'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            return {}, content
        
        front_matter_text = match.group(1)
        html_content = content[match.end():].strip()
        
        # Use YAML parser for robust parsing
        try:
            metadata = yaml.safe_load(front_matter_text) or {}
        except yaml.YAMLError:
            # Fallback to simple parsing
            metadata = self._simple_parse_front_matter(front_matter_text)
        
        return metadata, html_content
    
    def _simple_parse_front_matter(self, text):
        """Simple fallback parser for front matter."""
        metadata = {}
        current_key = None
        current_list = None
        
        for line in text.split('\n'):
            line = line.rstrip()
            if not line.strip():
                continue
            
            # Check for list item
            if line.startswith('  - ') or line.startswith('    - '):
                if current_key and current_list is not None:
                    item = line.strip()[2:].strip()
                    if ': ' in item:
                        # Dict item in list
                        if not current_list or not isinstance(current_list[-1], dict):
                            current_list.append({})
                        key, val = item.split(': ', 1)
                        current_list[-1][key.strip()] = val.strip()
                    else:
                        current_list.append(item)
            elif ': ' in line or line.endswith(':'):
                parts = line.split(': ', 1)
                key = parts[0].strip()
                value = parts[1].strip() if len(parts) > 1 else ''
                
                if value:
                    metadata[key] = value
                    current_key = key
                    current_list = None
                else:
                    # Start of a list
                    current_key = key
                    current_list = []
                    metadata[key] = current_list
        
        return metadata

    def generate_url_from_path(self, filepath, locale):
        """Generate URL path from file path."""
        path = Path(filepath)
        parts = list(path.parts)
        
        # Remove content and locale prefix
        content_idx = None
        for i, p in enumerate(parts):
            if p == 'content':
                content_idx = i
                break
        
        if content_idx is not None:
            parts = parts[content_idx + 1:]
            # Remove locale directory
            if parts and parts[0] == locale:
                parts = parts[1:]
        
        # Handle pages directory
        if parts and parts[0] == 'pages':
            parts = parts[1:]
        
        url_path = '/'.join(parts)
        if url_path.endswith('.html'):
            if url_path == 'index.html':
                url_path = '/'
            else:
                url_path = '/' + url_path[:-5] + '/'
        elif not url_path.startswith('/'):
            url_path = '/' + url_path + '/'
        
        return url_path

    def get_template_name(self, filepath, metadata):
        """Determine which template to use."""
        path_str = str(filepath)
        
        if '/events/' in path_str:
            return 'event.html'
        elif '/initiatives/' in path_str:
            return 'initiative.html'
        elif '/team/' in path_str:
            return 'team_member.html'
        elif '/news/' in path_str:
            return 'news_article.html'
        elif '404' in path_str:
            return '404.html'
        elif 'contact' in path_str:
            return 'contact.html'
        elif 'newsletter' in path_str:
            return 'newsletter.html'
        elif 'index' in path_str:
            return 'home.html'
        else:
            return 'page.html'

    def process_content_file(self, filepath, locale):
        """Process a single content file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata, html_content = self.parse_front_matter(content)
        
        # Add computed fields
        metadata['source_file'] = str(filepath)
        metadata['url'] = self.generate_url_from_path(filepath, locale)
        metadata['locale'] = locale
        
        return metadata, html_content

    def build(self):
        """Build the complete site."""
        output_dir = Path(self.config['build']['output_dir'])
        content_dir = Path(self.config['build']['content_dir'])
        assets_dir = Path(self.config['build']['assets_dir'])
        templates_dir = Path(self.config['build']['templates_dir'])
        default_locale = self.config['site'].get('default_locale', 'en-AU')
        
        # Clean output directory
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)
        
        # Setup Jinja2
        env = Environment(
            loader=FileSystemLoader(templates_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )
        
        # Add globals
        env.globals['config'] = self.config
        env.globals['current_year'] = datetime.now().year
        
        # Process content for default locale
        locale_dir = content_dir / default_locale
        if not locale_dir.exists():
            # Fallback to content root if no locale dirs
            locale_dir = content_dir
        
        # Collect all content
        for content_file in locale_dir.rglob('*.html'):
            if '.gitkeep' in str(content_file):
                continue
                
            metadata, html_content = self.process_content_file(content_file, default_locale)
            
            # Skip news if disabled
            if '/news/' in str(content_file) and not self.config['features'].get('enable_news_section', False):
                continue
            
            # Categorize
            path_str = str(content_file)
            if '/events/' in path_str:
                self.events.append(metadata)
            elif '/news/' in path_str:
                self.news.append(metadata)
            elif '/team/' in path_str:
                self.team.append(metadata)
            elif '/initiatives/' in path_str:
                self.initiatives.append(metadata)
            
            self.pages.append({
                'metadata': metadata,
                'content': html_content,
                'template': self.get_template_name(content_file, metadata)
            })
        
        # Render all pages
        for page_data in self.pages:
            self._render_page(env, output_dir, page_data)
        
        # Build listing pages
        self._build_events_listing(env, output_dir)
        if self.config['features'].get('enable_team_profiles', True):
            self._build_team_listing(env, output_dir)
        if self.config['features'].get('enable_news_section', False):
            self._build_news_listing(env, output_dir)
        
        # Copy assets
        if assets_dir.exists():
            shutil.copytree(assets_dir, output_dir / 'assets')
            print(f"Copied assets to {output_dir / 'assets'}")
        
        # Generate sitemap
        if self.config['build'].get('generate_sitemap', True):
            self._generate_sitemap(output_dir)
        
        # Generate robots.txt
        if self.config['build'].get('generate_robots_txt', True):
            self._generate_robots_txt(output_dir)
        
        # Copy CNAME if configured
        site_url = self.config['site'].get('url', '')
        if site_url and 'github.io' not in site_url:
            domain = site_url.replace('https://', '').replace('http://', '').rstrip('/')
            with open(output_dir / 'CNAME', 'w') as f:
                f.write(domain)
            print(f"Created CNAME: {domain}")
        
        print(f"\nSite built successfully in '{output_dir}'")
        print(f"  - {len(self.pages)} pages")
        print(f"  - {len(self.events)} events")
        print(f"  - {len(self.news)} news articles")
        print(f"  - {len(self.team)} team members")

    def _render_page(self, env, output_dir, page_data):
        """Render a single page."""
        metadata = page_data['metadata']
        html_content = page_data['content']
        template_name = page_data['template']
        
        template = env.get_template(template_name)
        
        # Build context
        context = {
            'page': metadata,
            'content': html_content,
        }
        
        # Add type-specific context
        if template_name == 'event.html':
            context['event'] = metadata
        elif template_name == 'news_article.html':
            context['article'] = metadata
        elif template_name == 'team_member.html':
            context['member'] = metadata
        elif template_name == 'initiative.html':
            context['initiative'] = metadata
        
        rendered = template.render(**context)
        
        # Determine output path
        url = metadata['url']
        if url == '/':
            output_path = output_dir / 'index.html'
        else:
            # Remove leading/trailing slashes and create directory
            clean_path = url.strip('/')
            output_path = output_dir / clean_path / 'index.html'
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered)
        
        print(f"Built: {output_path}")

    def _build_events_listing(self, env, output_dir):
        """Build events listing page."""
        # Sort by date descending
        self.events.sort(key=lambda x: x.get('date', ''), reverse=True)
        
        # Split by status
        today = datetime.now().strftime('%Y-%m-%d')
        upcoming = [e for e in self.events if e.get('status') == 'upcoming' or 
                   (e.get('date', '') >= today and e.get('status') != 'past')]
        past = [e for e in self.events if e.get('status') == 'past' or 
               (e.get('date', '') < today and e.get('status') != 'upcoming')]
        
        template = env.get_template('events_list.html')
        rendered = template.render(
            page={'title': 'Events', 'url': '/events/', 'description': 'Upcoming and past events'},
            upcoming_events=upcoming,
            past_events=past if self.config['features'].get('show_past_events', True) else []
        )
        
        events_dir = output_dir / 'events'
        events_dir.mkdir(exist_ok=True)
        
        with open(events_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(rendered)
        
        print(f"Built: {events_dir / 'index.html'}")

    def _build_team_listing(self, env, output_dir):
        """Build team listing page."""
        template = env.get_template('team_list.html')
        rendered = template.render(
            page={'title': 'Team', 'url': '/team/', 'description': 'Meet our team'},
            team_members=self.team
        )
        
        team_dir = output_dir / 'team'
        team_dir.mkdir(exist_ok=True)
        
        with open(team_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(rendered)
        
        print(f"Built: {team_dir / 'index.html'}")

    def _build_news_listing(self, env, output_dir):
        """Build news listing page."""
        # Sort by date descending
        self.news.sort(key=lambda x: x.get('date', ''), reverse=True)
        
        template = env.get_template('news_list.html')
        rendered = template.render(
            page={'title': 'News', 'url': '/news/', 'description': 'News and announcements'},
            news_articles=self.news
        )
        
        news_dir = output_dir / 'news'
        news_dir.mkdir(exist_ok=True)
        
        with open(news_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(rendered)
        
        print(f"Built: {news_dir / 'index.html'}")

    def _generate_sitemap(self, output_dir):
        """Generate XML sitemap."""
        site_url = self.config['site'].get('url', 'https://example.com').rstrip('/')
        now = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        
        urls = []
        
        # Add all pages
        for page_data in self.pages:
            url = page_data['metadata'].get('url', '/')
            priority = '1.0' if url == '/' else '0.8'
            
            # Determine change frequency
            if '/events/' in url:
                changefreq = 'weekly'
            elif '/news/' in url:
                changefreq = 'weekly'
            else:
                changefreq = 'monthly'
            
            urls.append({
                'loc': urljoin(site_url, url),
                'lastmod': page_data['metadata'].get('date', now),
                'changefreq': changefreq,
                'priority': priority
            })
        
        # Add listing pages
        listing_pages = [
            ('/events/', 'weekly', '0.9'),
            ('/team/', 'monthly', '0.7'),
        ]
        
        if self.config['features'].get('enable_news_section', False):
            listing_pages.append(('/news/', 'weekly', '0.8'))
        
        for url, freq, priority in listing_pages:
            urls.append({
                'loc': urljoin(site_url, url),
                'lastmod': now,
                'changefreq': freq,
                'priority': priority
            })
        
        # Generate XML
        xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        
        for url_data in urls:
            xml_content += '  <url>\n'
            xml_content += f'    <loc>{url_data["loc"]}</loc>\n'
            xml_content += f'    <lastmod>{url_data["lastmod"]}</lastmod>\n'
            xml_content += f'    <changefreq>{url_data["changefreq"]}</changefreq>\n'
            xml_content += f'    <priority>{url_data["priority"]}</priority>\n'
            xml_content += '  </url>\n'
        
        xml_content += '</urlset>'
        
        with open(output_dir / 'sitemap.xml', 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        print(f"Generated: {output_dir / 'sitemap.xml'}")

    def _generate_robots_txt(self, output_dir):
        """Generate robots.txt - open to all crawlers."""
        site_url = self.config['site'].get('url', 'https://example.com').rstrip('/')
        
        robots_content = """# RBO Website Toolkit - robots.txt
# Welcome to all search engines and AI crawlers

User-agent: *
Allow: /

# Sitemap location
Sitemap: {site_url}/sitemap.xml

# Specific crawler welcomes (they'll index anyway, but let's be friendly)
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: DuckDuckBot
Allow: /

User-agent: Slurp
Allow: /

User-agent: Yandex
Allow: /

User-agent: Baiduspider
Allow: /

# AI/LLM crawlers - also welcome
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Anthropic-AI
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: CCBot
Allow: /

User-agent: cohere-ai
Allow: /
""".format(site_url=site_url)
        
        with open(output_dir / 'robots.txt', 'w', encoding='utf-8') as f:
            f.write(robots_content)
        
        print(f"Generated: {output_dir / 'robots.txt'}")


def main():
    """Main entry point."""
    builder = SiteBuilder()
    builder.build()


if __name__ == '__main__':
    main()
```

---

## Development Server with Hot Reload

### toolkit/dev_server.py

```python
#!/usr/bin/env python3
"""
RBO Website Toolkit - Development Server with Hot Reload
Watches for file changes and automatically rebuilds the site.

Usage:
    python toolkit/dev_server.py
    python toolkit/dev_server.py --port 8080
"""

import os
import sys
import time
import argparse
import threading
import http.server
import socketserver
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Import the build module
from build import SiteBuilder


class RebuildHandler(FileSystemEventHandler):
    """Handler that triggers rebuilds on file changes."""
    
    def __init__(self, builder, debounce_seconds=1.0):
        self.builder = builder
        self.debounce_seconds = debounce_seconds
        self.last_build = 0
        self.pending_build = False
        self.lock = threading.Lock()
    
    def on_any_event(self, event):
        # Ignore directory events and hidden files
        if event.is_directory:
            return
        if '/.' in event.src_path or event.src_path.startswith('.'):
            return
        # Ignore site output directory
        if '/site/' in event.src_path:
            return
        
        # Check for relevant file types
        relevant_extensions = {'.html', '.css', '.js', '.json', '.md', '.png', '.jpg', '.jpeg', '.svg'}
        path = Path(event.src_path)
        if path.suffix.lower() not in relevant_extensions:
            return
        
        self._schedule_rebuild(event.src_path)
    
    def _schedule_rebuild(self, changed_path):
        """Schedule a rebuild with debouncing."""
        with self.lock:
            now = time.time()
            if now - self.last_build < self.debounce_seconds:
                self.pending_build = True
                return
            
            self.last_build = now
            self.pending_build = False
        
        print(f"\n--- Change detected: {changed_path}")
        self._do_rebuild()
    
    def _do_rebuild(self):
        """Execute the rebuild."""
        try:
            print("Rebuilding site...")
            start = time.time()
            self.builder.build()
            elapsed = time.time() - start
            print(f"Rebuild complete in {elapsed:.2f}s")
            print("Ready for changes...")
        except Exception as e:
            print(f"Build error: {e}")


class QuietHTTPHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler that suppresses most logging."""
    
    def __init__(self, *args, directory=None, **kwargs):
        self.directory = directory
        super().__init__(*args, directory=directory, **kwargs)
    
    def log_message(self, format, *args):
        # Only log errors
        if args[1].startswith('4') or args[1].startswith('5'):
            super().log_message(format, *args)
    
    def do_GET(self):
        # Handle 404 with custom page
        path = self.translate_path(self.path)
        if not os.path.exists(path):
            # Try adding index.html for directories
            if not path.endswith('/'):
                index_path = path + '/index.html'
                if os.path.exists(index_path):
                    self.path = self.path + '/index.html'
                    return super().do_GET()
            
            # Serve 404 page
            self.send_error(404)
            return
        
        return super().do_GET()


def run_server(port, directory):
    """Run the HTTP server."""
    os.chdir(directory)
    
    handler = lambda *args, **kwargs: QuietHTTPHandler(*args, directory=directory, **kwargs)
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description="Development server with hot reload")
    parser.add_argument('--port', '-p', type=int, default=8000, help="Port to serve on")
    parser.add_argument('--no-watch', action='store_true', help="Disable file watching")
    args = parser.parse_args()
    
    # Initial build
    print("Performing initial build...")
    builder = SiteBuilder()
    builder.build()
    
    output_dir = Path(builder.config['build']['output_dir']).resolve()
    
    if not args.no_watch:
        # Setup file watcher
        handler = RebuildHandler(SiteBuilder())  # Fresh builder for each rebuild
        observer = Observer()
        
        # Watch content, assets, and templates
        watch_paths = ['content', 'assets', 'toolkit/templates']
        for watch_path in watch_paths:
            if os.path.exists(watch_path):
                observer.schedule(handler, watch_path, recursive=True)
                print(f"Watching: {watch_path}")
        
        observer.start()
    
    # Run server
    try:
        print(f"\n{'='*50}")
        print(f"Development server starting...")
        print(f"{'='*50}\n")
        run_server(args.port, str(output_dir))
    except KeyboardInterrupt:
        print("\nShutting down...")
        if not args.no_watch:
            observer.stop()
            observer.join()


if __name__ == '__main__':
    main()
```

---

## Content Validation Script

### toolkit/validate.py

```python
#!/usr/bin/env python3
"""
RBO Website Toolkit - Content Validation
Validates content files, configuration, and checks for common issues.

Usage:
    python toolkit/validate.py
    python toolkit/validate.py --fix  # Auto-fix some issues
    python toolkit/validate.py --strict  # Fail on warnings
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse


class ValidationError:
    def __init__(self, file, message, line=None, severity='error'):
        self.file = file
        self.message = message
        self.line = line
        self.severity = severity  # 'error', 'warning', 'info'
    
    def __str__(self):
        loc = f"{self.file}"
        if self.line:
            loc += f":{self.line}"
        return f"[{self.severity.upper()}] {loc}: {self.message}"


class ContentValidator:
    def __init__(self, config_path="content/config.json"):
        self.errors = []
        self.warnings = []
        self.config = self._load_config(config_path)
        self.config_path = config_path
    
    def _load_config(self, config_path):
        """Load and validate configuration."""
        if not os.path.exists(config_path):
            self.errors.append(ValidationError(
                config_path, 
                "Configuration file not found"
            ))
            return {}
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(ValidationError(
                config_path,
                f"Invalid JSON: {e}"
            ))
            return {}
    
    def validate_all(self):
        """Run all validation checks."""
        print("Validating RBO Website Toolkit content...\n")
        
        self._validate_config()
        self._validate_content_files()
        self._validate_assets()
        self._validate_links()
        self._validate_accessibility()
        
        return self._report()
    
    def _validate_config(self):
        """Validate configuration file."""
        print("Checking configuration...")
        
        if not self.config:
            return
        
        # Required fields
        required_paths = [
            ('site.name', str),
            ('site.url', str),
            ('site.default_locale', str),
            ('organization.rbo_name', str),
            ('contact.linkedin_page', str),
            ('branding.logo', str),
        ]
        
        for path, expected_type in required_paths:
            value = self._get_nested(self.config, path)
            if value is None:
                self.errors.append(ValidationError(
                    self.config_path,
                    f"Missing required field: {path}"
                ))
            elif not isinstance(value, expected_type):
                self.errors.append(ValidationError(
                    self.config_path,
                    f"Invalid type for {path}: expected {expected_type.__name__}"
                ))
        
        # Validate URL format
        site_url = self._get_nested(self.config, 'site.url')
        if site_url:
            parsed = urlparse(site_url)
            if not parsed.scheme or not parsed.netloc:
                self.errors.append(ValidationError(
                    self.config_path,
                    f"Invalid site URL: {site_url}"
                ))
        
        # Validate navigation
        nav = self._get_nested(self.config, 'navigation')
        if nav:
            for item in nav:
                if 'label' not in item or 'url' not in item:
                    self.errors.append(ValidationError(
                        self.config_path,
                        f"Navigation item missing label or url: {item}"
                    ))
        
        # Check sponsor images exist
        sponsors = self._get_nested(self.config, 'sponsors.items') or []
        for sponsor in sponsors:
            logo_path = sponsor.get('logo', '')
            if logo_path:
                full_path = Path('assets') / logo_path.lstrip('/')
                # Adjust for assets prefix in path
                if logo_path.startswith('/assets/'):
                    full_path = Path(logo_path.lstrip('/'))
                if not full_path.exists():
                    self.warnings.append(ValidationError(
                        self.config_path,
                        f"Sponsor logo not found: {logo_path}",
                        severity='warning'
                    ))
    
    def _validate_content_files(self):
        """Validate all content files."""
        print("Checking content files...")
        
        content_dir = Path(self.config.get('build', {}).get('content_dir', 'content'))
        
        for html_file in content_dir.rglob('*.html'):
            self._validate_content_file(html_file)
    
    def _validate_content_file(self, filepath):
        """Validate a single content file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(ValidationError(
                str(filepath),
                f"Cannot read file: {e}"
            ))
            return
        
        # Check for front matter
        if not content.strip().startswith('<!--'):
            self.warnings.append(ValidationError(
                str(filepath),
                "No front matter found (should start with <!--)",
                severity='warning'
            ))
            return
        
        # Extract and validate front matter
        match = re.search(r'<!--\s*(.*?)\s*-->', content, re.DOTALL)
        if not match:
            self.errors.append(ValidationError(
                str(filepath),
                "Malformed front matter (unclosed comment)"
            ))
            return
        
        front_matter = match.group(1)
        
        # Required fields based on content type
        path_str = str(filepath)
        
        if '/events/' in path_str:
            required = ['title', 'date', 'status']
            for field in required:
                if f'{field}:' not in front_matter:
                    self.errors.append(ValidationError(
                        str(filepath),
                        f"Event missing required field: {field}"
                    ))
            
            # Validate date format
            date_match = re.search(r'date:\s*(\S+)', front_matter)
            if date_match:
                date_str = date_match.group(1)
                try:
                    datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    self.errors.append(ValidationError(
                        str(filepath),
                        f"Invalid date format: {date_str} (expected YYYY-MM-DD)"
                    ))
            
            # Validate status
            status_match = re.search(r'status:\s*(\S+)', front_matter)
            if status_match:
                status = status_match.group(1)
                if status not in ['upcoming', 'past']:
                    self.warnings.append(ValidationError(
                        str(filepath),
                        f"Unexpected event status: {status}",
                        severity='warning'
                    ))
        
        elif '/news/' in path_str:
            required = ['title', 'date']
            for field in required:
                if f'{field}:' not in front_matter:
                    self.errors.append(ValidationError(
                        str(filepath),
                        f"News article missing required field: {field}"
                    ))
        
        elif '/team/' in path_str:
            required = ['name', 'title', 'organization']
            for field in required:
                if f'{field}:' not in front_matter:
                    self.warnings.append(ValidationError(
                        str(filepath),
                        f"Team member missing field: {field}",
                        severity='warning'
                    ))
        
        # Check for title in all content
        if 'title:' not in front_matter and '/pages/' in path_str:
            self.warnings.append(ValidationError(
                str(filepath),
                "Page missing title field",
                severity='warning'
            ))
        
        # Check HTML content
        html_content = content[match.end():].strip()
        if not html_content:
            self.warnings.append(ValidationError(
                str(filepath),
                "No HTML content after front matter",
                severity='warning'
            ))
    
    def _validate_assets(self):
        """Validate asset files."""
        print("Checking assets...")
        
        assets_dir = Path(self.config.get('build', {}).get('assets_dir', 'assets'))
        
        # Check required directories
        required_dirs = ['css', 'images', 'js']
        for dir_name in required_dirs:
            dir_path = assets_dir / dir_name
            if not dir_path.exists():
                self.warnings.append(ValidationError(
                    str(dir_path),
                    f"Recommended directory missing: {dir_name}",
                    severity='warning'
                ))
        
        # Check for required CSS files
        required_css = ['style.css', 'responsive.css']
        for css_file in required_css:
            css_path = assets_dir / 'css' / css_file
            if not css_path.exists():
                self.errors.append(ValidationError(
                    str(css_path),
                    f"Required CSS file missing: {css_file}"
                ))
        
        # Check logo exists
        logo_path = self._get_nested(self.config, 'branding.logo')
        if logo_path:
            full_path = Path(logo_path.lstrip('/'))
            if not full_path.exists():
                self.errors.append(ValidationError(
                    str(full_path),
                    f"Logo file not found: {logo_path}"
                ))
    
    def _validate_links(self):
        """Check for broken internal links."""
        print("Checking internal links...")
        
        content_dir = Path(self.config.get('build', {}).get('content_dir', 'content'))
        
        # Collect all valid URLs
        valid_urls = {'/'}
        for html_file in content_dir.rglob('*.html'):
            # Generate URL from path
            rel_path = html_file.relative_to(content_dir)
            parts = list(rel_path.parts)
            
            # Remove locale prefix if present
            if parts and re.match(r'^[a-z]{2}-[A-Z]{2}$', parts[0]):
                parts = parts[1:]
            
            # Remove 'pages' prefix
            if parts and parts[0] == 'pages':
                parts = parts[1:]
            
            url_path = '/'.join(parts)
            if url_path.endswith('.html'):
                if url_path == 'index.html':
                    valid_urls.add('/')
                else:
                    valid_urls.add('/' + url_path[:-5] + '/')
        
        # Add standard listing pages
        valid_urls.update(['/events/', '/team/', '/news/', '/initiatives/', '/contact/', '/about/', '/newsletter/'])
        
        # Check links in content
        for html_file in content_dir.rglob('*.html'):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all href links
            links = re.findall(r'href=["\']([^"\']+)["\']', content)
            
            for link in links:
                # Skip external links and anchors
                if link.startswith('http') or link.startswith('#') or link.startswith('mailto:'):
                    continue
                
                # Normalize link
                normalized = link.rstrip('/') + '/' if not link.endswith('/') else link
                if normalized == '//' or not normalized.startswith('/'):
                    continue
                
                # Check if valid
                if normalized not in valid_urls and not link.startswith('/assets/'):
                    self.warnings.append(ValidationError(
                        str(html_file),
                        f"Potentially broken link: {link}",
                        severity='warning'
                    ))
    
    def _validate_accessibility(self):
        """Check for basic accessibility issues."""
        print("Checking accessibility...")
        
        content_dir = Path(self.config.get('build', {}).get('content_dir', 'content'))
        
        for html_file in content_dir.rglob('*.html'):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check images have alt text
            img_tags = re.findall(r'<img[^>]*>', content)
            for img in img_tags:
                if 'alt=' not in img:
                    self.warnings.append(ValidationError(
                        str(html_file),
                        f"Image missing alt attribute: {img[:50]}...",
                        severity='warning'
                    ))
            
            # Check for empty links
            empty_links = re.findall(r'<a[^>]*>\s*</a>', content)
            for link in empty_links:
                if 'aria-label' not in link:
                    self.warnings.append(ValidationError(
                        str(html_file),
                        f"Empty link without aria-label: {link}",
                        severity='warning'
                    ))
    
    def _get_nested(self, obj, path):
        """Get nested dictionary value by dot-notation path."""
        keys = path.split('.')
        for key in keys:
            if isinstance(obj, dict) and key in obj:
                obj = obj[key]
            else:
                return None
        return obj
    
    def _report(self):
        """Generate validation report."""
        print("\n" + "="*60)
        print("VALIDATION REPORT")
        print("="*60)
        
        if self.errors:
            print(f"\nERRORS ({len(self.errors)}):")
            print("-"*40)
            for error in self.errors:
                print(f"  {error}")
        
        if self.warnings:
            print(f"\nWARNINGS ({len(self.warnings)}):")
            print("-"*40)
            for warning in self.warnings:
                print(f"  {warning}")
        
        print("\n" + "="*60)
        
        if self.errors:
            print(f"FAILED: {len(self.errors)} errors, {len(self.warnings)} warnings")
            return False
        elif self.warnings:
            print(f"PASSED with {len(self.warnings)} warnings")
            return True
        else:
            print("PASSED: All checks passed!")
            return True


def main():
    parser = argparse.ArgumentParser(description="Validate RBO Website content")
    parser.add_argument('--strict', action='store_true', help="Fail on warnings")
    parser.add_argument('--config', default='content/config.json', help="Path to config file")
    args = parser.parse_args()
    
    validator = ContentValidator(args.config)
    success = validator.validate_all()
    
    if args.strict and validator.warnings:
        print("\nStrict mode: treating warnings as errors")
        success = False
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
```

---

## Agent Instructions for Post-Event Updates

### agent_instructions/update_event_post.md

```markdown
# Updating an Event Page After the Event

## Overview
After an event has concluded, update the event page to:
1. Change status from "upcoming" to "past"
2. Add recording link (if available)
3. Add presentation slides (if available)
4. Add event photos (if available)
5. Add any additional resources

## Step-by-Step Process

### Step 1: Locate the Event File

Find the event file in `content/[locale]/events/`:
```bash
ls content/en-AU/events/
```

### Step 2: Update the Front Matter

Open the event file and update these fields:

```html
<!--
title: [Keep existing]
date: [Keep existing]
...

# CHANGE THIS:
status: past

# ADD THESE (as applicable):
recording_url: https://www.youtube.com/watch?v=xxxxx
recording_embed_url: https://www.youtube.com/embed/xxxxx
recording_platform: YouTube
slides_url: /assets/downloads/event-name-slides.pdf

# For multiple resources:
resources:
  - title: Presentation Slides
    url: /assets/downloads/slides.pdf
  - title: Workshop Materials
    url: /assets/downloads/workshop.pdf
  - title: Reference Guide
    url: /assets/downloads/guide.pdf

# For photos:
photos_gallery: true
photos:
  - url: /assets/images/events/event-name/photo1.jpg
    caption: Opening keynote presentation
  - url: /assets/images/events/event-name/photo2.jpg
    caption: Interactive workshop session
  - url: /assets/images/events/event-name/photo3.jpg
    caption: Networking break
-->
```

### Step 3: Upload Resources

1. **Slides/Documents**: Save to `assets/downloads/`
   ```bash
   cp ~/Downloads/presentation.pdf assets/downloads/event-name-slides.pdf
   ```

2. **Photos**: Create event photo directory and add images
   ```bash
   mkdir -p assets/images/events/event-name/
   cp ~/Downloads/photos/*.jpg assets/images/events/event-name/
   ```

### Step 4: Video Embedding

For YouTube videos:
- Recording URL: `https://www.youtube.com/watch?v=VIDEO_ID`
- Embed URL: `https://www.youtube.com/embed/VIDEO_ID`

For BrightTalk:
- Just provide the webcast URL; template will show as a link

For other platforms:
- Provide the recording_url and recording_platform name

### Step 5: Build and Preview

```bash
# Build the site
python toolkit/build.py

# Preview locally
python toolkit/dev_server.py
# Open http://localhost:8000/events/event-name/
```

### Step 6: Verify the Page

Check that:
- [ ] Status badge shows "Past Event"
- [ ] Recording section appears (if recording_url set)
- [ ] Video embeds correctly (for YouTube)
- [ ] Resources section appears (if slides/resources set)
- [ ] Photo gallery displays (if photos set)
- [ ] Registration button is hidden
- [ ] All links work correctly

### Step 7: Commit and Push

```bash
git add content/en-AU/events/event-name.html
git add assets/downloads/
git add assets/images/events/event-name/
git commit -m "Update event: Event Name - add recording and materials"
git push
```

## Example: Complete Post-Event Update

Before (upcoming event):
```html
<!--
title: Digital Twins in Healthcare Summit
date: 2024-11-20
status: upcoming
registration_url: https://brighttalk.com/webcast/12345
...
-->
```

After (past event with all materials):
```html
<!--
title: Digital Twins in Healthcare Summit
date: 2024-11-20
status: past
recording_url: https://www.youtube.com/watch?v=abc123
recording_embed_url: https://www.youtube.com/embed/abc123
recording_platform: YouTube
slides_url: /assets/downloads/healthcare-summit-2024-slides.pdf
resources:
  - title: Case Study Handout
    url: /assets/downloads/healthcare-case-study.pdf
  - title: Implementation Checklist
    url: /assets/downloads/implementation-checklist.pdf
photos_gallery: true
photos:
  - url: /assets/images/events/healthcare-summit-2024/keynote.jpg
    caption: Dr. Smith delivering the opening keynote
  - url: /assets/images/events/healthcare-summit-2024/workshop.jpg
    caption: Hands-on workshop session
...
-->
```

## Notes

- The template automatically hides the registration button for past events
- YouTube videos are embedded directly; other platforms show as links
- Photos are lazy-loaded for performance
- Resources appear in the order listed
```

---

## Versioning & Update Guide

### UPDATING.md

```markdown
# Updating the RBO Website Toolkit

This guide explains how to update your site when the upstream RBO Website Toolkit receives updates.

## Understanding What to Update

The toolkit is designed with clear separation:

### Files You CAN Customize (Your Content)
- `content/` - All your pages, events, news, team profiles
- `assets/images/` - Your images, logos, photos
- `assets/downloads/` - Your downloadable resources
- `content/config.json` - Your site configuration

### Files You Should NOT Edit (Toolkit Core)
- `toolkit/` - Build scripts, templates, validation
- `.github/workflows/` - Deployment automation
- `agent_instructions/` - AI agent guides

## Update Process

### For Fork-Based Setup

1. **Add upstream remote** (first time only):
   ```bash
   git remote add upstream https://github.com/dtc-rbo/website-toolkit.git
   ```

2. **Fetch upstream changes**:
   ```bash
   git fetch upstream
   ```

3. **Review changes**:
   ```bash
   git log upstream/main --oneline -10
   ```

4. **Merge updates**:
   ```bash
   git merge upstream/main
   ```

5. **Resolve any conflicts**:
   - Conflicts in `toolkit/` - Keep upstream version
   - Conflicts in `content/` - Keep your version
   - Conflicts in `config.json` - Merge manually (keep your values, add new fields)

6. **Test locally**:
   ```bash
   python toolkit/validate.py
   python toolkit/dev_server.py
   ```

7. **Push updates**:
   ```bash
   git push origin main
   ```

### For Submodule-Based Setup

1. **Update submodule**:
   ```bash
   cd toolkit
   git fetch origin
   git checkout main
   git pull
   cd ..
   ```

2. **Commit submodule update**:
   ```bash
   git add toolkit
   git commit -m "Update toolkit to latest version"
   git push
   ```

## Handling Breaking Changes

Occasionally, toolkit updates may include breaking changes. These will be documented in the toolkit's CHANGELOG.md.

### Common Breaking Changes

1. **New required config fields**:
   - Add the new fields to your `config.json`
   - Check `config.json` in upstream for default values

2. **Template changes**:
   - If you've customized templates (not recommended), merge changes manually
   - Consider moving customizations to CSS instead

3. **New dependencies**:
   - Run `pip install -r toolkit/requirements.txt`

## Version Compatibility

Check your toolkit version:
```bash
cat toolkit/VERSION
```

The toolkit follows semantic versioning:
- **Major** (1.0.0 -> 2.0.0): Breaking changes, manual migration may be needed
- **Minor** (1.0.0 -> 1.1.0): New features, backward compatible
- **Patch** (1.0.0 -> 1.0.1): Bug fixes, no action needed

## Getting Help

If you encounter issues during updates:

1. Check the toolkit's CHANGELOG.md for migration notes
2. Run validation: `python toolkit/validate.py`
3. Check GitHub Issues on the toolkit repository
4. Contact the DTC RBO support channel
```

### CUSTOMIZATION.md

```markdown
# Customizing Your RBO Website

This guide explains what you can safely customize and how.

## Safe Customizations

### 1. Site Configuration (`content/config.json`)

All site settings are in one file:

```json
{
  "site": {
    "name": "Your RBO Name",
    "short_name": "DTC YourRegion",
    "tagline": "Your tagline here"
    // ... more settings
  }
}
```

### 2. Content Pages (`content/[locale]/`)

Add, edit, or remove:
- Pages in `pages/`
- Events in `events/`
- Team members in `team/`
- News articles in `news/`
- Initiatives in `initiatives/`

### 3. Images and Assets (`assets/`)

Replace or add:
- Logo: `assets/images/dtc-logo.png` or update path in config
- Sponsor logos: `assets/images/sponsors/`
- Team photos: `assets/images/team/`
- Event images: `assets/images/events/`

### 4. Colors and Branding

In `content/config.json`:
```json
{
  "branding": {
    "primary_color": "#0066CC",
    "secondary_color": "#003366",
    "accent_color": "#00AAFF"
  }
}
```

For advanced CSS customizations, create:
`assets/css/custom.css`

Then add to your `content/config.json`:
```json
{
  "build": {
    "custom_css": "/assets/css/custom.css"
  }
}
```

## What NOT to Customize

### Toolkit Core (`toolkit/`)

These files receive updates from upstream:
- `toolkit/build.py`
- `toolkit/templates/*.html`
- `toolkit/validate.py`

If you need template changes:
1. First, check if CSS can achieve what you need
2. If not, open an issue on the toolkit repo
3. As last resort, customize but document changes

### GitHub Workflows (`.github/workflows/`)

These ensure proper deployment. Only modify if you understand GitHub Actions.

## Adding New Features

### New Page Type

1. Create content file: `content/en-AU/pages/new-page.html`
2. Add to navigation in `config.json`
3. Build and test

### New Navigation Item

```json
{
  "navigation": [
    // ... existing items
    {"label": "New Page", "url": "/new-page/"}
  ]
}
```

### Dropdown Navigation

```json
{
  "navigation": [
    {
      "label": "Resources",
      "url": "/resources/",
      "children": [
        {"label": "Whitepapers", "url": "/resources/whitepapers/"},
        {"label": "Case Studies", "url": "/resources/case-studies/"}
      ]
    }
  ]
}
```

## Disabling Features

```json
{
  "features": {
    "enable_news_section": false,
    "enable_newsletter_page": false,
    "show_sponsors_footer": false
  }
}
```
```

---

## Additional CSS for Accessibility and New Features

### assets/css/accessibility.css

```css
/* Accessibility Enhancements */

/* Skip to content link */
.skip-link {
    position: absolute;
    top: -100px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--primary-color);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 0 0 var(--border-radius) var(--border-radius);
    z-index: 9999;
    text-decoration: none;
    font-weight: 500;
    transition: top 0.2s ease;
}

.skip-link:focus {
    top: 0;
    outline: 3px solid var(--accent-color);
    outline-offset: 2px;
}

/* Focus indicators */
a:focus,
button:focus,
input:focus,
select:focus,
textarea:focus {
    outline: 3px solid var(--accent-color);
    outline-offset: 2px;
}

/* Remove outline for mouse users */
a:focus:not(:focus-visible),
button:focus:not(:focus-visible) {
    outline: none;
}

/* Ensure focus-visible works */
a:focus-visible,
button:focus-visible {
    outline: 3px solid var(--accent-color);
    outline-offset: 2px;
}

/* Screen reader only content */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}

/* High contrast mode support */
@media (prefers-contrast: high) {
    :root {
        --primary-color: #0000EE;
        --text-color: #000000;
        --background: #FFFFFF;
        --border-color: #000000;
    }
    
    a {
        text-decoration: underline;
    }
    
    .btn {
        border-width: 3px;
    }
}

/* Minimum touch target size */
.btn,
.nav-item a,
.social-links a {
    min-height: 44px;
    min-width: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

/* Ensure sufficient color contrast */
.text-light,
.event-card-date,
.speaker-title,
.registration-note {
    color: #595959; /* Meets WCAG AA for normal text on white */
}

/* Video container for responsive embeds */
.video-container {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    overflow: hidden;
    max-width: 100%;
    margin: 1rem 0;
}

.video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
}
```

### Additional styles for new features (append to style.css)

```css
/* Sponsor Logos */
.footer-sponsors {
    padding: 2rem 0;
    border-top: 1px solid rgba(255,255,255,0.2);
    margin-top: 2rem;
}

.footer-sponsors h3 {
    text-align: center;
    margin-bottom: 1.5rem;
}

.sponsor-logos {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 2rem;
}

.sponsor-link {
    display: block;
    opacity: 0.8;
    transition: opacity 0.2s ease;
}

.sponsor-link:hover {
    opacity: 1;
}

.sponsor-logo {
    max-height: 50px;
    max-width: 150px;
    width: auto;
    filter: brightness(0) invert(1); /* White logos in footer */
}

.sponsor-platinum .sponsor-logo {
    max-height: 60px;
    max-width: 180px;
}

/* Homepage sponsor section (if needed) */
.homepage-sponsors .sponsor-logo {
    filter: none;
    max-height: 40px;
}

/* Event Status Badges */
.event-status-badge {
    margin-bottom: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    font-size: 0.875rem;
    font-weight: 500;
    border-radius: 100px;
}

.badge-upcoming {
    background: #E8F5E9;
    color: #2E7D32;
}

.badge-past {
    background: var(--background-alt);
    color: var(--text-light);
}

/* Event Recording Section */
.event-recording {
    margin: 2rem 0;
    padding: 1.5rem;
    background: var(--background-alt);
    border-radius: var(--border-radius);
}

.event-recording h2 {
    margin-bottom: 1rem;
}

/* Event Resources Section */
.event-resources {
    margin: 2rem 0;
}

.resource-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.resource-list li {
    margin-bottom: 0.75rem;
}

.resource-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--background-alt);
    border-radius: var(--border-radius);
    transition: background 0.2s ease;
}

.resource-link:hover {
    background: var(--border-color);
    text-decoration: none;
}

/* Photo Gallery */
.event-photos {
    margin: 2rem 0;
}

.photo-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
}

.gallery-item {
    margin: 0;
}

.gallery-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: var(--border-radius);
}

.gallery-item figcaption {
    font-size: 0.875rem;
    color: var(--text-light);
    margin-top: 0.5rem;
}

/* News Section */
.news-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.news-card {
    background: var(--background);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    overflow: hidden;
    transition: box-shadow 0.2s ease;
}

.news-card:hover {
    box-shadow: var(--shadow-md);
}

.news-card-image {
    width: 100%;
    height: 180px;
    object-fit: cover;
}

.news-card-content {
    padding: 1.25rem;
}

.news-card-date {
    font-size: 0.875rem;
    color: var(--text-light);
    margin-bottom: 0.5rem;
    display: block;
}

.news-card-title {
    font-size: 1.125rem;
    margin-bottom: 0.75rem;
}

.news-card-title a {
    color: var(--text-color);
}

.news-card-title a:hover {
    color: var(--primary-color);
}

.news-card-excerpt {
    font-size: 0.9375rem;
    color: var(--text-light);
    margin-bottom: 0.75rem;
}

.read-more {
    font-size: 0.875rem;
    font-weight: 500;
}

/* Newsletter Page */
.newsletter-page {
    max-width: var(--content-width);
    margin: 0 auto;
}

.connect-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.connect-card {
    padding: 2rem;
    background: var(--background-alt);
    border-radius: var(--border-radius);
    text-align: center;
}

.connect-card.primary-connect {
    background: var(--primary-color);
    color: white;
}

.connect-card.primary-connect h2 {
    color: white;
}

.connect-card.primary-connect .btn-primary {
    background: white;
    color: var(--primary-color);
    border-color: white;
}

.connect-card.primary-connect .btn-primary:hover {
    background: var(--background-alt);
    color: var(--primary-color);
}

.connect-icon {
    margin-bottom: 1rem;
    color: white;
}

.connect-card h2 {
    margin-bottom: 1rem;
}

.connect-card p {
    margin-bottom: 1.5rem;
}

/* 404 Error Page */
.error-page {
    text-align: center;
    padding: 4rem 1rem;
    max-width: 600px;
    margin: 0 auto;
}

.error-code {
    font-size: 6rem;
    font-weight: 700;
    color: var(--border-color);
    margin: 1rem 0;
    line-height: 1;
}

.error-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin: 2rem 0;
    flex-wrap: wrap;
}

.error-help {
    text-align: left;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border-color);
}

.error-help ul {
    list-style: none;
    padding: 0;
}

.error-help li {
    margin-bottom: 0.5rem;
}

/* Dropdown Navigation */
.nav-item.has-dropdown {
    position: relative;
}

.dropdown-arrow {
    font-size: 0.75rem;
    margin-left: 0.25rem;
    transition: transform 0.2s ease;
}

.dropdown-arrow::after {
    content: '\25BC';
}

.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    min-width: 200px;
    background: var(--background);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-md);
    padding: 0.5rem 0;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.2s ease;
    list-style: none;
    margin: 0;
    z-index: 100;
}

.nav-item.has-dropdown:hover .dropdown-menu,
.nav-item.has-dropdown:focus-within .dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.dropdown-menu a {
    display: block;
    padding: 0.5rem 1rem;
    color: var(--text-color);
}

.dropdown-menu a:hover {
    background: var(--background-alt);
    text-decoration: none;
}

/* Empty State */
.empty-state {
    text-align: center;
    padding: 3rem 1rem;
    color: var(--text-light);
}

.empty-state p {
    margin-bottom: 1rem;
}
```

---

## Updated Python Dependencies

### toolkit/requirements.txt

```
jinja2>=3.1.0
pyyaml>=6.0
python-dotenv>=1.0.0
openai>=1.0.0
requests>=2.31.0
beautifulsoup4>=4.12.0
Pillow>=10.0.0
watchdog>=3.0.0
```

---

## GitHub Actions Validation Workflow

### .github/workflows/validate.yml

```yaml
name: Validate Content

on:
  pull_request:
    branches: [main]
    paths:
      - 'content/**'
      - 'assets/**'
  push:
    branches: [main]
    paths:
      - 'content/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r toolkit/requirements.txt
      
      - name: Run validation
        run: python toolkit/validate.py --strict
      
      - name: Test build
        run: python toolkit/build.py
```

---

## Summary of Additions

This v2.0 specification adds:

| Feature | Description |
|---------|-------------|
| **SEO** | Sitemap.xml generation, robots.txt (AI-crawler friendly), JSON-LD structured data |
| **Validation** | `validate.py` script with front matter checking, link validation, accessibility checks |
| **Dev Server** | Hot reload development server with file watching |
| **i18n Structure** | Locale directories (en-AU, ja-JP) ready for future internationalization |
| **Event Lifecycle** | Unified event template handling upcoming/past states, recordings, slides, photos |
| **News Section** | Optional news/announcements feature (disabled by default) |
| **Sponsors** | Partner logo section in footer and homepage |
| **Newsletter Page** | LinkedIn-focused follow page template |
| **404 Page** | Custom error page |
| **Accessibility** | WCAG 2.1 AA considerations, skip links, focus indicators, reduced motion |
| **Versioning Docs** | UPDATING.md and CUSTOMIZATION.md guides |

The specification is now comprehensive and ready for implementation.