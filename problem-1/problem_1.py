
# Check if pair in arr add up to k
def solve(arr, k):
    remainders = set()
    for n in arr:
        r = k - n
        if r in remainders:
            return True
        remainders.add(n)
    return False
