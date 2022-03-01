from problem_7 import solve

def test_example_1():
    assert solve('111') == 3

def test_example_2():
    assert solve('311') == 2


def test_example_3():
    assert solve('131') == 2

def test_example_5():
    assert solve('101') == 1

def test_example_6():
    assert solve('1011') == 2
