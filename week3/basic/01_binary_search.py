"""
[이분 탐색 - Binary Search]

문제 설명:
- 정렬된 배열에서 특정 값을 찾는 이분 탐색 알고리즘을 구현합니다.
- 배열을 반으로 나누어 탐색 범위를 절반씩 줄여갑니다.

입력:
- arr: 정렬된 정수 배열
- target: 찾고자 하는 값

출력:
- target이 있는 인덱스 (없으면 -1)

예제:
입력: arr = [1, 3, 5, 7, 9, 11, 13], target = 7
출력: 3

힌트:
- left, right 포인터 사용
- mid = (left + right) // 2
- arr[mid]와 target 비교하여 범위 조정
"""

def binary_search(arr, target):
    """
    이분 탐색 구현
    
    Args:
        arr: 정렬된 배열
        target: 찾을 값
    
    Returns:
        target의 인덱스 (없으면 -1)
    """
    # 검색범위의 시작과 끝점 설정
    left = 0
    right = len(arr) - 1
    
    # TODO: left가 right보다 작거나 같을 때까지 반복
    ## 중간 인덱스 계산
    ## arr[mid]와 target 비교
    ## 같으면 mid 반환
    ## target이 더 크면 left = mid + 1
    ## target이 더 작으면 right = mid - 1
    while True:
        # mid 갱신, 검색 성공여부 확인. 맞다면 mid 반환.
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid
        # target이 중간값보다 오른쪽에 있는지 확인. 맞다면 검색 시작점 갱신.
        elif arr[mid] < target:
            left = mid + 1
        # target이 중간값보다 왼쪽에 있는지 확인. 맞다면 검색 끝점 갱신.
        else:
            right = mid - 1
        
        # 검색 실패 조건 확인. 맞다면 반복문 종료 후 -1 반환
        if left > right: 
            break
    return -1

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    target1 = 7
    result1 = binary_search(arr1, target1)
    print(f"배열: {arr1}")
    print(f"찾는 값: {target1}")
    print(f"결과: 인덱스 {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target2 = 14
    result2 = binary_search(arr2, target2)
    print(f"배열: {arr2}")
    print(f"찾는 값: {target2}")
    print(f"결과: 인덱스 {result2}")
    print()
    
    # 테스트 케이스 3: 없는 값
    arr3 = [1, 3, 5, 7, 9]
    target3 = 6
    result3 = binary_search(arr3, target3)
    print(f"배열: {arr3}")
    print(f"찾는 값: {target3}")
    print(f"결과: 인덱스 {result3}")

""" TIP """
# 1. return과 break의 차이: return은 함수 내부에서만 쓰이고 값을 반환한다. break는 반복문에서만 사용된다. 여기서 return은 함수안에 반복문이 있기 때문에 사용하였다.
# 2. while True 문의 의미: 원래 'while 조건:' 같은 형식으로 사용하지만 조건 대신 무조건 True로 판단되면 무한 루프가 시작된다. 반복문 내부 코드가 전부 실행되면 다시 반복문 바로 다음 코드부터 실행한다. 이 경우 break로 탈출하는 구간이 있다.
# 3. return -1의 의미: 문제가 발생했거나 찾는 값이 없다는 뜻으로 사용
# 4. pl or pr: 이진 탐색에서는 mid 기준 key 값의 위치를 기반으로 검색 시작점 or 끝점 하나만 수정한다
# 5. 요소 or 인덱스 비교: 햇갈린다면 비교하는 대상을 생각한다. 비교 대상에 요소(target)가 포함되어 있다면 요소를, 인덱스끼리만 비교한다면 인덱스로 비교한다
# 6. 중복 if는 가능한가?: if 문은 여러번 등장해도 된다. 각 if 문을 순차적으로 처리한다. 그렇기 때문에 이 코드에서 return이 없다면(target 위치 특정x) 무조건 다음 검색 실패 여부 판단 if문을 실행한다
# 7. while문 다른 방법: while left <= right: 으로 설정할 수도 있지만 현재 방식의 장점이 있다 1: 순차적인 인간적 사고: 일단 범위를 좁히는 작업을 하고(A), 그 결과 범위가 역전되었다면 멈춰라(B) / 2: 탐색과 탐색실패가 명확히 나뉘어 가독성이 높다

""" 오류 """
# 1. typeError 발생: python에서 인덱스는 반드시 정수여야 한다. 그러므로 48줄에서 /(실수반환) 대신 //(정수 몫만 반환)을 사용해야 한다