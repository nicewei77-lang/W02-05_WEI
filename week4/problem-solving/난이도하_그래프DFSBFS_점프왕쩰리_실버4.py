# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
"""
문제
‘쩰리’는 점프하는 것을 좋아하는 젤리다. 단순히 점프하는 것에 지루함을 느낀 ‘쩰리’는 새로운 점프 게임을 해보고 싶어 한다. 새로운 점프 게임의 조건은 다음과 같다.

‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.
새로운 게임이 맘에 든 ‘쩰리’는, 계속 게임을 진행해 마침내 최종 단계에 도달했다. 하지만, 게임을 진행하는 구역이 너무 넓어져버린 나머지, 이 게임에서 이길 수 있는지 없는지 가늠할 수 없어졌다. ‘쩰리’는 유능한 프로그래머인 당신에게 주어진 구역에서 승리할 수 있는 지 알아봐 달라고 부탁했다. ‘쩰리’를 도와 주어진 게임 구역에서 끝 점(오른쪽 맨 아래 칸)까지 도달할 수 있는지를 알아보자!

입력
입력의 첫 번째 줄에는 게임 구역의 크기 N (2 ≤ N ≤ 3)이 주어진다.
입력의 두 번째 줄부터 마지막 줄까지 게임판의 구역(맵)이 주어진다.
게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.

출력
‘쩰리’가 끝 점에 도달할 수 있으면 “HaruHaru”(인용부호 없이), 도달할 수 없으면 “Hing” (인용부호 없이)을 한 줄에 출력합니다.

예제 입력 1 
3
1 1 10
1 5 1
2 2 -1

예제 출력 1 
HaruHaru

# 슈도코드
좌표계 만들기
while -1에 도달할 때까지 DO
    칸 수 읽기
    칸 수만큼 아래 or 오른쪽 이동
    if -1까지의 거리 < 칸 수 then
        Hing 출력
    elif -1까지의 거리 > 칸 수 then
        다시 이동
    elif -1까지의 거리 == 칸 수
        HaruHaur 출력
        
       
"""
from collections import deque

N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().split()))) # board.append(input()) — 이러면 board에 문자열이 들어가니 숫자 리스트로 변환
    
    
queue = deque()
queue.append([0, 0]) # r, c가 아직 정의되지 않았으니 [0, 0]이 아닌 시작점 좌표를 넣어야 함
visited = [] # while 문 밖에서 초기화
win = False
while queue:
    r, c = queue.popleft()
    n = board[r][c]
    for dr, dd in [[n, 0], [0, n]]:
        if r + dr <= N - 1 and c + dd <= N - 1 and [r + dr, c + dd] not in visited: # if dr <= N - 1 and dd <= N - 1: — 이건 이동량을 체크하는 거지, 도착 좌표를 체크하는 게 아니에요. r + dr과 c + dd가 범위 안인지 확인해야 해요. / visited 체크를 오프셋이 아니라 실제 도착 좌표로 해야 해요. [r+dr, c+dd]가 visited에 있는지 확인해보세요!
            dr, dd = r + dr, c + dd # nr, nc로 했으면 가독성 업
            queue.append([dr, dd]) # queue.append([r, c]) — 현재 위치를 다시 넣고 있어요. 새로운 위치를 넣어야 해요.
            visited.append([dr, dd])
            if board[dr][dd] == -1:
                    print("HaruHaru")
                    win = True
if win == False: # 이게 없으면 항상 실행 / print("Hing") # print("Hing")이 for 루프 안에 있어요 — BFS가 완전히 끝난 뒤에 한 번만 출력해야 해요. 지금 구조면 매번 출력돼요.
    print("Hing")   
        
        
# 좌표 표현하는 법: 행과 열은 [r, c]으로 묶어서 관리   
# 트레이싱 해야 하는 변수
# 큐에 넣는 값
# 큐에서 빼는 값
# 큐에서 빼는 법
# 방문체크 해야하는 이유: 아래/오른쪽으로만 가서 재방문할 수 없지만 함정이 존재. 칸의 값이 0일 경우 같은 칸을 넣으면서 무한 루프에 빠진다
# while queue 존재 이유(하나씩 넣고 하나씩 빼는데): 
# 큐를 쓰는 이유: 내 생각 행, 열 순으로 빼려고

    """Retrospective
    # 문제정의
    ## 정의
    '젤리를 이동시켜 골에 도달할 수 있으면 X 도중에 실패하면 Y 출력'
    ## 문제 나누기
    '방문 - 승패판단' 구조는 맞음
    ## 조건 파악
    '점프'가 아닌 '한 칸씩 이동'으로 오해석 => 한 점프에 아래와 오른쪽 양방향의 움직임이 동시에 가능한 줄 알았음
    
    # 접근
    ## 거리
    현재 골까지의 거리와 n을 비교 => 이번 이동이 보드범위를 벗어나는지 체크했어야 함 (원인: 조건 오이해)
    n과 현재 이동 가능한 거리를 비교하는 아이디어 방향은 맞았음
    ## DFS
    도달 가능여부/최단거리/모든경우/연결된 묶음 수 => 그래프문제(BFS, DFS)
    트리는 노드 -> 노드 경로가 딱 하나, 방향이 부모 -> 자식으로만, 사이클 없다
    ## 분기가 2개
    그래프는 갈라졌다가 같은 노드에서 합류 가능 - 같은 칸에 또 방문할 수 있는 문제라 그래프 사용                                                                                                                                                                                                                                                                    
    
    # 개념 모호
    ## 좌표 표현 방법
    위치는 (행, 열) 쌍으로 표현한다. 보통 변경할 일이 없고 set에 넣는 일이 많아 튜플로 제작
    
    ## 문제를 그래프로 표현한다는 것은 무엇인지
    그래프란 자료구조일 뿐(자료형x) 코드로 다양하게 구현한다
        방법 1: 딕셔너리 (04_bfs.py에서 했던 방식)
        graph = {0: [1, 2], 1: [0, 2], ...}

        방법 2: 2D 리스트 (이번 문제)
        board[r][c] → 값으로 이웃을 계산

        방법 3: 간선 리스트
        edges = [(0, 1), (0, 2), (1, 3)]
        
        이번 문제에서 그래프란 노드: (r, c) 좌표 / 간선: a에서 b 칸으로 갈 수 있다는 관계성 / 이웃(잠재적) (r+n, c), (r, c+n) 도착 노드
    
    ## BFS가 뭐고 어떻게 코드에서 쓰이는지
    가까운 곳부터 차례로 탐색하는 방법 큐 사용(FIFO)
    그냥 리스트를 써도 됨 lst.pop(0) 근데 이건 O(n)로 오래걸림
    
    ## DFS가 뭐고 어떻게 코드에서 쓰이는지
    한방향으로 끝까지 파고드는 방식. 스택, 재귀 사용
    
    ## for 반복문 in list 형태와 range 차이
    꺼내기, 세기
    
    ## visited를 넣지 않으면 발생하는 일
    n이 0이면 같은 값 무한 추가 -> 무한루프
    다른 경로로 같은 칸 도달 -> 다음 경로 중복 탐색
    
    ## 큐는 왼쪽에서 뺄 수 있는 리스트인지
    다름. 큐는 양쪽에서 빠르게 뺄 수 있음
    리스트는 한 줄로 붙은 배열이고, 큐는 연결 리스트라
    
    # 핵심 패턴
    ## 플래그 변수(Flag Variable)
    False True 조건에 주목. 맨 처음 상태를 저장해두는 변수. 특정 조건이 만족되면 성공, 실패 여부를 전달한다. 반복문을 중단하거나 특정 조건문 실행. 변수명은 is_win 같은 식.
    
    ## 중첩 조건문
    if안에 if가 들어가는 구조
    같은 열에도 if를 쓸 수 있다 다만 둘 다 실행될 수 있다. elif는 하나만 실행된다
    r, c = queue.popleft()
    
    ## 인큐 디큐 피크(peek) 동작
    인큐: queue.append(item)
    디큐: queue.popleft()
    피크: queue[i]
    
    ## while 문
    큐가 빌 때까지 = 다음에 갈 칸이 없을 때까지
    
    ## bfs 이웃 찾는 법
---------------------------------------------
    문제 유형	    |   이웃 찾는 방법
---------------------------------------------
    딕셔너리 그래프   | graph[vertex]에서 꺼냄
    격자 (이번 문제) | 칸 값으로 이동량 계산
    격자 (미로)	    |고정 방향 벡터 (상하좌우)
    격자 (8방향)	| 대각선 포함 8개 벡터
    """
    
    """2트
    
    문제정의
    v1 
    v1.2 N x N 격자의 (0,0)에서 출발하여, 현재 칸 값만큼 아래 또는 오른쪽으로 이동할 때, (N-1, N-1)에 도달 가능한지 판별하라 (boolean)
    
    문제 분해
    v1
    - N x N 격자의 (0,0)에서 출발한다
    - 현재 칸 값만큼 아래 또는 오른쪽으로 이동한다
    - 격자를 벗어났으면 False 반환
    - 격자 안이면 이동 후 (N-1, N-1)인지 판별
    - 도달했다면 True 반환
    - 도달하지 않았다면 현재 판별 전까지 2~3 단계 반복
    
    v1.1
    1. N x N 격자의 (0,0)에서 출발, 큐에 넣는다
    2. 큐에서 좌표를 꺼내고 현재 칸 값 n을 읽는다
    3. 아래(r+n, c)와 오른쪽(r, c+n) 두 방향 각각에 대해:
        3-1. 격자 밖이거나 방문했으면 건너뛴다
        3-2. (N-1, N-1)이면 True 반환
        3-3. 아니면 큐에 넣는다
    4. 큐가 빌 때까지 2~3 반복
    5. 큐가 비었는데 도달 못했으면 False 반환
    
    v2
    1. queue = deque([(0, 0)]),  visited = {(0, 0)}
    2. while 큐가 빌 때까지:
        2-1. (r, c) = queue.popleft()
        2-2. n = board[r][c]
        2-3. for (r+n, c) 와 (r, c+n) 각각에 대해:
            if 0 <= nr < N 그리고 0 <= nc < N 그리고 (nr, nc) not in visited:
                if board[nr][nc] == -1 이면 return True
                아니면 큐와 visited에 (nr, nc) 넣는다
    3. return False
    
## 문제 정의 법칙

| 법칙 | 효과 |
|------|------|
| 1. 크기를 수치로 | 경계 체크 조건이 나옴 |
| 2. 위치를 좌표로 | 초기값, 종료 조건이 나옴 |
| 3. 목표를 동사로 | 알고리즘 선택이 가능 |
| 4. 리턴 타입을 명시 | 코드의 끝 모양이 보임 |
| 5. 제약 조건을 포함 | 방향 벡터, 이웃 계산법 결정 |

**공식:** `[크기] + [좌표] + [제약] + [동사] + [리턴 타입]`

---

## 문제 분해 법칙

| 법칙 | 효과 |
|------|------|
| 1. and/or 구분 | 분기 구조 결정 |
| 2. 제어문은 키워드, 조건은 자연어 | 구조는 코드처럼, 읽기는 사람처럼 |
| 3. 들여쓰기 | 코드 구조가 보임 |
| 4. "~할 때까지"로 종료 조건 명시 | while 조건 도출 |
| 5. 성공/실패 종료 조건 둘 다 | 출력 누락 방지 |
| 6. 조건을 수식으로 풀어쓰기 | 코드 변환 시 번역 불필요 |

**2. 제어문별 기술 방법**

| 제어문 | 슈도코드 표현 | 코드 |
|--------|-------------|------|
| for | "각각에 대해:" | `for x in [...]` |
| while | "~할 때까지 반복:" | `while 조건:` |
| if/elif/else | "~이면 / 아니면" | `if / elif / else` |
| break | "즉시 중단" | `break` |
| continue | "건너뛴다" | `continue` |

예시:

```
큐가 빌 때까지 반복:              ← while
    두 방향 각각에 대해:           ← for
        격자 밖이면 건너뛴다       ← if + continue
        (N-1,N-1)이면 즉시 중단   ← if + break
```

---

**3. 구체적 수식 = 문제 정의의 조건을 좌표/숫자로 풀어쓴 것**

```
문제 정의:  "현재 칸 값만큼 아래로 이동"     ← 사람이 읽기 좋음
문제 분해:  "아래 → (r+n, c)"              ← 코드로 옮기기 좋음
코드:       nr, nc = r + n, c              ← 그대로 복붙
```
**6. 조건을 수식으로 풀어쓰기** — 세부 규칙:

| 변환 대상 | 자연어 | 수식 |
|----------|--------|------|
| 방향 | "아래로" | `(r+n, c)` |
| 거리 | "n칸만큼" | `r + n` |
| 범위 | "격자 안" | `0 <= nr < N` |
| 위치 | "끝점" | `(N-1, N-1)` |
| 값 읽기 | "현재 칸 값" | `board[r][c]` |
| 판정 | "도착인지" | `board[nr][nc] == -1` |

---

**규칙: 명사가 나오면 수식으로 바꿀 수 있는지 확인한다**

```
"현재 칸 값만큼"  → 명사: 현재 칸 값 → board[r][c]
"아래로"         → 명사: 아래      → (r+n, c)
"격자를 벗어나면" → 명사: 격자      → 0 <= nr < N
"끝점에 도달"    → 명사: 끝점      → (N-1, N-1)
```

문제 분해를 쓸 때 **명사를 발견할 때마다 "이거 수식으로 바꿀 수 있나?"** 한 번씩 확인하면 돼요!

좋은 질문이에요. 풀이를 모르는 상태에서 문제를 나누는 **사고 과정**을 단계로 정리해볼게요.

---

## 요약: 4가지 질문

| 순서 | 질문 | 얻는 것 |
|------|------|---------|
| 1 | 입력과 출력 사이에 **뭐가 빠져있지?** | 전체 간격 파악 |
| 2 | 출력을 얻으려면 **뭘 알아야 하지?** (거꾸로) | 필요한 단계 도출 |
| 3 | 이게 **하나? 여럿?** | 반복/탐색 구조 결정 |
| 4 | 이 단계를 **알겠어? 모르겠어?** | 더 쪼갤지 결정 |

## 문제 분해 사고법 (4단계)

**1단계: 입력 → 출력 사이의 간격을 본다**

```
입력: N x N 격자
출력: boolean (도달 가능 여부)
간격: 격자를 받아서 어떻게든 도달 여부를 알아내야 함
```

"이 간격을 어떻게 메울까?"가 출발점이에요.

---

**2단계: 간격을 메우려면 뭘 알아야 하는지 질문한다**

핵심 질문: **"출력을 얻으려면 중간에 뭘 알아야 하지?"**

```
도달 가능한지 알려면?
  → 갈 수 있는 경로가 있는지 알아야 함
    → 어디로 갈 수 있는지 알아야 함
      → 현재 칸 값을 읽어야 함
        → 현재 위치를 알아야 함
```

이렇게 **출력에서 거꾸로** 질문을 이어가면 필요한 단계들이 나와요.

---

**3단계: 각 단계마다 "하나? 여럿?" 을 묻는다**

```
갈 수 있는 곳이 하나? 여럿?  → 여럿 (아래, 오른쪽)
확인할 칸이 하나? 여럿?      → 여럿 (경로가 여러 개)
시도가 한 번? 여러 번?       → 여러 번 (반복 필요)
```

- "하나" → 단순 계산
- "여럿" → **반복문 또는 탐색** 필요
- "여럿 + 분기" → **BFS/DFS** 후보

---

**4단계: 모르는 부분만 더 쪼갠다**

전부 다 쪼갤 필요 없어요. **"이건 어떻게 하지?"** 싶은 부분만 한 단계 더 구체화:

```
"갈 수 있는 곳 확인" → 어떻게?
  → 모르겠음 → 더 쪼갬: "칸 값 읽고, 두 방향 좌표 계산"

"큐에서 꺼내기" → 어떻게?
  → 알겠음 → 안 쪼갬
```

---



처음 나눈 게 정답이 아니어도 괜찮아요. 이 4가지 질문을 **반복**하면서 점점 구체화하는 거예요!
    
    """
    
# N x N 격자의 (0,0)에서 출발하여, 현재 칸 값만큼 아래 또는 오른쪽으로 이동할 때, (N-1, N-1)에 도달 가능한지 판별하라 (boolean)

# 1차 수정
N = int(input())
board = [list(map(int, input().split())) for row in range(N)]
queue = deque()
visited = set()

is_win = False

queue.append((0, 0))
r, c = (0, 0)
n = board[r][c]
while queue:
    for dr, dc in [[n, 0], [0, n]]:
        nr, nc = (r + dr, c + dc)
        if nr <= N - 1 and nc <= N - 1 and (nr, nc) not in visited:
            queue.append((nr, nc))
            visited.append((nr, nc))
        elif board[nr][nc] == -1:
            print("HaruHaru")
            is_win = True
        else:
            continue
if is_win == False:
    print("Hing")

# 2차 수정       
N = int(input())
board = [list(map(int, input().split())) for row in range(N)]
queue = deque()
visited = set()

is_win = False

queue.append((0, 0))
r, c = (0, 0)
visited.add((0, 0))
while queue:
    r, c = queue.popleft()
    n = board[r][c]
    for dr, dc in [[n, 0], [0, n]]:
        nr, nc = (r + dr, c + dc)
        if nr <= N - 1 and nc <= N - 1 and (nr, nc) not in visited:
            queue.append((nr, nc))
            visited.append((nr, nc))
        elif board[nr][nc] == -1:
            print("HaruHaru")
            is_win = True
        else:
            continue
if is_win == False:
    print("Hing")           

# 3차 수정
N = int(input())
board = [list(map(int, input().split())) for row in range(N)]
queue = deque()
visited = set()

is_win = False

queue.append((0, 0))
visited.add((0, 0)) # 처음 위치 추가해야 함

while queue:
    r, c = queue.popleft() # 값 갱신을 위해 안에서 정의해야 함
    n = board[r][c]
    
    for dr, dc in [[n, 0], [0, n]]:
        nr, nc = (r + dr, c + dc)
        if nr <= N - 1 and nc <= N - 1 and (nr, nc) not in visited:
            queue.append((nr, nc))
            visited.add((nr, nc)) # set은 add 사용
            if board[nr][nc] == -1: # 들여쓰기
                print("HaruHaru")
                is_win = True # break가 없어서 반복문 계속 실행. 다른 루트가 있으면 중복 print
        else: # 필요없음
            continue
        
if is_win == False:
    print("Hing")

# ai 코드    
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
visited = set()

queue.append((0, 0))
visited.add((0, 0))

is_win = False

while queue:
    r, c = queue.popleft()
    n = board[r][c]

    if n == -1: # 이웃 칸을 큐에 넣으며 -1 체크. 큐에서 꺼낸 것을 처리한다는 원칙에 따라 가장 중요한 것을 먼저. 
        is_win = True
        break # 도달 시 즉시 종료. 중복출력을 방지하고 True 반환 뒤 반복문이 계속 도는 것을 방지함

    for dr, dc in [(n, 0), (0, n)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited: # 여러 경로로 도달한 같은 좌표가 큐에 들어가서 불필요한 연산을 하게 됨. 또한 미로 탐색 등의 4방향 이동 가능 문제에선 무한 루프 문제가 일어날 수 있음.
            
            visited.add((nr, nc))
            queue.append((nr, nc))

print("HaruHaru" if is_win else "Hing") # 출력을 한 곳에서 처리


# 노드 = 칸, 이웃 = 격자 안 도달 가능한 칸

# 시작점을 큐에 넣는다
# 큐에서 꺼낸다
# 칸의 값 만큼 아래와 오른쪽으로 이동한다
# 종료칸에 도착했다면 True
# 이동이 가능한지 확인한다
# 큐가 빌 때까지 반복한다
# 큐가 비었는데 종료칸에 도착하지 못했다면 False
# bool 값에 따라 print


# 인풋 받기
from collections import deque
N = int(input())
board = [list(map(int, input().split() )) for _ in range(N)]

# 시작점 넣기
queue = deque([(0, 0)]) # 소괄호는 그냥 그룹핑 괄호라 deque((0, 0)) 넣으면 0을 각자 따로 저장함. 리스트로 감싸줘야.
# visited = set((0, 0)) # 생성자 방식
visited = {(0, 0)} # 컴프리헨션 방식


is_win = False

# 이동하기
while queue:
    row, col = queue.popleft()
    n = board[row][col]
    for d_row, d_col in ((n, 0), (0, n)):
        next_row, next_col = row + d_row, col + d_col

# 종료칸 판별
        if n == -1:
            is_win = True
            break      
            
# 이동 가능 판별
        elif 0 <= next_row <= N - 1 and 0 <= next_col <= N - 1 and (next_row, next_col) not in visited:
            queue.append((next_row, next_col))
            visited.add((next_row, next_col))
# 출력
if is_win == True: 
    print("HaruHaru")
else:
    print("Hing")
    
# 이동하기
while queue:
    row, col = queue.popleft()
    n = board[row][col]
    
    # 종료칸 판별
    if n == -1:
            is_win = True
            break   
        
    for d_row, d_col in ((n, 0), (0, n)):
        next_row, next_col = row + d_row, col + d_col
         
# 이동 가능 판별
        if 0 <= next_row <= N - 1 and 0 <= next_col <= N - 1 and (next_row, next_col) not in visited:
            queue.append((next_row, next_col))
            visited.add((next_row, next_col))
# 출력
if is_win == True: # if 다음에는 참 거짓을 평가한다 is_win은 boolen이라 True를 써줄 필요가 없음
    print("HaruHaru")
else:
    print("Hing")
    
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def jumpking(row, col):
    # 범위 밖이면 실패
    if not (0 <= row < n and 0 <= col < n):
        return "Hing"

    start = board[row][col]

    # 도착점이면 성공
    if start == -1:
        return "HaruHaru"

    # 이미 방문했으면 실패
    if visited[row][col]:
        return "Hing"

    visited[row][col] = True

    right = jumpking(row, col + start)
    bottom = jumpking(row + start, col)

    if right == "HaruHaru" or bottom == "HaruHaru":
        return "HaruHaru"
    return "Hing"

print(jumpking(0, 0))

# 최적화 코드

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def jumpking(row, col):
    # 범위 밖
    if row >= n or col >= n:
        return False

    # 도착
    if board[row][col] == -1:
        return True

    jump = board[row][col]

    # 오른쪽 또는 아래 중 하나라도 성공하면 성공
    return jumpking(row, col + jump) or jumpking(row + jump, col)

print("HaruHaru" if jumpking(0, 0) else "Hing")


# 우리의 재귀 코드

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 1단계: 이 함수는 무슨 질문에 답하는가?
#   → "(row, col)에서 출발하면 -1에 도달할 수 있는가?"
# 2단계: 바로 답할 수 있는 경우는?
#   → 범위 밖, -1 도착, 이미 방문
# 3단계: 작은 답으로 내 답을 조립할 수 있는가?
#   → 오른쪽/아래 칸이 도달 가능하면 나도 가능

def can_reach(row, col):
    if row >= n or col >= n:
        return False

    if board[row][col] == -1:
        return True

    if visited[row][col]:
        return False

    visited[row][col] = True
    jump = board[row][col]

    return can_reach(row, col + jump) or can_reach(row + jump, col)

print("HaruHaru" if can_reach(0, 0) else "Hing")


# 내가 처음부터 재귀로 푼다면

# 인풋
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = set()

# solve(r, c): "(r, c)에서 출발하면 -1에 도달할 수 있는가?"
def solve(r, c):
    # base case 1: 범위 밖 → 도달 불가
    if r >= n or c >= n:
        return False
    # base case 2: -1 칸 도착 → 도달 성공
    if board[r][c] == -1:
        return True
    # base case 3: 이미 간 곳 → 다시 탐색 안해도 됨
    if (r, c) in visited:
        return False

    visited.add((r, c)) # else 생략 조기반환 패턴
    jump = board[r][c]
    # 오른쪽/아래 중 하나라도 도달 가능하면 True (or 단축 평가)
    return solve(r, c + jump) or solve(r + jump, c)

# 출력
print("HaruHaru" if solve(0, 0) else "Hing")


# memo(캐싱) 버전
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
memo = {}

# solve(r, c): "(r, c)에서 출발하면 -1에 도달할 수 있는가?"
def solve(r, c):
    if r >= n or c >= n:
        return False
    if board[r][c] == -1:
        return True
    if (r, c) in memo:
        return memo[(r, c)]

    memo[(r, c)] = False
    jump = board[r][c]
    result = solve(r, c + jump) or solve(r + jump, c)
    memo[(r, c)] = result
    return result

print("HaruHaru" if solve(0, 0) else "Hing")



n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = set()

def solve(r, c):
    if r >= n or c >= n: return False
    if board[r][c] == -1: return True
    if (r, c) in visited: return False
    
    visited.add((r, c))
    jump = board[r][c]
    
    return solve(r + jump, c) or solve(r, c + jump) # 다음 점프들도 어느 순간에 base case에 도착

print("HaruHaru" if solve(0, 0) else "Hing") # 삼항 연산자는 else 필요