"""
[머지 정렬 구현]

문제 설명:
- 머지 정렬(Merge Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 배열을 절반으로 나누고, 각각을 정렬한 후 병합합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [38, 27, 43, 3, 9, 82, 10]
출력: [3, 9, 10, 27, 38, 43, 82]

힌트:
- 배열을 절반으로 분할 (재귀)
- 각 부분을 재귀적으로 정렬
- 정렬된 두 부분을 병합
"""

def merge(arr, left, mid, right):
    """
    두 개의 정렬된 부분 배열을 병합하는 함수
    
    Args:
        arr: 원본 배열
        left: 왼쪽 부분의 시작 인덱스
        mid: 왼쪽 부분의 끝 인덱스
        right: 오른쪽 부분의 끝 인덱스
    """
    # TODO: 왼쪽과 오른쪽 부분 배열을 임시 배열로 복사
    
    left_buff = arr[left:mid+1]
    right_buff = arr[mid+1:right+1]
    
    # TODO: 포인터 초기화
    i, j, k = 0, 0, left
    
    
    # TODO: left_arr와 right_arr를 비교하며 작은 값을 arr에 복사
    while i < len(left_buff) and j < len(right_buff):
        if left_buff[i] < right_buff[j]:
            arr[k] = left_buff[i]
            i += 1
        else:
             arr[k] = right_buff[j]
             j += 1
        k += 1
    
    # TODO: 남은 원소들을 복사
    # left_buff에 남은 원소가 있으면 복사
    # right_buff에 남은 원소가 있으면 복사
    while i < len(left_buff):
        arr[k] = left_buff[i]
        i += 1
        k += 1

    while j < len(right_buff):
        arr[k] = right_buff[j]
        j += 1
        k += 1

def merge_sort_helper(arr, left, right):
    """
    머지 정렬 재귀 함수
    
    Args:
        arr: 배열
        left: 시작 인덱스
        right: 끝 인덱스
    """
    # TODO: base case - left가 right보다 작을 때만 정렬
    ## 중간 지점 계산
    ## 왼쪽 절반 재귀 정렬
    ## 오른쪽 절반 재귀 정렬
    ## 정렬된 두 절반을 병합
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(arr, left, mid)
        merge_sort_helper(arr, mid + 1, right)
        merge(arr, left, mid, right)
        
def merge_sort(arr):
    """
    머지 정렬 메인 함수
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    if len(arr) > 1:
        merge_sort_helper(arr, 0, len(arr) - 1)
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 역순
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = merge_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 중복 원소
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("=== 테스트 케이스 4: 중복 원소 ===")
    print(f"정렬 전: {arr4}")
    result4 = merge_sort(arr4.copy())
    print(f"정렬 후: {result4}")


# 병합 방식: 왼쪽만 buff에 두는 방식 vs 왼쪽/오른쪽 둘 다 임시 배열로 복사하는 방식이 있음. 이 문제는 후자(left_buff, right_buff 모두 생성)를 요구함. 결과는 동일하고 구현 방식만 다름.
# 왼쪽/오른쪽 정렬 주체: merge_sort_helper가 재귀로 분할하며 알아서 정렬함. merge 호출 시점엔 이미 두 쪽이 각각 정렬 완료된 상태임.
# 병합 후 남은 원소: 한 쪽이 먼저 소진되면 나머지 쪽에 원소가 여러 개 남을 수 있음. 남은 원소들은 이미 정렬된 상태이므로 순서대로 arr에 붙이면 됨.
# while 조건 순서: j >= 0 and arr[j] > key처럼 범위 체크를 앞에 써야 함. and는 왼쪽부터 평가하므로 j >= 0이 False면 arr[j] 접근 자체를 안 함(단락평가).
# k 초기값: k = left로 시작해야 함. 재귀 분할 후 merge가 호출될 때 left가 0이 아닐 수 있어서, k=0으로 시작하면 엉뚱한 자리(arr[0])부터 덮어씀.
# 함수 실행 순서: merge_sort → merge_sort_helper(재귀 분할) → merge. merge는 항상 가장 마지막에 호출됨. 재귀가 바닥(원소 1개)까지 내려간 후 올라오면서 병합함.
