

def solve(arr):
    # Move all negative and zero to the start of the array
    pos_idx = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[pos_idx] = arr[pos_idx], arr[i]
            pos_idx += 1

    # Iterate through the array and set the idx of each number to negative
    for i in range(pos_idx, len(arr)):
        abs_item = abs(arr[i])
        if abs_item < len(arr):
            arr[abs_item] = abs(arr[abs_item]) * -1

    # Return the index of the first positive number
    for i in range(pos_idx, len(arr)):
        if arr[i] > 0:
            return i

    return i + 1