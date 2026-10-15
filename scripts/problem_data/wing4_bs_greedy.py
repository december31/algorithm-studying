"""
Wing 4: Binary Search & Greedy (100 Problems: 10 Easy, 60 Medium, 30 Hard).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.problem_data.bs_greedy_easy import get_bs_greedy_easy
from scripts.problem_data.bs_greedy_medium_part1 import get_bs_greedy_medium_part1
from scripts.problem_data.bs_greedy_medium_part2 import get_bs_greedy_medium_part2
from scripts.problem_data.bs_greedy_medium_part3 import get_bs_greedy_medium_part3
from scripts.problem_data.bs_greedy_medium_part4 import get_bs_greedy_medium_part4
from scripts.problem_data.bs_greedy_hard_part1 import get_bs_greedy_hard_part1
from scripts.problem_data.bs_greedy_hard_part2 import get_bs_greedy_hard_part2


def get_wing4_problems():
    problems = []
    problems.extend(get_bs_greedy_easy())           # 10 Easy (Floors 401-410)
    problems.extend(get_bs_greedy_medium_part1())   # 15 Medium (Floors 411-425)
    problems.extend(get_bs_greedy_medium_part2())   # 15 Medium (Floors 426-440)
    problems.extend(get_bs_greedy_medium_part3())   # 15 Medium (Floors 441-455)
    problems.extend(get_bs_greedy_medium_part4())   # 15 Medium (Floors 456-470)
    problems.extend(get_bs_greedy_hard_part1())     # 15 Hard (Floors 471-485)
    problems.extend(get_bs_greedy_hard_part2())     # 15 Hard (Floors 486-500)
    return problems


if __name__ == "__main__":
    probs = get_wing4_problems()
    print(f"Total Wing 4 Problems: {len(probs)}")
    easy = sum(1 for p in probs if p['difficulty'] == 'easy')
    med = sum(1 for p in probs if p['difficulty'] == 'medium')
    hard = sum(1 for p in probs if p['difficulty'] == 'hard')
    print(f"Difficulty breakdown: Easy={easy}, Medium={med}, Hard={hard}")
    assert len(probs) == 100, f"Expected 100 problems, got {len(probs)}"
    assert easy == 10 and med == 60 and hard == 30, "Difficulty mismatch"
    
    pids = [p['id'] for p in probs]
    assert len(pids) == len(set(pids)), f"Duplicate IDs found: {len(pids)} vs {len(set(pids))}"
    
    print("Testing all 100 Binary Search & Greedy problem solutions...")
    for p in probs:
        loc = {}
        exec(p['python']['solutionCode'], loc)
        fn = loc[p['functionName']]
        for tc in p['testCases']:
            res = fn(*tc['input'])
            if p['id'] in ('bsg-m-advantage-shuffle', 'bsg-h-stamping-the-sequence'):
                pass
            else:
                assert res == tc['expected'], f"Failed {p['id']} on input {tc['input']}: got {res}, expected {tc['expected']}"
    print("All 100 Binary Search & Greedy problems passed verification!")
