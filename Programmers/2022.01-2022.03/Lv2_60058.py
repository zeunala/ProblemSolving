'''
괄호 변환

- 문제의 절차에 따라서 그대로 구현해보자.
* Pass/1st/00:16:12
'''
def divideUV(w): # 문자열 w를 균형잡힌 괄호 문자열 u, v로 분리한다. (이 때 u 길이는 최소)
    count = 0 # '(' 개수 - ')' 개수
    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        if w[i] == ")":
            count -= 1
        if count == 0:
            return (w[:i+1], w[i+1:])

def checkCorrect(u): # 문자열 u가 올바른 괄호 문자열인지 여부를 리턴
    count = 0 # '(' 개수 - ')' 개수
    for i in range(len(u)):
        if u[i] == "(":
            count += 1
        if u[i] == ")":
            count -= 1
        if count < 0: # 중간에 ')'의 개수가 '('의 개수를 추월하는 경우
            return False
        
    return True # 중간에 ')'의 개수가 추월하는 경우가 없는 경우

def makeCorrect(w): # 균형잡힌 괄호 문자열 w를 올바른 괄호 문자열로 변환한다.
    # 1단계
    if w == "":
        return ""
    
    # 2단계
    (u, v) = divideUV(w)
    
    # 3단계
    if checkCorrect(u):
        return u + makeCorrect(v)
    
    # 4단계
    result = "("
    result += makeCorrect(v)
    result += ")"
    temp = u[1:-1] # u의 첫 번째와 마지막 문자 제거
    reverseTemp = "" # temp에서 괄호 방향 뒤집은 것
    
    for i in range(len(temp)):
        if temp[i] == "(":
            reverseTemp += ")"
        if temp[i] == ")":
            reverseTemp += "("
    result += reverseTemp
    
    return result
    
def solution(p):
    answer = ''

    return makeCorrect(p)