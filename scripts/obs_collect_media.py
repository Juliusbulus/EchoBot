# python3 obs_collect_media.py /path/to/scene_collection.json ~/Desktop/OBS_Media_Collected --dry-run
import argparse
import csv
import hashlib
import json
import shutil
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Union

Json = Union[dict, list, str, int, float, bool, None]


def sha8(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8", errors="ignore")).hexdigest()[:8]


def iter_strings(node: Json) -> Iterable[str]:
    """Yield all string values from a nested JSON structure."""
    if isinstance(node, dict):
        for k, v in node.items():
            # Skip obvious non-file fields
            if isinstance(v, str):
                yield v
            else:
                yield from iter_strings(v)
    elif isinstance(node, list):
        for item in node:
            yield from iter_strings(item)


def looks_like_path(s: str) -> bool:
    """
    Heuristics to identify local file paths.
    - Absolute paths on macOS/Linux (starts with '/')
    - Absolute paths on Windows (e.g., 'C:\\' or 'C:/')
    - Excludes http(s) URLs
    """
    if not isinstance(s, str):
        return False
    ls = s.strip()
    if not ls:
        return False
    lower = ls.lower()
    if lower.startswith("http://") or lower.startswith("https://"):
        return False
    if ls.startswith("/"):
        return True
    # Windows drive
    if len(ls) > 2 and ls[1] == ":" and (ls[2] == "\\" or ls[2] == "/"):
        return True
    return False


def collect_paths(data: Json) -> set[Path]:
    paths: set[Path] = set()
    for s in iter_strings(data):
        if looks_like_path(s):
            paths.add(Path(s))
    return paths


def unique_dest_name(dest_dir: Path, src_path: Path) -> Path:
    """
    Create a destination filename in dest_dir.
    If a file with the same name exists (or another source shares the same name),
    append '-<hash8>' before the extension.
    """
    base = src_path.name
    candidate = dest_dir / base
    if not candidate.exists():
        return candidate

    stem = src_path.stem
    suffix = "".join(src_path.suffixes)  # keep compound suffixes
    hashed = f"{stem}-{sha8(str(src_path))}{suffix}"
    return dest_dir / hashed


def copy_files(
    paths: Iterable[Path], dest_dir: Path, dry_run: bool = False
) -> tuple[int, int, list]:
    copied = 0
    skipped = 0
    manifest_rows = []

    dest_dir.mkdir(parents=True, exist_ok=True)

    for p in sorted(set(paths)):
        src = p
        if not src.exists():
            skipped += 1
            manifest_rows.append([str(src), "", "MISSING"])
            continue
        if src.is_dir():
            skipped += 1
            manifest_rows.append([str(src), "", "SKIPPED_DIR"])
            continue

        dst = unique_dest_name(dest_dir, src)
        action = "COPY"
        if dry_run:
            action = "DRY_RUN"
        else:
            shutil.copy2(src, dst)
            copied += 1
        manifest_rows.append([str(src), str(dst), action])

    return copied, skipped, manifest_rows


def write_manifest(dest_dir: Path, rows: list, dry_run: bool):
    manifest = dest_dir / ("manifest_dry_run.csv" if dry_run else "manifest.csv")
    with manifest.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source_path", "dest_path", "status"])
        w.writerows(rows)
    return manifest


def main():
    ap = argparse.ArgumentParser(
        description="Collect all local media referenced in an OBS scene-collection JSON and copy into one folder."
    )
    ap.add_argument("json_file", help="Path to OBS scene-collection JSON")
    ap.add_argument("dest_dir", help="Destination directory to copy media into")
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="List what would be copied, but don't copy",
    )
    args = ap.parse_args()

    json_path = Path(args.json_file).expanduser()
    dest_dir = Path(args.dest_dir).expanduser()

    if not json_path.exists():
        print(f"Error: JSON file not found: {json_path}", file=sys.stderr)
        sys.exit(1)

    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading/parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

    all_strings = list(iter_strings(data))  # noqa
    raw_paths = collect_paths(data)

    # Optionally, further restrict to common OBS file keys (kept generic by default)
    # If you want to only copy from specific keys like 'local_file', uncomment and adapt:
    # raw_paths = {Path(s) for s in all_strings if looks_like_path(s)}

    print(f"Found {len(raw_paths)} candidate path(s).")

    copied, skipped, rows = copy_files(raw_paths, dest_dir, dry_run=args.dry_run)
    manifest = write_manifest(dest_dir, rows, dry_run=args.dry_run)

    print(f"Done. Copied: {copied}, Skipped/Missing: {skipped}.")
    print(f"Manifest: {manifest}")


if __name__ == "__main__":
    main()
