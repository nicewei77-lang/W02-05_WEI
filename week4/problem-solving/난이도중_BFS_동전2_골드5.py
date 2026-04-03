# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

"""
    문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

예제 입력 1 
3 15
1
5
12
예제 출력 1 
3
 I: 동전종류 n int / 가격 k int
 O: 동전의 최소 개수 int / 불가능할시 -1
조건: 같은 동전 여러개 주어질 수 있다

문제정의: 동전 종류와 가격이 주어졌을 때 합으로 k원을 만드는 동전의 최소 개수 n을 구하라

만들 수 있는지 판별
조합 만들기
가장 적은 조합 저장 - 가장 작은지 판별, 작은거 저장



순회를 하면서 합이 k True
k 초과 false

k 미만 

재귀함수



스택에 넣기
넣으면서 

    """
from collections import deque
   
queue = deque()
n, k = map(int, input().split())
result = []
shortest = float('inf')
for _ in range(n):
        queue.append(int(input()))

def plus_coin(arr, result):
    global shortest
    for i in queue:
        result.append(i)
        
        if sum(result) == k:
                shortest = min(shortest, len(result))  
        elif sum(result) < k:
            plus_coin(queue, result)
       
        result.pop()   
    return shortest

plus_coin(queue, result)
print(shortest if shortest != float('inf') else -1)

# ============================================
# [재귀/백트래킹 실수 정리 - 다음에 꼭 기억할 것]
# ============================================
#
# 1. 백트래킹 = append → 탐색 → pop
#    - 재귀 호출 후 반드시 pop()으로 되돌려야 한다
#    - 안 하면 이전 경로의 결과가 다음 경로에 오염됨
#
# 2. return / continue는 pop()을 건너뛸 수 있다
#    - 조건 분기 안에서 return이나 continue를 쓰면
#      pop()이 실행되지 않아 백트래킹이 깨진다
#    - 해결: 모든 분기가 끝난 뒤 pop()이 항상 실행되게 구조를 짜기
#
# 3. 최소값 갱신은 "정답 확인 → 비교" 순서
#    - 먼저 sum == k인지 확인하고, 그 안에서 min()으로 갱신
#    - 순서가 뒤바뀌면 정답이 아닌 경우에도 갱신하게 됨
#
# 4. 최솟값 추적은 리스트보다 단순 변수가 낫다
#    - shortest = float('inf') → shortest = min(shortest, len(result))
#    - 리스트로 하면 append/pop/인덱스 접근이 꼬이기 쉬움
#
# 5. global 사용법
#    - 함수 밖에서는 그냥 변수 선언 (global 키워드 X)
#    - 함수 안에서 전역 변수를 "수정"할 때만 global 선언
#
# 6. 함수의 역할과 출력을 분리하기
#    - 함수는 탐색만 하고, print는 함수 밖에서
#    - 함수 안에 print를 넣으면 재귀할 때마다 출력됨
#
# 7. 재귀 풀이의 한계: Python 재귀 깊이 제한 (기본 1000)
#    - sys.setrecursionlimit()으로 늘릴 수 있지만
#    - 근본적으로 BFS/DP가 이 유형에는 더 적합함
#    - "합계 = 노드, 동전 하나 추가 = 간선" → BFS 최단거리
# ============================================

n, k = map(int, input().split())
num = 0
won = 0
wallet = deque([[0, 0]])
visited = []
n_coins = [int(input()) for i in range(n)]

while won != k:
    for i in range(1, 10000): # num이 1씩 늘어남
        for j in n_coins:
            coin = wallet.popleft() # 큐에서 coin pop
            num, won = coin # num, won 만들기
            num = i
            won += j
            if (num, won) not in visited:
                wallet.append([num, won]) # 큐에 coin 넣기
                visited.append((num, won))# 방문록에 coin 넣기
print(num) # num 반환

# ============================================
# [BFS 풀이 피드백 정리]
# ============================================
#
# 1. deque().append()는 None을 반환한다
#    - deque().append(x) 의 결과를 변수에 담으면 None이 들어감
#    - 초기화는 deque([[0, 0]]) 처럼 생성자에 직접 넣기
#
# 2. append()는 인자를 하나만 받는다
#    - append(num, won) → TypeError
#    - append([num, won]) 으로 리스트 하나를 넣어야 함
#
# 3. BFS 구조: while + popleft가 핵심
#    - while 큐가 비어있지 않을 때:
#        꺼낸다 (popleft)
#        각 동전에 대해:
#            새 합계 계산
#            k면 → 정답 출력 후 종료
#            k 미만이고 미방문 → 큐에 넣기
#    - for i in range(1, 10000) 같은 건 필요 없음
#    - 큐에서 꺼내는 순서 자체가 BFS의 탐색 순서를 결정함
#
# 4. 상태를 단순화하면 더 쉽다
#    - [num, won] 쌍 대신 "합계(won)"만 큐에 넣어도 됨
#    - 동전 수(num)는 BFS의 "레벨"로 셀 수 있음
#    - 처음 k에 도달한 레벨 = 최소 동전 수
#
# 5. visited는 set + tuple이 빠르다
#    - 리스트의 in 검사는 O(n), set의 in 검사는 O(1)
#    - visited = set() → visited.add(won)
# ============================================

# while 큐가 비어있지 않을 때:
#     하나 꺼낸다 (popleft)
#     각 동전에 대해:
#         새 합계를 계산한다
#         k면 → 정답
#         k 미만이고 미방문이면 → 큐에 넣는다

n, k = map(int, input().split())
wallet = deque([0])
visited = ()
n_coins = [int(input()) for i in range(n)]
level = 0

while wallet:
    level += 1
    for _ in range(len(wallet)):
        won = wallet.popleft()
        for coin in n_coins:
            new_won = won + coin
            if new_won == k:
                print(level)
            elif new_won < k and new_won not in visited:
                wallet.append(new_won)

# ============================================
# [BFS 풀이 - 큐에 (상태, 거리) 같이 넣는 방식]
# ============================================
# 레벨 관리 없이, 기본 BFS 뼈대 그대로 사용
# 큐에 (합계, 동전수) 튜플을 넣어서 거리를 함께 추적

from collections import deque

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
visited = set()
queue = deque([(0, 0)])   # (합계, 동전수)
visited.add(0)

while queue:
    won, count = queue.popleft()       # 기본 뼈대: 꺼낸다
    for coin in coins:                 # 기본 뼈대: 이웃을 본다
        new_won = won + coin
        if new_won == k:               # 종료 조건
            print(count + 1)
            exit()
        elif new_won < k and new_won not in visited:
            visited.add(new_won)        # 기본 뼈대: 미방문이면
            queue.append((new_won, count + 1))  # 큐에 넣는다

print(-1)  # 큐가 비었는데 못 찾음 → 불가능

# ============================================
# [비교]
# 레벨 방식: for _ in range(len(queue)) + level 변수 따로 관리
# 튜플 방식: 큐에 거리를 같이 넣어서 기본 뼈대 그대로 사용
# 결과는 동일, 익숙한 걸 쓰면 됨
# ============================================



queue = deque()
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
visited = set()
cur = 0
level = 0
queue.append(coins[0])
visited.add(coins[0])

while queue:
    level += 1
    for i in range(len(queue)):
        cur = queue.popleft()
        
        for coin in coins:
            if cur + coin == k:
                print(level)
                break # exit()
            
            elif cur + coin < k and (cur + coin) not in visited:
                visited.add(cur + coin)
                queue.append(cur + coin)
print(-1)

n, k = map(int, input().split())
wallet = deque([0])
visited = ()
n_coins = [int(input()) for i in range(n)]
level = 0

while wallet:
    level += 1
    for _ in range(len(wallet)):
        won = wallet.popleft()
        for coin in n_coins:
            new_won = won + coin
            if new_won == k:
                print(level)
            elif new_won < k and new_won not in visited:
                wallet.append(new_won)