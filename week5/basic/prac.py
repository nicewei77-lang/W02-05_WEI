def solve(state, memo=None):
    if memo is None:
        memo = {}
        
    if base_case: return base_value
    
    if state in memo: return memo[state]
    
    memo[state] = 점화식(solve(작은 state, memo))
    
    return memo[state]
answer = solve(start_state)
