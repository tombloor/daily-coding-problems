

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _serialize_helper(root):
    results = []
    if not root:
        results.append('')
    else:
        results.append(root.val)
        results += _serialize_helper(root.left)
        results += _serialize_helper(root.right)
    return results

def serialize(root):
    results = _serialize_helper(root)
    return ','.join(results)

def _deserialize_helper(arr, idx):
    if arr[idx] == '':
        return None, idx
    
    n = Node(arr[idx])
    n.left, idx = _deserialize_helper(arr, idx + 1)
    n.right, idx = _deserialize_helper(arr, idx + 1)

    return n, idx

def deserialize(s):
    arr = s.split(',')
    result, _ =  _deserialize_helper(arr, 0)
    return result