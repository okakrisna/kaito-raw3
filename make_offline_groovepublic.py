#!/usr/bin/env python3
"""
Replace groovepublic.com absolute URLs with relative paths
"""

import re

# Read the HTML file
html_path = '/tmp/cc-agent/60777008/project/groovepublic.com/reveused/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace groovepublic.com URLs with relative paths
# Path from /groovepublic.com/reveused/ to /groovepublic.com/ is ../

# For wp-content, wp-includes, wp-admin (go up to groovepublic.com root)
content = content.replace('https://groovepublic.com/wp-content/', '../wp-content/')
content = content.replace('https://groovepublic.com/wp-includes/', '../wp-includes/')
content = content.replace('https://groovepublic.com/wp-admin/', '../wp-admin/')

# For other groovepublic.com references (keep them as is for now, or make relative)
# These are mostly metadata URLs that don't need to load
content = content.replace('https://groovepublic.com/', '../')
content = content.replace('http://groovepublic.com/', '../')

# Keep certain URLs absolute for metadata (Open Graph, schema.org, etc)
# Revert metadata URLs back to absolute
metadata_patterns = [
    (r'href="\.\./reveused/"', 'href="https://groovepublic.com/reveused/"'),
    (r'href="\.\./author/', 'href="https://groovepublic.com/author/'),
    (r'href="\.\./category/', 'href="https://groovepublic.com/category/'),
    (r'href="\.\./feed/', 'href="https://groovepublic.com/feed/'),
    (r'href="\.\./comments/', 'href="https://groovepublic.com/comments/'),
    (r'"@id":\s*"\.\.\/#', '"@id": "https://groovepublic.com/#'),
    (r'"@id":\s*"\.\./wp-content/', '"@id": "https://groovepublic.com/wp-content/'),
    (r'"url":\s*"\.\./wp-content/', '"url": "https://groovepublic.com/wp-content/'),
    (r'"url":\s*"\.\."', '"url": "https://groovepublic.com"'),
    (r'content="\.\./wp-content/', 'content="https://groovepublic.com/wp-content/'),
]

for pattern, replacement in metadata_patterns:
    content = re.sub(pattern, replacement, content)

# Write the modified content
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ groovepublic.com URLs converted to relative paths!")
print("✓ Metadata URLs kept absolute for SEO/sharing purposes")
