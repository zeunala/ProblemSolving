'''
세 개의 소수 문제

입력
첫째 줄에 T(Test Case의 수를 의미함)가 주어진다.
입력은 T개의 Test Case로 이루어진다.
각 Test Case는 하나의 정수 K (7 ≤ K < 1,000, K는 홀수)로 구성된다.

출력
T줄에 걸쳐서, 각 줄에 K가 어떻게 세 소수의 합으로 표현되는지 출력해야 한다.
가능하다면 그 세 소수를 오름차순 정렬하여 출력하면 된다.
여러 개의 답이 가능하다면 그 중 하나만 출력하면 되고, 만약 불가능하다면 0을 출력한다.
'''

'''
- K의 범위가 1000 미만이므로 1000 이하의 모든 소수들에 대해 세 소수의 합을 구하는 방식을 이용한다.
* Pass/1st/00:10:15
'''
import sys
import math

isPrime = [True] * 1000
isPrime[0] = False
isPrime[1] = False
for i in range(2, math.floor(math.sqrt(1000)) + 1):
    j = 2
    while i * j < len(isPrime):
        isPrime[i * j] = False
        j += 1

primeList = [] # 1000 이하의 소수 목록
for i in range(len(isPrime)):
    if isPrime[i]:
        primeList.append(i)
        
primeSumDict = {} # primeSumDict[7] = (2, 2, 3) 식으로 분해한 소수를 저장
for i in range(len(primeList)):
    for j in range(i, len(primeList)):
        for k in range(j, len(primeList)):
            if primeList[i] + primeList[j] + primeList[k] >= 1000:
                break
            primeSumDict[primeList[i] + primeList[j] + primeList[k]] = (primeList[i], primeList[j], primeList[k])
            
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    
    if N in primeSumDict:
        (a, b, c) = primeSumDict[N]
        print(a, b, c)
    else:
        print(0)