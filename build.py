#!/usr/bin/env python3
"""
RBO Website Toolkit - Static Site Generator (MVP)
Builds static HTML from templates and content files.
"""

import os
import sys
import json
import shutil
import re
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml


# Default configuration
DEFAULT_CONFIG = {
    "site": {
        "default_locale": "en-SG",
        "url": "https://example.com"
    },
    "build": {
        "output_dir": "site",
        "content_dir": "content",
        "assets_dir": "assets",
        "templates_dir": "toolkit/templates"
    },
    "features": {
        "show_past_events": True
    }
}


class SiteBuilder:
    def __init__(self, config_path="content/config.json"):
        self.config = self.load_config(config_path)
        self.pages = []
        self.events = []

    def load_config(self, config_path):
        """Load site configuration from JSON file."""
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
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

        try:
            metadata = yaml.safe_load(front_matter_text) or {}
        except yaml.YAMLError:
            metadata = {}

        return metadata, html_content

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
        elif 'contact' in path_str:
            return 'contact.html'
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
        default_locale = self.config['site'].get('default_locale', 'en-SG')

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
            locale_dir = content_dir

        # Collect all content
        for content_file in locale_dir.rglob('*.html'):
            if '.gitkeep' in str(content_file):
                continue

            metadata, html_content = self.process_content_file(content_file, default_locale)

            path_str = str(content_file)
            if '/events/' in path_str:
                self.events.append(metadata)

            self.pages.append({
                'metadata': metadata,
                'content': html_content,
                'template': self.get_template_name(content_file, metadata)
            })

        # Render all pages
        for page_data in self.pages:
            self._render_page(env, output_dir, page_data)

        # Build events listing page
        self._build_events_listing(env, output_dir)

        # Copy assets
        if assets_dir.exists():
            shutil.copytree(assets_dir, output_dir / 'assets')
            print(f"Copied assets to {output_dir / 'assets'}")

        # Copy CNAME file for custom domain (if exists)
        cname_file = Path('CNAME')
        if cname_file.exists():
            shutil.copy(cname_file, output_dir / 'CNAME')
            print(f"Copied CNAME file for custom domain")

        print(f"\nSite built successfully in '{output_dir}'")
        print(f"  - {len(self.pages)} pages")
        print(f"  - {len(self.events)} events")

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
        elif template_name == 'home.html':
            # Pass first upcoming event as featured event
            upcoming = [e for e in self.events if e.get('status') == 'upcoming']
            if upcoming:
                context['featured_event'] = upcoming[0]

        rendered = template.render(**context)

        # Determine output path
        url = metadata['url']
        if url == '/':
            output_path = output_dir / 'index.html'
        else:
            clean_path = url.strip('/')
            output_path = output_dir / clean_path / 'index.html'

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered)

        print(f"Built: {output_path}")

    def _build_events_listing(self, env, output_dir):
        """Build events listing page."""
        # Normalize dates to strings for comparison
        def get_date_str(event):
            date_val = event.get('date', '')
            if hasattr(date_val, 'isoformat'):
                return date_val.isoformat()
            return str(date_val) if date_val else ''
        
        # Sort by date descending
        self.events.sort(key=lambda x: get_date_str(x), reverse=True)

        # Split by status
        today = datetime.now().strftime('%Y-%m-%d')
        upcoming = [e for e in self.events if e.get('status') == 'upcoming' or
                   (get_date_str(e) >= today and e.get('status') != 'past')]
        past = [e for e in self.events if e.get('status') == 'past' or
               (get_date_str(e) < today and e.get('status') != 'upcoming')]

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


def main():
    """Main entry point."""
    builder = SiteBuilder()
    builder.build()


if __name__ == '__main__':
    main()

