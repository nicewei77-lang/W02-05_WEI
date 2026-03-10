"""
[삽입 정렬 구현]

문제 설명:
- 삽입 정렬(Insertion Sort) 알고리즘을 구현합니다.
- 정렬된 부분에 새로운 원소를 적절한 위치에 삽입하는 방식입니다.
- 카드 게임에서 손에 든 카드를 정렬하는 방식과 유사합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [12, 11, 13, 5, 6]
출력: [5, 6, 11, 12, 13]

힌트:
- 첫 번째 원소는 이미 정렬되어 있다고 가정
- 두 번째 원소부터 시작하여 앞의 정렬된 부분에 삽입
- 삽입 위치를 찾기 위해 뒤에서 앞으로 비교
"""


def insertion_sort(arr):
    """
    삽입 정렬 구현

    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)

    # TODO: 두 번째 원소(인덱스 1)부터 시작
    ## 각 원소를 정렬된 부분에 삽입
    ## 현재 원소를 key에 저장
    ## key를 삽입할 위치 찾기
    ## j는 key 바로 앞 인덱스부터 시작
    ## arr[j] > key인 동안 원소를 오른쪽으로 이동
    ## 찾은 위치에 key 삽입
    for i in range(1, n):
        key = arr[i] #포인터는 계속 왼쪽으로 이동하는데 0보다 작아지면 완전히 반대인 오른쪽 끝으로 간다 + 인덱스 i로 지금 선택해서 삽입할 원소를 key로 지정
        j = i - 1 # i의 바로 앞 원소인 j부터 앞->뒤로 i와 비교. j는 지금 비교하는 원소의 인덱스. 정렬된 부분의 마지막부터 비교 시작
        while j >= 0 and arr[j] > key: # 포인터가 key 보다 클 때만 원소를 오른쪽으로 이동
            arr[j + 1] = arr[j]
            j -= 1 # while이 돌 때마다 이동을 오른쪽->왼쪽으로 진행
        arr[j + 1] = key # i=2일 때 while 안들어감 - 원리 자리인 arr[2]에 key 다시 들어감

    return arr

    # 이미 정렬된 [1,2,3,4,5] 넣으면?
    ## 계속 arr[j] < key=arr[i]라서 while이 실행이 안되며, key는 제자리로 들어간다.

    # j가 정방향이 아닌 이유
    ## 오른쪽→왼쪽은 "key보다 크다 = 밀어야 한다"가 일치하기 때문에 탐색과 이동이 같은 조건으로 동시에 처리돼.

def insertion_sort_with_steps(arr):
    """
    과정을 출력하는 삽입 정렬
    """
    n = len(arr)
    print(f"초기 배열: {arr}")

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        print(f"\nStep {i}: key = {key}")
        print(f"정렬된 부분: {arr[:i]}")

        # TODO: 삽입 위치 찾기 및 이동
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"삽입 후: {arr}")

    return arr


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [12, 11, 13, 5, 6]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = insertion_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    # 테스트 케이스 2: 과정 출력
    arr2 = [5, 2, 4, 6, 1, 3]
    print("=== 테스트 케이스 2: 정렬 과정 ===")
    result2 = insertion_sort_with_steps(arr2.copy())
    print()

    # 테스트 케이스 3: 이미 정렬된 배열
    arr3 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 3: 이미 정렬됨 ===")
    print(f"정렬 전: {arr3}")
    result3 = insertion_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print("이미 정렬된 경우 O(n) 시간 소요")
