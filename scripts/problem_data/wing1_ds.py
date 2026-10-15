"""
Wing 1: Data Structures - 100 Problems (10 Easy, 60 Medium, 30 Hard).
"""
from scripts.problem_data.ds_easy import get_data_structures_problems as get_ds_easy
from scripts.problem_data.ds_medium_part1 import get_data_structures_medium as get_ds_m1
from scripts.problem_data.ds_medium_part2 import get_data_structures_medium_part2 as get_ds_m2
from scripts.problem_data.ds_medium_part3 import get_data_structures_medium_part3 as get_ds_m3
from scripts.problem_data.ds_medium_part4 import get_data_structures_medium_part4 as get_ds_m4
from scripts.problem_data.ds_hard import get_data_structures_hard as get_ds_hard


def get_wing1_problems():
    easy = get_ds_easy()        # 10
    med1 = get_ds_m1()          # 10
    med2 = get_ds_m2()          # 10
    med3 = get_ds_m3()          # 20
    med4 = get_ds_m4()          # 20
    hard = get_ds_hard()        # 30

    all_p = easy + med1 + med2 + med3 + med4 + hard
    assert len(all_p) == 100, f"Expected 100 problems, got {len(all_p)}"
    return all_p
