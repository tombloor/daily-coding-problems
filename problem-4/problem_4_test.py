from problem_4 import solve

def test_example_1():
    arr = [3, 4, -1, 1]

    assert solve(arr) == 2

def test_example_2():
    arr = [1, 2, 0]
    
    assert solve(arr) == 3