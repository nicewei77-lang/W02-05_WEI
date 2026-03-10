# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

numbers = [int(input()) for i in range(9)]
# 반복해서 꺼내기
max = numbers[0]
max_index = 1
n = len(numbers)
for i in range(n - 1):
    if numbers[i + 1] > max:
        max = numbers[i + 1]
        max_index = i + 2
print(max)
print(max_index)

# 오류 1. input을 정수로 변환 안 함
# 오류 2. numbers[i+1] > max를 numbers[i+1] > i로 잘못 씀
# 오류 3. print 안에 변수가 아닌 문자열 리터럴을 출력
# 오류 4. 출력 변수명 불일치 max를 max_val이라 씀
# 오류 5. 반복문 전에 변수를 선언하지 않아. 최대값이 첫 번째 인덱스에 있는 경우 max_index가 만들어지지 않음

# 보완 1. else 없이 if만 있으면 조건 거짓일 때 아무것도 안하고 다음으로 감. 다음 if문 반복
