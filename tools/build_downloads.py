#!/usr/bin/env python3
"""Build stable ZIPs from the 24 iRiver theme JSONs. Original archives stay intact."""
from pathlib import Path
from collections import defaultdict
import argparse, json, os, zipfile

ROOT = Path(__file__).resolve().parents[1]
MODES = ("Default_Dialogue", "Highlighter")


def collect():
    colors = defaultdict(dict)
    for group in ("light", "dark"):
        for path in sorted((ROOT / "themes" / group).glob("*.json")):
            json.loads(path.read_text(encoding="utf-8-sig"))
            for mode in MODES:
                suffix = f"_{mode}.json"
                if path.name.startswith("iRiver_") and path.name.endswith(suffix):
                    color = path.name[len("iRiver_"):-len(suffix)]
                    if mode in colors[color]:
                        raise ValueError("Duplicate variant: " + path.name)
                    colors[color][mode] = path
                    break
            else:
                raise ValueError("Unexpected JSON: " + str(path))
    if len(colors) != 12 or any(set(group) != set(MODES) for group in colors.values()):
        raise ValueError("Expected exactly 12 colors with 2 variants each")
    return dict(sorted(colors.items()))


def archive_entries(colors, color=None):
    files = ([colors[color][mode] for mode in MODES] if color else
             [colors[name][mode] for name in colors for mode in MODES])
    return [(p.name, p.read_bytes()) for p in files] + [
        (name, (ROOT / name).read_bytes()) for name in ("LICENSE", "NOTICE.txt")
    ]


def validate(path, expected):
    with zipfile.ZipFile(path) as z:
        if sorted(z.namelist()) != sorted(n for n, _ in expected):
            raise ValueError(f"ZIP entries mismatch: {path}")
        for name, data in expected:
            if z.read(name) != data:
                raise ValueError(f"ZIP content differs from source JSON: {path}::{name}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check existing ZIPs without modifying them")
    args = parser.parse_args()
    colors = collect()
    dest = ROOT / "downloads"
    all_jobs = [("iRiver_Theme_Complete.zip", archive_entries(colors))] + [
        (f"iRiver_Theme_{name}.zip", archive_entries(colors, name)) for name in colors
    ]
    dest.mkdir(exist_ok=True)
    for name, expected in all_jobs:
        path = dest / name
        if not args.check:
            temp = dest / (name + ".tmp")
            with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
                for filename, data in expected:
                    z.writestr(filename, data)
            os.replace(temp, path)
        validate(path, expected)
    print(f"OK: {len(colors)} colors, {len(colors)*2} themes, {len(all_jobs)} valid ZIP files; check={args.check}")


if __name__ == "__main__":
    main()
