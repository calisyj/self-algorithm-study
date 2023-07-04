'''
배열과 리스트
배열: 인덱스를 이용하여 값에 바로 접근 가능, 값의 삽입과 삭제가 어려움, 배열 크기 초기에 선언
리스트: 노드와 헤더를 통해 순차적으로 값에 접근, 값의 삽입과 삭제가 쉬움, 배열 크기 선언 필요 없음
파이썬에서는 배열과 리스트를 구분하지 않는다.
'''
# 002_평균구하기
'''
평균 계산 방법을 조작하는 문제
최대값을 M이라 할 때 모든 점수를 점수/M*100 으로 고친다.

1번째 줄에 시험을 본 과목의 개수 N이 주어진다. 해당 값은 1,000보다 작거나 같다. 2번째 줄에 세준이의 현재 성적이 주어진다. 
해당 값은 100보다 작거나 같은, 음이 아닌 정수이고, 적어도 1개의 값은 0보다 크다.
'''

# 주의할 점
'''
1) input()함수 사용 시 () 빼먹지 말기
2) input()함수로 불러온 값을 숫자연산에 사용할 경우 int선언해줘야 함
3) map(function, iterable)
map함수는 iterable의 각 요소에 대해 function함수를 적용한 결과를 새로운 iterator로 반환한다.
- function: 각 요소에 적용할 함수
- iterable: 함수를 적용할 데이터 집합
ex) map(int, input().split())
iput입력을 띄어쓰기 구분하여 받고 그 데이터를 int값으로 변환한다. 
'''

# 슈도 코드
'''
시험 본 과목의 개수 n 선언 및 입력받기
현재 성적을 띄어쓰기 구분하여 입력받기
입력받은 성적 중 최대값을 M변수로 선언
입력받은 성적 값들을 점수/M*100으로 고친 리스트 새롭게 생성
새로운 리스트 값들의 평균값 계산하여 출력
'''

n = input()
scores = list(map(int, input().split()))
M = max(scores)
new_scores = []
sum = 0
for score in scores:
    score = score/M*100
    new_scores.append(score)

for score in new_scores:
    sum = sum+score

mean = sum/len(new_scores)
print(mean)