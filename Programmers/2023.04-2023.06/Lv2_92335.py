'''
k진수에서 소수 개수 구하기

- 문제의 요구사항을 그대로 구현한다.
우선 n을 k진수로 바꾸고, 0을 기준으로 후보들을 구하고 그 중 소수의 개수를 구한다.
n이 100만까지밖에 안되므로 시간초과를 염두에 두지 않아도 된다.
* Pass/1st/00:10:36
'''
import math

def changeByK(n, k): # n을 k진수로 바꾼 문자열 리턴
    result = ""
    
    while n > 0:
        result = str(n % k) + result
        n //= k
    
    return result

def isPrime(n): # n이 소수인지 유무 리턴
    if n == 1:
        return False
    
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True
    
def solution(n, k):
    answer = 0
    kNum = changeByK(n, k) # k진수
    
     # "0"을 기준으로 잘라 정수로 나타내되 빈 문자열 제거
    targets = [int(e) for e in kNum.split("0") if e]
    
    for e in targets:
        if isPrime(e):
            answer += 1
    
    return answer