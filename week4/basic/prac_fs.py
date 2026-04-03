# BFS (너비 우선 탐색)

def bfs(start):
    # 1) 시작점 초기화
    queue = deque([start])
    visited = {start}
    
    # 2) 큐가 빌 때까지 반복
    while queue:
        cur = queue.popleft()
        
        # 3) 이웃 순회 → 미방문이면 방문+큐삽입
        for nxt in neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    
    # 4) 결과 반환
    return visited

# DFS (깊이 우선 탐색)

def dfs(cur, visited=None):
    # 1) 첫 호출이면 초기화
    if visited is None:
        visited = []
    
    # 2) 현재 정점 방문 처리
    visited.append(cur)
    
    # 3) 이웃 순회 → 미방문이면 재귀
    for nxt in neighbors(cur):
        if nxt not in visited:
            dfs(nxt, visited)
    
    # 4) 결과 반환
    return visited


def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        cur = queue.popleft()
        
        for nxt in neighbors(cur):
            if nxt not in visited:
                visited.add()
                queue.append(nxt)
                
    return visited


def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        cur = queue.popleft()
        
        for nxt in neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
                
    return visited
                
        
    
    
def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        cur = queue.popleft()
        
        for nxt in neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
                
    retuen visited
    
    
def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        cur = queue.popleft()
        
        for nxt in neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
                
    return visited




def dfs(cur, visited=None):
    if visited is None:
        visited = []
        
    for nxt in neighbors(cur):
        if nxt not in visited:
            dfs(nxt, visited)
            
    return visited


def dfs(cur, visited=None):
    if visited is None:
        visited = []
        
    visited.append(cur)
        
    for nxt in neighbors(cur):
        if nxt not in visited:
            dfs(nxt, visited)
            
    return visited



def dfs(cur, visited=None):
    if visited is None:
        visited = []
        
    visited.append(cur)
    
    for nxt in neighbors(cur):
        if nxt not in visited:
            dfs(nxt, visited)
            
    return visited


def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        cur = queue.popleft()
        
        for nxt in neighbors(cur):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
                
    return visited
    
    
    
def dfs(cur, visited=None):
    if visited is None:
        visited = []
       
    visited.append(cur)
    
    for nxt in neighbors(cur):
        if nxt not in visited:
            dfs(nxt, visited)
            
    return visited
    
