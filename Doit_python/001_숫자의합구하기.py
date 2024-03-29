'''
배열과 리스트
배열: 인덱스를 이용하여 값에 바로 접근 가능, 값의 삽입과 삭제가 어려움, 배열 크기 초기에 선언
리스트: 노드와 헤더를 통해 순차적으로 값에 접근, 값의 삽입과 삭제가 쉬움, 배열 크기 선언 필요 없음
파이썬에서는 배열과 리스트를 구분하지 않는다.
'''
# 001_ 숫자의 합 구하기
'''
N개의 숫자가 공백 없이 써 있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오.

1번째 줄에 숫자의 개수 N(1<=N<=100), 2번째 줄에 숫자 N개가 공백 없이 주어진다.
'''

# 주의할 점
'''
1) input()함수 사용 시 () 빼먹지 말기
2) input()함수로 불러온 값을 숫자연산에 사용할 경우 int선언해줘야 함
'''


n = input()
numbers = list(input())
sum = 0

for num in numbers:
    sum = sum + int(num)

print(sum)

