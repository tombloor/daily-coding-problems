
def solve(s):
    if len(s) == 0:
        return 1                  # We've made it through a valid solution
    
    if s[0] == '0':
        return 0                  # This is an invalid solution, leading zeros are not allowed

    solutions = solve(s[1:])      # Recurse, taking the first number in isolation

    if len(s) >= 2 and int(s[0:2]) < 27:
        solutions += solve(s[2:]) # We are able to also consider the first two numbers together, so recurse without them

    return solutions
