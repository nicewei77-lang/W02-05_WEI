"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

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
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문

# 질문 #
큐에 넣을 때 start 체크 이유
node는 어떤 값인지
처음에 start만 넣는데 어떻게 끝까지 순회하는지
이웃을 result가 아니라 큐에 추가하는 이유
set() - 집합(set). 원소 있는지 확인하는 데에 적합. 인덱싱은 안됨. 반복문으로 값을 하나씩 꺼냄. 중복 허용 x(수학의 집합과 같음) 같은 값 또 넣으면 무시
deque() 빈 큐 만드는 함수
이웃: 인접한 노드를 이렇게 부름
굳이 visited를 집합으로 만든 이유: 확인을 빠르게 하기 위해 항상 O(1)
큐의 초기값은 iterable, 그 중에서도 순서가 있는 자료형이어야 한다. 초기값을 펼쳐서 원소를 하나씩 가져오기 때문 - 리스트, 튜플, 문자열

"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    ## 방문한 정점 집합
    visited = set()
    
    # TODO: 큐 생성 및 시작 정점 추가
    ## 큐 생성과 START 노드 넣기
    ## 빈 결과 리스트 만들기
    queue = deque([start])
    visited.add(start)
    result = []

    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 결과에 기록
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

