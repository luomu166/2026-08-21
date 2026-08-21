import pathlib
import re
from html.parser import HTMLParser

root = pathlib.Path("outputs/portfolio-site")

# 1) CSS brace balance
css = (root / "assets/css/style.css").read_text(encoding="utf-8")
print("CSS braces:", css.count("{"), css.count("}"),
      "OK" if css.count("{") == css.count("}") else "MISMATCH")

# 2) referenced local assets exist
html = (root / "index.html").read_text(encoding="utf-8")
refs = set(re.findall(r'(?:src|href)="(assets/[^"]+)"', html))
missing = [r for r in refs if not (root / r).exists()]
print("local refs:", len(refs), "missing:", missing if missing else "none")

# 3) basic tag balance
class P(HTMLParser):
    VOID = {"meta", "link", "img", "br", "hr", "input", "source",
            "area", "base", "col", "embed", "track", "wbr"}

    def __init__(self):
        super().__init__()
        self.stack = []
        self.errs = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errs.append(("mismatch", tag, self.getpos()))


p = P()
p.feed(html)
print("tag stack leftover:", p.stack if p.stack else "none",
      "errors:", p.errs if p.errs else "none")
