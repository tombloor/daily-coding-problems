from problem_2 import solve, solve_followup

def test_example_1():
    arr = [1, 2, 3, 4, 5]
    
    assert solve(arr) == [120, 60, 40, 30, 24]

def test_example_2():
    arr = [3, 2, 1]
    
    assert solve(arr) == [2, 3, 6]

def test_followup_1():
    arr = [1, 2, 3, 4, 5]
    
    assert solve_followup(arr) == [120, 60, 40, 30, 24]

def test_followup_2():
    arr = [3, 2, 1]
    
    assert solve_followup(arr) == [2, 3, 6]
