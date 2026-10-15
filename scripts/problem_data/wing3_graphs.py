"""
Wing 3: Graphs (100 Problems: 10 Easy, 60 Medium, 30 Hard).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.problem_data.graph_easy import get_graph_easy
from scripts.problem_data.graph_medium_part1 import get_graph_medium_part1
from scripts.problem_data.graph_medium_part2 import get_graph_medium_part2
from scripts.problem_data.graph_medium_part3 import get_graph_medium_part3
from scripts.problem_data.graph_medium_part4 import get_graph_medium_part4
from scripts.problem_data.graph_hard_part1 import get_graph_hard_part1
from scripts.problem_data.graph_hard_part2 import get_graph_hard_part2


def get_wing3_problems():
    problems = []
    problems.extend(get_graph_easy())           # 10 Easy (Floors 301-310)
    problems.extend(get_graph_medium_part1())   # 15 Medium (Floors 311-325)
    problems.extend(get_graph_medium_part2())   # 15 Medium (Floors 326-340)
    problems.extend(get_graph_medium_part3())   # 15 Medium (Floors 341-355)
    problems.extend(get_graph_medium_part4())   # 15 Medium (Floors 356-370)
    problems.extend(get_graph_hard_part1())     # 15 Hard (Floors 371-385)
    problems.extend(get_graph_hard_part2())     # 15 Hard (Floors 386-400)
    return problems


if __name__ == "__main__":
    probs = get_wing3_problems()
    print(f"Total Wing 3 Problems: {len(probs)}")
    easy = sum(1 for p in probs if p['difficulty'] == 'easy')
    med = sum(1 for p in probs if p['difficulty'] == 'medium')
    hard = sum(1 for p in probs if p['difficulty'] == 'hard')
    print(f"Difficulty breakdown: Easy={easy}, Medium={med}, Hard={hard}")
    assert len(probs) == 100, f"Expected 100 problems, got {len(probs)}"
    assert easy == 10 and med == 60 and hard == 30, "Difficulty mismatch"
    
    pids = [p['id'] for p in probs]
    assert len(pids) == len(set(pids)), f"Duplicate IDs found: {len(pids)} vs {len(set(pids))}"
    
    print("Testing all 100 Graph problem solutions...")
    for p in probs:
        loc = {}
        exec(p['python']['solutionCode'], loc)
        fn = loc[p['functionName']]
        for tc in p['testCases']:
            res = fn(*tc['input'])
            assert res == tc['expected'], f"Failed {p['id']} on input {tc['input']}: got {res}, expected {tc['expected']}"
    print("All 100 Graph problems passed verification!")
