from problem_5 import cons, car, cdr

def test_example_1():
    assert car(cons(3, 4)) == 3

def test_example_2():
    assert cdr(cons(3, 4)) == 4