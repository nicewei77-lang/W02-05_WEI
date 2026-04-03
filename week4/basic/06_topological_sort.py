"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용

순서가 정해져 있는 작업의 순서를 결정하기 위한 알고리즘
모든 조건을 만족하는 일렬 배열을 만든다
정확히 이 순서대로만 가면 끝까지 할 수 있다
이게 위상 정렬
다른 순서도 존재한다
DAG(일방향+사이클x) 그래프에만 적용 - 시작점이 존재해야 함
두 가지 해결책을 낸다: 현재 그래프는 위상 정렬이 가능한가? 가능하다면 그 결과는 무엇인가?
큐나 스택으로 구현. 큐가 더 많이 쓰임
위상 정렬이 완전히 수행되려면 정확히 N개의 노드를 방문
큐에서 꺼낸 뒤 result에 넣는다
node는 항상 정점

In-degree (진입 차수): 나에게 들어오는 화살표 개수. (나를 지목한 사람)
Out-degree (진출 차수): 나로부터 나가는 화살표 개수. (내가 지목한 사람)

빨간줄 => 바로 윗줄이나 아랫줄에 오류가 있다


<단계>
1. 진입차수(해당 노드로 들어오는 선)이 0인 정점 큐에 삽입
2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거한다
3. 간선 제거 이후 진입차수가 0이 된 다른 정점들을 다시 큐에 삽입
4. 큐가 빌 때까지 2~3번 과정을 반복. 모든 원소 방문 전에 큐가 비며 사이클이 존재. 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과

# 질문 #
간선 리스트 생김새
edges = [
    (0, 1),  # 0 → 1
    (0, 2),  # 0 → 2
    (1, 3),  # 1 → 3
]
간선 그래프에 삽입 => 인덱스가 정점번호 값이 이웃목록
# graph[0].append(1) → [[], [], [], []] → [[1], [], [], []]
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    graph = [[] for _ in range(vertices)]
    in_degree = [0] * vertices
 
    
    # TODO: 그래프 구성 및 진입 차수 계산
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    queue = deque()
    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i) 
    
    result = []
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while queue:
        node = queue.popleft()
        result.append(node)
        
    ## 이웃 진입차수 감소
    ## 진입차수 0인 이웃 queue에 추가
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
