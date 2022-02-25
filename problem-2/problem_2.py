import math

# return array where each element is product of all others (excluding itself)
def solve(arr):
    total = math.prod(arr)
    result = []
    
    for n in arr:
        result.append(total / n)

    return result

#[3, 2, 1] == [2, 3, 6]
def solve_followup(arr):
    result = [1 for n in range(0, len(arr))]
    tmp = 1

    # Iterate forward - filling cumulative product of arr[0] -> arr[i]
    for i in range(0, len(arr)):
        result[i] = tmp
        tmp *= arr[i]

    # [1, 3, 6]

    # Reset tmp 
    tmp = 1

    # Iterate backward - filling with cumulative product of arr[-1] -> arr[i] 
    for i in range(1, len(arr) + 1):
        result[-i] = tmp * result[-i]
        tmp *= arr[-i]

    return result