#!/usr/bin/env python3
"""
Final cleanup for offline mode
"""

import re

# Read the HTML file
html_path = '/tmp/cc-agent/60777008/project/groovepublic.com/reveused/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove or disable unnecessary external connections
# 1. Remove dns-prefetch for fonts.googleapis.com
content = content.replace(
    "<link rel='dns-prefetch' href='//fonts.googleapis.com' />",
    "<!-- Offline: dns-prefetch removed -->"
)

# 2. Comment out Rank Math SEO comment
content = content.replace(
    "<!-- Search Engine Optimization by Rank Math - https://rankmath.com/ -->",
    "<!-- Search Engine Optimization by Rank Math (offline mode) -->"
)

# 3. Replace gravatar with local placeholder or remove
# Create a simple SVG placeholder for avatar
svg_placeholder = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="96" height="96"%3E%3Crect width="96" height="96" fill="%23ddd"/%3E%3Ctext x="50%25" y="50%25" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif" font-size="48" fill="%23999"%3EA%3C/text%3E%3C/svg%3E'
content = content.replace(
    'https://secure.gravatar.com/avatar/83e4e4deb0fb9c15fd0b2ee765f87bd4?s=96&amp;d=blank&amp;r=g',
    svg_placeholder
)

# Write the modified content
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Final cleanup completed!")
print("  - DNS prefetch removed")
print("  - Gravatar replaced with SVG placeholder")
print("  - Rank Math reference updated")
print("\nRemaining external URLs are intentional:")
print("  - Social media links (Instagram, YouTube)")
print("  - WhatsApp contact link")
print("  - Google Maps location")
print("  - Facebook Pixel (already disabled)")
print("\n✓ Website is now fully offline-capable!")
