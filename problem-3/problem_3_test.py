from problem_3 import Node, serialize, deserialize

def test_example_1():
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    assert deserialize(serialize(node)).left.left.val == 'left.left'

def test_example_2():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    
    assert serialize(node) == 'root,left,left.left,,,,right,,'