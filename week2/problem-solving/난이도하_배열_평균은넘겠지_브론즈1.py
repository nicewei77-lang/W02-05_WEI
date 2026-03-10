# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.

# 예제 입력
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# 예제 출력
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%

n = int(input())

percent_stu = 0
data = [list(map(int, input().split())) for _ in range(n)]
for i in data:
    over_aver_stu = []
    aver = sum(i[1:]) / i[0]
    for j in i[1:]:
        if j > aver:
            over_aver_stu.append(j)
    percent = round((len(over_aver_stu) / i[0] * 100), 3)
    print(f"{percent}%")

# Tip
## input()으로 받은 숫자는 문자열
## int는 하나의 값을 정수로 바꾼다. map - 매핑 함수는 여러개를 정수로 변환. 매핑은 대응시키다라는 어감.
## map()의 결과는 리스트가 아니라 객체이다. 그래서 list로 한번 더 변환 필요
## (언더바): 반복문에서 인덱스 숫자(i)를 실제로 쓰지 않을 때 파이썬에서 관습적으로 사용하는 표시
## f-string 방식: 문자열 앞에 f 붙이고 변수를 중괄호 안에 넣어 숫자나 변수를 문자열과 합침
## return은 반드시 함수 내부에 있어야 하며 함수의 실행을 끝내고 싶은 지점에 들여쓴다. 여기는 함수가 없으니 필요없다.
## 반복문의 변수에 이름을 붙이면 덜 햇갈린다

# 메소드
## 1. input() 한 줄을 문자열로 읽어옴
## 2. 문자열.split() 하나의 긴 문자열 덩어리를 공백을 기준으로 잘라 문자열 리스트로 만듬. ()안에는 뭐든 올 수 있다 "," ":" "\n"
## 3. map(int, 문자열) 잘린 문자열들을 각각 정수로 변환. 이터러블은 전부 넣을 수 있음. 결과는 map 객체
## 4. list() 값들을 하나의 리스트로 묶어줌
## 5. round(값, 자릿수) 소수점 n까지만 남김

# error
## 1. 중첩 반복문을 쓸 때 
## 2. aver 계산에서 i 대신 data 사용함 - for 변수 in 컬렉션에서 변수는 컬렉션의 원소 그 자체 - 중첩 반복문의 바깥 변수는 안쪽의 컬렉션이 되어야 함
## 3. over_aver_stu = []가 케이스마다 초기화 되어야 함 - 루프 안으로 넣는다
## 4. j[j] (x) j 자체가 i 배열의 원소 j > aver: (o)
## 5. percent 나누는 값은 현재 줄의 학생 수인 i[0]이다
## 6. i[j]가 원소 자체인데 append(j)로 충분

# 수정 전 1차
# n = int(input())
# over_aver_stu = []
# percent_stu = 0
# data = [list(map(int, input().split())) for _ in range(n)]
# for i in data:
#     # 평균
#     aver = sum(data[1:]) / data[0]
#     for j in data[1:]:
#         if data[j] > aver:
#             over_aver_stu.append(data[j])
#     percent = round(3, len(over_aver_stu) / data[i] * 100)
#     print(f"{percent}%")
