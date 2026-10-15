"""
Master Assembly & Dual-Storage Emitter Script.

Combines:
- 98 Existing problems in public/problems/data/*.json
- 500 New problems across the 5 Wings (scripts/problem_data/wing*.py)
Total: 598 algorithm challenges.

Actions:
1. Strips any legacy JavaScript from starter/solution code (locks strictly to Python 3).
2. Generates backend/data/problems_backup.json (master persistent backup).
3. Generates public/problems/data/{id}.json for all 598 problems.
4. Generates public/problems/catalog.json (compact metadata for all 598 problems).
5. Generates src/data/problems/catalog.ts (TypeScript catalog used by frontend).
"""

import os
import sys
import glob
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.problem_data.wing1_ds import get_wing1_problems
from scripts.problem_data.wing2_bt import get_wing2_problems
from scripts.problem_data.wing3_graphs import get_wing3_problems
from scripts.problem_data.wing4_bs_greedy import get_wing4_problems
from scripts.problem_data.wing5_bit import get_wing5_problems


def assemble_all_problems():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    existing_dir = os.path.join(base_dir, "public", "problems", "data")
    
    # 1. Load 500 New Problems first
    w1 = get_wing1_problems()
    w2 = get_wing2_problems()
    w3 = get_wing3_problems()
    w4 = get_wing4_problems()
    w5 = get_wing5_problems()

    new_problems = w1 + w2 + w3 + w4 + w5
    new_ids = {p["id"] for p in new_problems}
    print(f"Loaded 500 new problems: Wing1={len(w1)}, Wing2={len(w2)}, Wing3={len(w3)}, Wing4={len(w4)}, Wing5={len(w5)}")

    # 2. Load Existing Problems (excluding any generated new ones)
    existing_files = glob.glob(os.path.join(existing_dir, "*.json"))
    print(f"Scanning {len(existing_files)} problem files from {existing_dir}...")
    
    existing_problems = []
    for f in existing_files:
        with open(f, "r", encoding="utf-8") as fp:
            p = json.load(fp)
            if p["id"] in new_ids:
                continue
            # Ensure top-level starterCode & solutionCode are 100% Python
            if "python" in p and p["python"].get("starterCode"):
                p["starterCode"] = p["python"]["starterCode"]
            if "python" in p and p["python"].get("solutionCode"):
                p["solutionCode"] = p["python"]["solutionCode"]
            existing_problems.append(p)

    print(f"Loaded {len(existing_problems)} original existing problems.")

    all_problems = existing_problems + new_problems
    print(f"Total problems combined: {len(all_problems)}")

    # 3. Verification & Validation
    seen_ids = set()
    duplicates = []
    for p in all_problems:
        pid = p["id"]
        if pid in seen_ids:
            duplicates.append(pid)
        seen_ids.add(pid)
    
    assert len(duplicates) == 0, f"Duplicate problem IDs found: {duplicates}"
    assert len(all_problems) == 598, f"Expected 598 problems, got {len(all_problems)}"

    # Difficulty counts
    easy_count = sum(1 for p in all_problems if p["difficulty"] == "easy")
    med_count = sum(1 for p in all_problems if p["difficulty"] == "medium")
    hard_count = sum(1 for p in all_problems if p["difficulty"] == "hard")
    print(f"Difficulty breakdown across 598 problems: Easy={easy_count}, Medium={med_count}, Hard={hard_count}")

    # Sort problems deterministically by wingId, floor, id
    all_problems.sort(key=lambda x: (x.get("wingId", ""), x.get("floor", 0), x["id"]))

    # 4. Emit backend/data/problems_backup.json
    backend_backup_path = os.path.join(base_dir, "backend", "data", "problems_backup.json")
    os.makedirs(os.path.dirname(backend_backup_path), exist_ok=True)
    with open(backend_backup_path, "w", encoding="utf-8") as fp:
        json.dump(all_problems, fp, indent=2, ensure_ascii=False)
    print(f"Successfully wrote master backup: {backend_backup_path} ({len(all_problems)} problems)")

    # 5. Emit all 598 individual JSON files to public/problems/data/{id}.json
    for p in all_problems:
        p_path = os.path.join(existing_dir, f"{p['id']}.json")
        with open(p_path, "w", encoding="utf-8") as fp:
            json.dump(p, fp, indent=2, ensure_ascii=False)
    print(f"Successfully wrote {len(all_problems)} individual problem JSON files in {existing_dir}")

    # 6. Build Catalog Entries
    catalog_entries = []
    for p in all_problems:
        catalog_entries.append({
            "id": p["id"],
            "wingId": p["wingId"],
            "floor": p.get("floor", 1),
            "title": p["title"],
            "difficulty": p["difficulty"],
            "visualizerType": p.get("visualizerType", "array"),
            "leetcodeId": p.get("leetcodeId"),
            "leetcodeTitle": p.get("leetcodeTitle"),
            "leetcodeUrl": p.get("leetcodeUrl"),
            "monster": p.get("monster", {})
        })

    # 7. Emit public/problems/catalog.json
    public_catalog_path = os.path.join(base_dir, "public", "problems", "catalog.json")
    with open(public_catalog_path, "w", encoding="utf-8") as fp:
        json.dump(catalog_entries, fp, indent=2, ensure_ascii=False)
    print(f"Successfully wrote public catalog: {public_catalog_path} ({len(catalog_entries)} entries)")

    # 8. Emit src/data/problems/catalog.ts
    ts_catalog_path = os.path.join(base_dir, "src", "data", "problems", "catalog.ts")
    ts_content = [
        "// Auto-generated by scripts/assemble_and_seed.py - DO NOT EDIT MANUALLY",
        "import { DungeonTopic, Difficulty } from '../../types/game';",
        "",
        "export interface CatalogEntry {",
        "  id: string;",
        "  wingId: DungeonTopic;",
        "  floor: number;",
        "  title: string;",
        "  difficulty: Difficulty;",
        "  visualizerType: string;",
        "  leetcodeId?: number | null;",
        "  leetcodeTitle?: string | null;",
        "  leetcodeUrl?: string | null;",
        "  monster: {",
        "    id: string;",
        "    name: string;",
        "    title: string;",
        "    maxHp: number;",
        "    hp: number;",
        "    sprite: string;",
        "    color: string;",
        "    attackName: string;",
        "    attackPower: number;",
        "    defeatQuote: string;",
        "  };",
        "}",
        "",
        f"export const problemCatalog: CatalogEntry[] = {json.dumps(catalog_entries, indent=2)};",
        ""
    ]
    with open(ts_catalog_path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(ts_content))
    print(f"Successfully wrote TypeScript catalog: {ts_catalog_path} ({len(catalog_entries)} entries)")


if __name__ == "__main__":
    assemble_all_problems()
