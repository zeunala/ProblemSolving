'''
압축

- 파이썬의 딕셔너리를 이용하면 쉽게 작업할 수 있을 것으로 보인다.
* Pass/1st/00:12:10
'''

def solution(msg):
    answer = []
    dict = {}
    
    for e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dict[e] = len(dict) + 1
    
    currentString = ""
    for i in range(len(msg)):
        currentString += msg[i]
        if i + 1 >= len(msg) or (currentString + msg[i + 1] not in dict):
            answer.append(dict[currentString])
            if i + 1 >= len(msg):
                dict[currentString] = len(dict) + 1
            else:
                dict[currentString + msg[i+1]] = len(dict) + 1
            currentString = ""
    
    return answer