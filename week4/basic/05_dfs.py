"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문

# 팁 #

dfs는 방금 만난 이웃의 집으로 바로 들어감

기본값(매개변수에 미리 정해두는 값) 함정: mutable은 초기화하지 않으면(맨 첫 호출에만) 계속 함수를 호출할 때마다 값이 그 위에 추가됨
즉, 같은 함수를 두 번 쓰는 순간 망가진다
mutable = None 을 기본값으로 하고 None이면 초기화 하는게 이를 피하는 방법

graph = {0: [1, 2], 1: [3, 4], 2: [5]}

DFS: 0 → 1 → 3 → 4 → 2 → 5   # 1 첫 번째 이웃의 이웃을 끝까지 파고든 뒤 2로
BFS: 0 → 1 → 2 → 3 → 4 → 5   # 0의 이웃 다 보고, 그 다음 레벨로

dfs는 start에서 갈 수 있는 모든 정점을 visited에 추가해서 반환한다
재귀 호출을 무시하고 보면 함수의 역할을 말할 수 있다
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화
    if visited is None:
        visited = []
    
    
    # TODO: 현재 정점 방문(visited에 추가)
    visited.append(start)
    
    
    # TODO: 인접한 정점들에 대해 재귀
    ## 방문하지 않은 정점이면 재귀 호출
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


