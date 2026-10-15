from typing import Any, Dict, List, Optional


def make_problem(
    pid: str,
    title: str,
    wing_id: str,
    floor: int,
    difficulty: str,
    visualizer_type: str = "array",
    monster_name: str = "Dungeon Beast",
    monster_title: str = "Terror of the Depths",
    monster_sprite: str = "slime",
    monster_color: str = "#8b5cf6",
    monster_attack: str = "Dark Bolt",
    monster_quote: str = "Arrgh, you mastered this algorithm!",
    description: str = "",
    examples: Optional[List[Dict[str, str]]] = None,
    constraints: Optional[List[str]] = None,
    function_name: str = "solution",
    starter_code: str = "",
    solution_code: str = "",
    test_cases: Optional[List[Dict[str, Any]]] = None,
    hints: Optional[List[str]] = None,
    leetcode_id: Optional[int] = None,
    leetcode_title: Optional[str] = None,
    leetcode_url: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Helper to construct a fully standardized problem dictionary."""
    v_type = kwargs.get("visualizerType", visualizer_type)
    examples = examples or []
    constraints = constraints or []
    test_cases = test_cases or []
    hints = hints or []

    formatted_cases = []
    for idx, tc in enumerate(test_cases, 1):
        inp = tc["input"]
        exp = tc["expected"]
        inp_disp = tc.get("inputDisplay") or (f"args={inp}" if len(inp) > 1 else str(inp[0]))
        exp_disp = tc.get("expectedDisplay") or str(exp)
        is_hidden = tc.get("isHidden", idx > 3)
        formatted_cases.append({
            "id": idx,
            "input": inp,
            "expected": exp,
            "inputDisplay": str(inp_disp)[:80],
            "expectedDisplay": str(exp_disp)[:80],
            "isHidden": is_hidden,
        })

    monster_hp = max(6, len(formatted_cases))
    if difficulty == "medium":
        monster_hp = max(8, monster_hp)
    elif difficulty == "hard":
        monster_hp = max(10, monster_hp)

    return {
        "id": pid,
        "wingId": wing_id,
        "floor": floor,
        "title": title,
        "difficulty": difficulty,
        "visualizerType": v_type,
        "monster": {
            "id": f"mon-{pid}",
            "name": monster_name,
            "title": monster_title,
            "maxHp": monster_hp,
            "hp": monster_hp,
            "sprite": monster_sprite,
            "color": monster_color,
            "attackName": monster_attack,
            "attackPower": 3 if difficulty == "hard" else (2 if difficulty == "medium" else 1),
            "defeatQuote": monster_quote,
        },
        "description": description,
        "examples": examples,
        "constraints": constraints,
        "starterCode": starter_code,
        "solutionCode": solution_code,
        "functionName": function_name,
        "testCases": formatted_cases,
        "hints": hints,
        "python": {
            "starterCode": starter_code,
            "solutionCode": solution_code,
        },
        "leetcodeId": leetcode_id,
        "leetcodeTitle": leetcode_title or title,
        "leetcodeUrl": leetcode_url or (f"https://leetcode.com/problems/{pid}/" if leetcode_id else None),
    }
