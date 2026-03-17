# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""

# 정답
import sys
input = sys.stdin.readline
N = int(input())
stack = []
result = []
for x in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        result.append(stack.pop() if stack else -1)
    elif command[0] == 'size':
        result.append(len(stack))
    elif command[0] == 'empty':
        result.append(0 if stack else 1)
    elif command[0] == 'top':
        result.append(stack[-1] if stack else -1)
print('\n'.join(map(str, result)))

# 오답
# N = int(input())
# stack = []
# result = []
# for x in range(N):
#     command = x.split()
#     if command[0] == 'push':
#         stack.append(command[1])
#     elif command == 'pop':
#         result.append(stack.pop() if stack else -1)
#     elif command == 'size':
#         result.append(len(stack))
#     elif command == 'empty':
#         result.append(0 if stack else 1)
#     elif command == 'top':
#         result.append(stack[-1] if stack else -1)
# print("'/n'.join(map(str, result))")

    """
    백준 스택(Stack) 문제 핵심 요약
1. sys.stdin.readline의 시작

시스템 표준 입력 통로(stdin)에서 줄바꿈(\n)을 만날 때까지 데이터를 한 번에 긁어옴.
input()보다 훨씬 빨라 대량 입력(1만 건 이상) 시 시간 초과 방지의 필수템.

2. .split()의 스마트한 처리

공백, 탭, 줄바꿈(\n)을 모두 '화이트스페이스'로 인식해 깔끔하게 잘라 리스트로 반환.
괄호 안에 아무것도 넣지 않아야 연속된 공백이나 끝의 줄바꿈까지 완벽하게 무시함.

3. int() 형변환의 범위

숫자 모양의 문자열("10")만 정수로 바꿀 수 있으며, 명령어("push")에 적용 시 ValueError 발생.
split() 결과 리스트에서 숫자가 위치한 인덱스(예: cmd[1])에만 선택적으로 적용해야 함.

4. if not stack (비어있는 리스트 체크)

파이썬에서 리스트가 비어있으면 False, 값이 있으면 True로 취급되는 특성 활용.
pop이나 top을 수행하기 전, IndexError를 막기 위한 가장 파이썬답고(Pythonic) 빠른 안전장치.

5. 리스트 인덱스 -1 (Top 구현)
리스트의 가장 마지막 요소를 가리키는 음수 인덱스.
데이터를 실제로 삭제하지 않고 '가장 위에 있는 값'만 확인해야 하는 top 명령에 최적.

6. for _ in range(N)의 의도
반복 횟수는 중요하지만 루프 안에서 숫자(0, 1, 2...) 자체를 쓸 일이 없을 때 사용.
"이 변수는 무시한다"는 의미를 전달하여 코드의 가독성을 높임.
    

[Python Stack & Input Parsing 핵심 요약]

1. sys.stdin.readline 사용 이유
   - input()보다 빠름. N이 클 때(10,000+) 시간 초과 방지용 표준 패턴.
   - 반드시 sys import 후 input = sys.stdin.readline 으로 덮어써야 함.

2. input().split()의 동작
   - 공백과 줄바꿈(\n)을 동시에 제거하고 리스트로 반환.
   - "push 5\n" → ["push", "5"], "pop\n" → ["pop"]
   - 결과가 항상 리스트이므로 cmd[0], cmd[1]로 꺼내야 함.
   - cmd == "pop" 은 False (리스트 vs 문자열), cmd[0] == "pop" 이 True.

3. push 시 int() 변환 필수
   - split() 결과는 항상 문자열. cmd[1]은 "5"이지 5가 아님.
   - stack.append(int(cmd[1])) 으로 저장해야 숫자로 출력됨.

4. 삼항 연산자 (조건 표현식)
   - 구조: [참일 때 값] if [조건] else [거짓일 때 값]
   - stack.pop() if stack else -1
     → 스택에 원소가 있으면 pop, 없으면 -1 반환.
   - 빈 리스트는 False, 원소가 있으면 True로 평가됨.

5. empty 명령의 반전 주의
   - 0 if stack else 1
   - "비어있으면 1"이므로 참/거짓이 일반 케이스와 반대.

6. 출력 시 슬래시 방향 주의
   - '\n'.join(...) : 줄바꿈 (백슬래시)
   - '/n'.join(...) : 그냥 문자 /n (슬래시) — 흔한 오타
"""  
    
