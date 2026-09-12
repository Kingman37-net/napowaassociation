import re
from pathlib import Path

DOCS = Path(__file__).parent.parent / 'docs'

for html_path in DOCS.glob('*.html'):
    content = html_path.read_text(encoding='utf-8')

    # Remove existing references
    content = re.sub(r'<link[^>]*assets/css/style\.css[^>]*>', '', content)
    content = re.sub(r'<script[^>]*assets/js/main\.js[^>]*></script>', '', content)

    # Inject CSS before </head>
    css_tag = '    <link rel="stylesheet" href="assets/css/style.css">\n'
    content = re.sub(r'(</head>)', css_tag + r'\1', content, count=1, flags=re.IGNORECASE)

    # Inject JS before </body>
    js_tag = '    <script src="assets/js/main.js"></script>\n'
    content = re.sub(r'(</body>)', js_tag + r'\1', content, count=1, flags=re.IGNORECASE)

    html_path.write_text(content, encoding='utf-8')
    print(f"🔗 {html_path.name}")

print("\n🎉 Assets linked.")
