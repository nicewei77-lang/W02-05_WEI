# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

"""
<이분탐색 - 수 찾기>
    
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5

예제 출력 1 
1
1
0
0
1
"""
# 문제분석 #
# 검색은 이분탐색으로
# 순회하면서 출력
# 필요한 것들은 리스트 두개, 리스트 길이 두개, mid 한개

# 질문 #
# 이분탐색 어떻게 했더라?
# 반복문에서 쓴 변수는 어떻게 되는가?
# 함수? 인자?
# 코드 쓰는 단계. 주석부터?
# 정렬이 되어있어야 했나?
"""
# 오답 #
N =int(input())
array_1 = [int(input()) for i in range(N)]
M = int(input())
array_2 = [int(input()) for j in range(M)]

def find_num(arr):
    while len(arr) = 1:
        mid = arr // 2
        for num in array_2:
            if num <= mid
            if num in array_1:
                print(1)
find_num(array_1)
"""

# 정답 #

# 리스트 만들기, 정렬
N = int(input())
list_A = map(int, input().split)
list_A.sort()

# lo/hi 초기화, 반복 조건 설정

def binary_sort(target, arr): 
    lo = 0 # 초기화는 반복문 밖에서
    hi = N - 1
    while lo < hi:

# mid 계산, target과 비교
        mid = (lo + hi) // 2
        if target == arr[mid]:
            return 1

# lo/hi 로 탐색 범위 좁히기
        elif target < arr[mid]:
            hi = mid - 1
        elif target > arr[mid]:
            lo = mid + 1
    return 0
        
# 다음 M개 원소 순회하며 결과 출력
M = int(input())
for num in map(int, input().split()):
    print(binary_sort(num, list_A)) # 실행한 함수를 print에 넣어서 함수 결과 바로 출력 가능

# 파슨스 질문 #
# 진행순서
# 재귀는 쓰이지 않는지
# - 두 가지 구현 방식이 있다 반복문: 루프로 범위를 좁혀감 / 재귀는 자기 자신을 호출(arr, target, lo, hi)
# mid가 어디로 정해지는지 감이 안옴 
# - 원소 개수가 홀수일 경우 정중앙 예시: (0+6)//2=3 0 1 2 [3] 4 5 6
# - 짝수라면 왼쪽 중앙으로 간다 예시: (0+5)//2=2   0 1 [2] 3 4 5
# mid는 탐색 범위에서 어떻게 되는가?
# - 비교 결과에 따라 다음 탐색 범위에서 제외된다. 포함시키거나 제외한다는 검사가 끝나기 때문에.
# 이분탐색에선 항상 함수를 만드는가?: 만들지 않고 반복문에서 바로 print() 가능. 
# 재귀와 반복문의 인자 차이: 검색 범위를 다음 호출에 넘겨야 해서 인자로 받는다 hi, lo
# 쿼리?: 찾고 싶은 값 하나
# 이진 탐색에 필요한 인자는 arr, target

# 팁 #
# if __name__ == "__main__":은 "이 파일이 직접 실행될 때만 아래 코드를 돌려라"라는 뜻

"""
순서: 함수정의 - 호출
보는 순서: 맨 밑 - 메인 로직 - 보조 함수
래퍼함수: 인자 개수 감소 장점, 데이터 전처리나 데이터 검증을 수행
헬퍼함수: 반복되는 계산 따로 떼어놓은 것, 초기화도 여기서

def solution():      # 메인 로직
    ...

def helper():        # 보조 함수
    ...

solution()           # 진입점, 맨 밑
"""

# 확인질문 #

