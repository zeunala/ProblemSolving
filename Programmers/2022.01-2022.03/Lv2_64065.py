'''
튜플

- s를 배열로 변환한 후 배열을 길이 순으로 정렬하자.
그 뒤 길이가 1인 배열부터 원래의 결과로 복구할 수 있다.
* Pass/1st/00:11:28
'''

def solution(s):
    answer = []
    
    arrS = []
    tempValue = 0
    tempArr = []
    for i in range(1, len(s) - 1): # 맨 앞뒤 { } 제외
        if s[i] == "{": # { 는 무시
            continue
        elif s[i] == ",":
            if tempValue == 0: # 튜플의 원소가 1이상인데 이 값이 0이면 {} 사이의 ,이라는 뜻
                continue
            else:
                tempArr.append(tempValue)
                tempValue = 0
        elif s[i] == "}":
            if tempValue != 0:
                tempArr.append(tempValue)
                tempValue = 0
            arrS.append(tempArr)
            tempArr = []
        else: # 그냥 숫자인 경우
            tempValue *= 10
            tempValue += int(s[i])
        
    arrS.sort(key = lambda x : len(x)) # 길이 순 정렬
    
    for i in range(len(arrS)):
        # 각 arrS의 원소에 대하여 answer에 없는걸 answer 뒤에 붙여나간다.
        for e in arrS[i]:
            if e not in answer:
                answer.append(e)
                break
    
    return answer