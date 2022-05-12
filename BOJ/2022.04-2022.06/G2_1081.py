'''
합

입력
첫째 줄에 두 정수 L과 U이 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

'''
- 결국 N이하의 모든 정수의 각 자리합을 O(1)으로 풀면 되는 문제이므로 단계적으로 문제를 분할해서 풀도록 한다.
* Pass/1st/00:51:47
'''
def calcSum10(N): # 0부터 10^N-1까지의 모든 정수의 각 자리합 리턴
    if N == 0:
        return 0
    else:
        return 45 * N * (10 ** (N - 1)) # 자릿수가 하나 커질수록 총 숫자의 개수가 10배가 되고, 자릿수에 비례하게 각 값이 증가한다.
    
def calcSumX0(X, N): # 0부터 (X*10^N)-1까지의 모든 정수의 각 자리합 리턴
    temp = 0
    for i in range(1, X + 1):
        temp += (i - 1)
        
    return X * calcSum10(N) + temp * 10 ** N

def calcSum(num): # 0부터 num까지의 모든 정수의 각 자리합 리턴
    if num <= 0:
        return 0
    
    tempNum = num
    idx = 0 # num이하인 수 중 10*N이 최대가 될 때 그 때의 idx값
    while tempNum >= 10:
        idx += 1
        tempNum //= 10
    
    firstNum = num # num의 가장 앞 자리 수
    while firstNum >= 10:
        firstNum //= 10
        
    tempPrefix = 0
    for i in range(1, firstNum + 1):
        tempPrefix += (i - 1)
        
    return calcSumX0(firstNum, idx) + firstNum * (num - (firstNum * (10 ** idx)) + 1) + calcSum(num - (firstNum * (10 ** idx)))

L, U = map(int, input().split())

print(calcSum(U) - calcSum(L - 1))