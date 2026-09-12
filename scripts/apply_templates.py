import re
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent.parent / 'templates'
DOCS_DIR = Path(__file__).parent.parent / 'docs'

nav_html = (TEMPLATE_DIR / 'nav.html').read_text(encoding='utf-8')
footer_html = (TEMPLATE_DIR / 'footer.html').read_text(encoding='utf-8')

for html_path in DOCS_DIR.glob('*.html'):
    content = html_path.read_text(encoding='utf-8')

    # Remove existing nav & footer
    content = re.sub(r'<nav\s+class="navbar".*?</nav>', '', content, flags=re.DOTALL|re.IGNORECASE)
    content = re.sub(r'<footer.*?</footer>', '', content, flags=re.DOTALL|re.IGNORECASE)

    content = re.sub(r'(<body[^>]*>)', r'\1\n' + nav_html, content, count=1, flags=re.IGNORECASE)
    content = re.sub(r'(</body>)', footer_html + r'\n\1', content, count=1, flags=re.IGNORECASE)

    html_path.write_text(content, encoding='utf-8')
    print(f"✅ {html_path.name}")

print("\n🎉 All pages updated.")
