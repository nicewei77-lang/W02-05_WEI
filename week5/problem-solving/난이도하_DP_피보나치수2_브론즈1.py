# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())


def b_fib(n):
    table = [0] * (n+1)
    
    table[0] = 0
    table[1] = 1
    
    
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
        
    return table[n]

answer = b_fib(n)
print(answer)


n = int(input())

def t_fib(n, memo=None):
    if memo == None:
        memo = {}
        
    if n <= 1: memo[n] = n
    
    if n in memo: return memo[n]
    
    memo[n] = t_fib(n-1) + t_fib(n-2)
    
    return memo[n]

print(t_fib(10))