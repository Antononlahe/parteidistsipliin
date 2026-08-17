"""Manual children_count corrections when the official profile line is blank or stale.

The committed HTML cache stays as published. This map is applied at write time so rebuild
does not revert the corrections. Keep slugs in apps/web/lib/varia.ts in sync.
"""

from __future__ import annotations

import json
from pathlib import Path

from parteidistsipliin_scraper.profile_cache import CACHE_DIR

OVERRIDES_PATH = CACHE_DIR / "children_overrides.json"


def load_children_overrides() -> dict[str, int]:
    raw = json.loads(Path(OVERRIDES_PATH).read_text(encoding="utf-8"))
    return {uuid: int(row["children_count"]) for uuid, row in raw.items()}
