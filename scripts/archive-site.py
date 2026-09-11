import os
import re
import json
from urllib.request import urlopen, Request
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser

BASE_URL = "https://www.florastreetstrategies.com"
PAGES = ["/", "/services", "/about", "/testimonials", "/contact"]
OUT_DIR = r"C:\sites\flora-street-strategies\docs\archive"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def fetch(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read(), resp.headers.get_content_type()

def safe_name(url):
    parsed = urlparse(url)
    path = parsed.path.lstrip("/")
    if not path:
        path = "index.html"
    if path.endswith("/"):
        path += "index.html"
    return path.replace("/", os.sep)

class AssetExtractor(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.assets = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "stylesheet":
            href = attrs.get("href")
            if href:
                self.assets.add(urljoin(self.base_url, href))
        if tag == "script":
            src = attrs.get("src")
            if src:
                self.assets.add(urljoin(self.base_url, src))
        if tag == "img":
            src = attrs.get("src", attrs.get("data-src"))
            if src:
                self.assets.add(urljoin(self.base_url, src))
        if tag == "source":
            src = attrs.get("src", attrs.get("srcset"))
            if src:
                self.assets.add(urljoin(self.base_url, src))

    def handle_data(self, data):
        for match in re.finditer(r'url\([\'\"]?([^\)\'\"]+)[\'\"]?\)', data):
            self.assets.add(urljoin(self.base_url, match.group(1)))

def download_asset(asset_url, out_dir):
    try:
        data, ct = fetch(asset_url)
        parsed = urlparse(asset_url)
        path = parsed.path.lstrip("/")
        if not path or path.endswith("/"):
            path += "asset.bin"
        ext = os.path.splitext(path)[1]
        if not ext and ct:
            if "css" in ct:
                path += ".css"
            elif "javascript" in ct:
                path += ".js"
            elif "svg" in ct:
                path += ".svg"
            elif "png" in ct:
                path += ".png"
            elif "jpeg" in ct or "jpg" in ct:
                path += ".jpg"
        local_path = os.path.join(out_dir, path.replace("/", os.sep))
        ensure_dir(os.path.dirname(local_path))
        with open(local_path, "wb") as f:
            f.write(data)
        return local_path
    except Exception as e:
        print(f"Failed to download {asset_url}: {e}")
        return None

def main():
    ensure_dir(OUT_DIR)
    manifest = {"pages": {}, "assets": []}
    all_assets = set()

    for page in PAGES:
        page_url = urljoin(BASE_URL, page)
        print(f"Fetching {page_url} ...")
        html_bytes, _ = fetch(page_url)
        html_text = html_bytes.decode("utf-8", errors="replace")

        extractor = AssetExtractor(page_url)
        extractor.feed(html_text)
        all_assets.update(extractor.assets)

        if page == "/":
            rel_path = "index.html"
        else:
            rel_path = page.lstrip("/") + ".html"
        out_path = os.path.join(OUT_DIR, rel_path.replace("/", os.sep))
        ensure_dir(os.path.dirname(out_path))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_text)
        manifest["pages"][page] = rel_path

    assets_dir = os.path.join(OUT_DIR, "assets")
    for asset_url in sorted(all_assets):
        print(f"Downloading asset {asset_url} ...")
        local = download_asset(asset_url, assets_dir)
        if local:
            manifest["assets"].append({"url": asset_url, "local": os.path.relpath(local, OUT_DIR)})

    manifest_path = os.path.join(OUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Archive complete. Manifest: {manifest_path}")

if __name__ == "__main__":
    main()
