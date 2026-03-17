# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

# input 받아와서 이차원 배열 paper 만들기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 색 개수 초기화
white, blue = 0, 0

# 4분할 하고 색 개수 저장하는 재귀함수 정의
def divide(x, y, size):
    global white, blue
    all_same = True
    color = paper[y][x]
## 순회하며 기준점 색과 같으면 True, 다르면 False 뒤 break
    for j in range(y, y+size):
        for i in range(x, x+size):
            if color != paper[j][i]:
                all_same = False
                break
        if all_same == False:
            break

## 기준점 색과 같을 때 색 개수 업데이트
    if all_same == True:
        white += 1 if color == 0 else 0
        blue += 1 if color == 1 else 0
        return

## 기준점 색과 다를 때 색종이 분할
    half = size // 2
    for dx in range(2):
        for dy in range(2):
            divide(x + dx * half, y + dy * half, half)

# 실행 및 출력
divide(0, 0, N)
print(white)
print(blue)



# # input 받아와서 이차원 배열 paper 만들기
# N = input()
# paper = [list(map(int, input().split())) for _ in range(N)]

# # 색 개수 초기화
# white, blue = 0, 0

# # 4분할 하고 색 개수 저장하는 재귀함수 정의
# def divide(x, y, size):
#     all_same = True
    
# ## 순회하며 기준점 색과 같으면 True, 다르면 False 뒤 break
#     for i in range(size):
#         for j in range(size):
#             if paper[x][y] != paper[i][j]:
#                 all_same = False
#                 break
#     if all_same == False:
#         break

# ## 기준점 색과 같을 때 색 개수 업데이트
#     if all_same == True:
#         white += 1 if paper[x][y] == 0 
#         blue += 1 if paper[x][y] == 1

# ## 기준점 색과 다를 때 색종이 분할
#     half = size // 2
#     for i in range(2):
#         for j in range(2):
#             x + half * i

# # 실행 및 출력
# divide(0, 0, N)
# print(white)
# print(blue)

# [색종이 만들기 - 핵심 요약]

# 1. 분할 정복 순서
#    판단 먼저 → 같으면 카운트+return, 다르면 4분할 재귀

# 2. 재귀 인자: divide(x, y, size)
#    x=열, y=행, size=한 변 길이 / 첫 호출: divide(0, 0, N)

# 3. 2차원 배열: paper[y][x] (행 먼저, 열 나중)
#    바깥 루프=행(y), 안쪽 루프=열(x)

# 4. all_same 판별
#    루프 전 True → 다른 색 발견 시 False+break(안쪽) → if not all_same: break(바깥)

# 5. 4분할: dy, dx 각각 range(2) → 4조합 = 4사분면 자동 커버
#    half = size // 2  (/는 float → 인덱스 불가, //필수)

# 6. global 선언
#    읽기만: 불필요 / 수정(+=): 필수 → 없으면 UnboundLocalError

# 7. 삼항연산자
#    [참] if [조건] else [거짓] — else 필수, 문장(+=) A자리 불가

# 8. return 위치: if all_same 블록 안 (밖으로 나오면 항상 종료)

# 9. white, blue = 0, 0 → 함수 밖에서 딱 한 번 (안에서 하면 재귀마다 리셋)



