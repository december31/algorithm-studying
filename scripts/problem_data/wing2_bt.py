"""
Wing 2: Backtracking (100 Problems: 10 Easy, 60 Medium, 30 Hard).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.problem_data.bt_easy import get_bt_easy
from scripts.problem_data.bt_medium_part1 import get_bt_medium_part1
from scripts.problem_data.bt_medium_part2 import get_bt_medium_part2
from scripts.problem_data.bt_medium_part3 import get_bt_medium_part3
from scripts.problem_data.bt_medium_part4 import get_bt_medium_part4
from scripts.problem_data.bt_medium_part5 import get_bt_medium_part5
from scripts.problem_data.bt_hard_part1 import get_bt_hard as get_bt_hard_part1
from scripts.problem_data.bt_hard_part2 import get_bt_hard_part2


def get_wing2_problems():
    problems = []
    problems.extend(get_bt_easy())           # 10 Easy (Floors 201-210)
    problems.extend(get_bt_medium_part1())   # 20 Medium (Floors 211-230)
    problems.extend(get_bt_medium_part2())   # 10 Medium (Floors 231-240)
    problems.extend(get_bt_medium_part3())   # 10 Medium (Floors 241-250)
    problems.extend(get_bt_medium_part4())   # 10 Medium (Floors 251-260)
    problems.extend(get_bt_medium_part5())   # 10 Medium (Floors 261-270)
    problems.extend(get_bt_hard_part1())     # 20 Hard (Floors 271-290)
    problems.extend(get_bt_hard_part2())     # 10 Hard (Floors 291-300)
    return problems


if __name__ == "__main__":
    probs = get_wing2_problems()
    print(f"Total Wing 2 Problems: {len(probs)}")
    easy = sum(1 for p in probs if p['difficulty'] == 'easy')
    med = sum(1 for p in probs if p['difficulty'] == 'medium')
    hard = sum(1 for p in probs if p['difficulty'] == 'hard')
    print(f"Difficulty breakdown: Easy={easy}, Medium={med}, Hard={hard}")
    assert len(probs) == 100, f"Expected 100 problems, got {len(probs)}"
    assert easy == 10 and med == 60 and hard == 30, "Difficulty mismatch"
    
    # Verify all problem IDs are unique
    pids = [p['id'] for p in probs]
    assert len(pids) == len(set(pids)), f"Duplicate IDs found: {len(pids)} vs {len(set(pids))}"
    
    print("Testing all 100 problem solutions...")
    for p in probs:
        loc = {}
        exec(p['python']['solutionCode'], loc)
        fn = loc[p['functionName']]
        for tc in p['testCases']:
            res = fn(*tc['input'])
            assert res == tc['expected'], f"Failed {p['id']} on input {tc['input']}: got {res}, expected {tc['expected']}"
    print("All 100 Backtracking problems passed verification!")
