from problem_1 import solve

def test_example_1():
    arr = [10,15,3,7]
    k = 17

    assert solve(arr, k) == True

def test_example_2():
    arr = [10,15,3,7]
    k = 19

    assert solve(arr, k) == False