#!/usr/bin/env python3
"""
Script to make groovepublic.com wedding invitation fully offline
by replacing all external URLs with local paths
"""

import re

# Read the HTML file
html_path = '/tmp/cc-agent/60777008/project/groovepublic.com/reveused/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Backup original
with open(html_path + '.backup', 'w', encoding='utf-8') as f:
    f.write(content)

# Define replacements (external URL -> local path)
# Path relatif dari /groovepublic.com/reveused/ ke root project adalah ../..
replacements = {
    # CDN Libraries
    'https://cdn.jsdelivr.net/npm/aos@2.3.1/dist/': '../../cdn.jsdelivr.net/npm/aos@2.3.1/dist/',
    'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/': '../../cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/',
    'https://code.jquery.com/': '../../code.jquery.com/',

    # Google Fonts
    'https://fonts.googleapis.com/css2?family=Inter': '../../fonts.googleapis.com/css2.css',
    'https://fonts.googleapis.com/css?family=Roboto': '../../fonts.googleapis.com/css.css',
    'https://fonts.googleapis.com/css2?family=Hanken+Grotesk': '../../fonts.googleapis.com/css2-b940eaaab1e59.css',

    # CloudHost fonts and MP3
    'https://is3.cloudhost.id/externalgroovepublic/': '../../is3.cloudhost.id/externalgroovepublic/',
}

# Apply replacements
for old_url, new_path in replacements.items():
    content = content.replace(old_url, new_path)

# Special handling for Facebook Pixel - comment it out instead of replacing
# Find and comment out Facebook pixel code
fb_pixel_pattern = r"(document,\s*'script',\s*'https://connect\.facebook\.net/en_US/fbevents\.js'\);)"
content = re.sub(fb_pixel_pattern, r"// \1  // Disabled for offline use", content)

# Also comment out the noscript Facebook pixel
content = content.replace(
    '<img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=743204613787069&ev=PageView&noscript=1"',
    '<!-- Offline: FB Pixel disabled <img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=743204613787069&ev=PageView&noscript=1"'
)
content = content.replace('</noscript>', '</noscript> -->')

# Write the modified content
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ HTML file successfully converted to offline mode!")
print("\nReplaced URLs:")
for old, new in replacements.items():
    print(f"  {old[:60]}... -> {new}")
print("\n✓ Facebook Pixel tracking disabled")
print(f"\n✓ Backup saved to: {html_path}.backup")
