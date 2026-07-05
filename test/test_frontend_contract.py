from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "webapp" / "frontend"
STATIC = ROOT / "webapp" / "static"
INDEX = STATIC / "index.html"


class IndexParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.asset_paths = []

    def handle_starttag(self, _tag, attrs):
        attributes = dict(attrs)
        if element_id := attributes.get("id"):
            self.ids.add(element_id)
        for name in ("src", "href"):
            if (path := attributes.get(name, "")).startswith("/static/assets/"):
                self.asset_paths.append(path)


def parse_static_index():
    parser = IndexParser()
    parser.feed(INDEX.read_text(encoding="utf-8"))
    return parser


def read_frontend_source():
    source_files = [
        path for path in sorted((FRONTEND / "src").rglob("*.ts"))
        if not path.name.endswith(".test.ts")
    ]
    source_files.extend(sorted((FRONTEND / "src").rglob("*.vue")))
    return "\n".join(path.read_text(encoding="utf-8") for path in source_files)


def test_production_index_mounts_vue_assets():
    index = parse_static_index()

    assert "app" in index.ids
    assert index.asset_paths


def test_frontend_source_has_scaffold_labels():
    source = read_frontend_source()

    for label in ("TensorGuard", "系统总览", "单 API 运行", "Bug 复现"):
        assert label in source, label


def test_frontend_source_has_no_hardcoded_environment_examples():
    source = read_frontend_source()

    for forbidden in ("NVIDIA A800", "NVIDIA L40", "CUDA 13.0", "GPU0"):
        assert forbidden not in source, forbidden


def test_generated_asset_paths_resolve():
    index = parse_static_index()

    assert index.asset_paths
    for asset_path in index.asset_paths:
        assert (STATIC / asset_path.removeprefix("/static/")).is_file(), asset_path


if __name__ == "__main__":
    test_production_index_mounts_vue_assets()
    test_frontend_source_has_scaffold_labels()
    test_frontend_source_has_no_hardcoded_environment_examples()
    test_generated_asset_paths_resolve()
    print("frontend scaffold contract: OK")
