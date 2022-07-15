'''
문제: 완주하지 못한 선수
작성자: calisyj
'''

def solution(participant, completion):
    count={}
    for i in participant: # 동명이인 구별
        #try: count[i] += 1
        #except: count[i]=1
        count = count.get(i, 0) +1 # i가 이미 있으면 +1 없으면 0
    
    for j in completion: # 완주자 구별
        if j in count:
            count[j] -= 1
    answer = [k for k, v in count.items() if v > 0]
    return answer[0]
