from collections import deque

def bfs(won):
    queue = deque()
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n+1)]
    visited = {}
    cur = 0
    level = 0
    queue.append(coins[0])
    visited.add(coins[0])
    
    while queue:
        level += 1
        for i in range(len(queue)):
            cur = queue.popleft()
            
            for coin in coins:
                if cur + coin == k: return level
                
                elif cur + coin < k and (cur + coin) not in visited:
                    visited.add(cur + coin)
                    queue.append(cur + coin)
                    
                
          
        
        
    
