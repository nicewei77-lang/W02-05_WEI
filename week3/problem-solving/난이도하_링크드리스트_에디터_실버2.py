# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

dummy = Node(None)
cursor = dummy
initial = input()
n = len(input())
commands = [input() for _ in range]

for ch in initial:
    node = Node(ch)
    node.prev = cursor # node 왼쪽 칸은 커서
    cursor.next = node # 커서 오른쪽 칸은 노드
    cursor = node # 커서는 노드(이동)

for cmd in commands: # commands 순회
    if cmd == 'L': # L 일 때
        if cursor != dummy: # cursor가 더미가 아니라면
            cursor = cursor.prev # 커서를 왼쪽으로 옮긴다
    elif cmd == 'D': # D 일 때
        if cursor.next: # 커서 오른쪽에 요소가 있다면
            cursor = cursor.next # 커서를 오른쪽으로 옮긴다
    elif cmd == 'B': # B 일 때
        if cursor != dummy: # 커서가 더미가 아니라면(문장의 맨 앞이 아닐 때)
            cursor.prev.next = cursor.next # 커서 노드 삭제(prev에게 next봐)
            if cursor.next: # 커서 노드 삭제 - 다음 노드 있을 때(next에게 prev봐)
                cursor.next.prev = cursor.prev
            cursor = cursor.prev # 삭제 후 커서 왼쪽으로 옮기기
    elif cmd[0] == 'P': # P 일 때
        node = Node(cmd[2]) # 명령어 노드 생성
        node.prev = cursor # prev 속성은 cursor(추가 전 마지막 요소)
        node.next = cursor.next # next 속성 교체
        if cursor.next: # 커서 다음 요소가 있다면
            cursor.next.prev = node # 커서 next 노드의 prev 속성 교체
        cursor.next = node # 커서 next 속성 교체
        cursor = node # 커서 옮기기

result = []
cur = dummy.next # 처음 빈 공간의 다음 노드
while cur: # 마지막 요소까지
    result.append(cur.data) # 노드의 data를 결과에 추가
    cur = cur.next # 다음 노드
print(''.join(result)) # 빈 문자열로 이음(.join은 무조건 조건 써야 함)

"""
# node의 prev, next 속성
비유하면 노드는 쪽지:
```
┌─────────────┐
│ data = 'a'  │
│ next = ___  │  ← 오른쪽 노드 적는 칸
│ prev = ___  │  ← 왼쪽 노드 적는 칸
└─────────────┘

# 커서의 개념

# self.next = None 초기화

# 문제와 코드의 간격

"""


# [연결 리스트 커서 에디터 핵심 요약]

# 1. 노드의 .next .prev는 파이썬이 주는 게 아니라 __init__에 직접 만든 칸.
# 2. Node() 호출마다 self는 그때 만들어진 객체. 100번 호출하면 100번 바뀜.
# 3. 더미 헤드 = 커서가 맨 앞일 때 가리킬 노드. cursor != dummy로 맨 앞 체크.
# 4. cursor = dummy는 "이름표를 dummy에 붙여". 이동이 아님.
# 5. node.prev = cursor는 "연결". cursor = node는 "이동". = 의 역할이 다름.
# 6. 양방향 연결은 양쪽 다 써야 함. 한쪽만 쓰면 한 방향만 이동 가능.
# 7. 문제의 "커서" = | 기호. 코드의 cursor = | 바로 왼쪽 노드. 약속임.
# 8. cursor = None은 삭제 아님. 삭제 = 주변 노드가 cursor를 건너뛰도록 포인터 변경.
# 9. cursor.next가 None일 때 cursor.next.prev 접근하면 터짐. if cursor.next 조건 필수.
# 10. "커서 왼쪽에 추가"(문제) = "cursor 오른쪽에 삽입"(코드). 같은 말.
# 11. cmd[0]='P', cmd[1]=' ', cmd[2]='x'. 문자는 cmd[2]로 꺼냄.
# 12. ''.join(list) = 리스트를 문자열로 합침. 앞의 ''가 구분자. 그냥 .join은 문법 오류.
