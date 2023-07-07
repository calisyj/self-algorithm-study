'''
배열과 리스트
배열: 인덱스를 이용하여 값에 바로 접근 가능, 값의 삽입과 삭제가 어려움, 배열 크기 초기에 선언
리스트: 노드와 헤더를 통해 순차적으로 값에 접근, 값의 삽입과 삭제가 쉬움, 배열 크기 선언 필요 없음
파이썬에서는 배열과 리스트를 구분하지 않는다.
'''
# 003_구간합구하기1
'''
수 N개가 주어졌을 때 i번째 수에서 j번째 수까지의 합을 구하는 프로그램을 작성하라

1번째 줄에 수의 개수 N(1<= N <= 10,000), 합을 구해야 하는 횟수 M(1<=M<=100,000), 2번째 줄에 N개의 수가 주어진다. 각 수는 1,000보다 작거나 같은 자연수다.
3번째 줄부터는 M개의 줄에 합을 구해야 하는 구간 i와 j가 주어진다.
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
1번째 줄에 N, M 입력 받기
2번째 줄에 배열 입력 받기
3번째 줄부터는 구해야 하는 구간 i와 j가 주어진다.
구간합 출력
'''

def range_sum(arr, i, j):
    sum = 0
    for k in range(i-1, j):
        if i - (j+1) == 0:
            sum += arr[k]
            continue
        sum += arr[k]
    return sum

N, M = map(int, input().split()) # N = 수의 개수, M = 합을 구해야 하는 횟수
arr = list(map(int, input().split()))
sum_arr = [0]

for a in range(M):
    i, j = map(int, input().split())
    sum_arr.append(range_sum(arr, i, j))

for s in range(1, len(sum_arr)):
    print(sum_arr[s])

