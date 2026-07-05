import json
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "webapp" / "frontend"
STATIC = ROOT / "webapp" / "static"


class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.asset_paths = []

    def handle_starttag(self, _tag, attrs):
        attributes = dict(attrs)
        for name in ("src", "href"):
            if (path := attributes.get(name, "")).startswith("/static/assets/"):
                self.asset_paths.append(path)


def test_vue_frontend_has_build_contract():
    package = json.loads((FRONTEND / "package.json").read_text(encoding="utf-8"))
    vite = (FRONTEND / "vite.config.ts").read_text(encoding="utf-8")

    assert package["scripts"]["build"] == "vue-tsc --noEmit && vite build"
    assert package["engines"]["node"] == ">=20.19.0"
    assert (FRONTEND / ".nvmrc").read_text(encoding="utf-8").strip() == "22"
    assert 'outDir: "../static"' in vite
    assert 'base: command === "build" ? "/static/" : "/"' in vite


def test_generated_assets_match_static_index():
    parser = AssetParser()
    parser.feed((STATIC / "index.html").read_text(encoding="utf-8"))

    assert parser.asset_paths
    for asset_path in parser.asset_paths:
        assert (STATIC / asset_path.removeprefix("/static/")).is_file(), asset_path


def test_python_static_root_is_unchanged():
    server = (ROOT / "webapp" / "server.py").read_text(encoding="utf-8")

    assert 'STATIC_ROOT = Path(__file__).resolve().parent / "static"' in server


if __name__ == "__main__":
    test_vue_frontend_has_build_contract()
    test_generated_assets_match_static_index()
    test_python_static_root_is_unchanged()
    print("frontend build contract: OK")
