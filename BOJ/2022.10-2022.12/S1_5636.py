'''
소수 부분 문자열

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 1,000개를 넘지 않는다.
각 테스트 케이스는 길이가 255를 넘지 않는 숫자 문자열로 이루어져 있다. 입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, 가장 큰 소수 부분 문자열을 출력한다. 
'''

'''
- 각 테스트 케이스의 문자열이 255까지이고, 소수도 10만이하의 소수만 판단하면 되므로 완전 탐색을 시도한다.
* Pass/1st/00:10:16
'''
import math

isPrime = [True] * 100001 # isPrime[i]는 i가 소수인지 유무를 나타냄
isPrime[0] = False
isPrime[1] = False

for i in range(2, math.floor(math.sqrt(len(isPrime))) + 1):
    if isPrime[i] == False:
        continue
    
    j = 2
    while i * j < len(isPrime):
        isPrime[i * j] = False
        j += 1
        
primeStringSet = set() # 소수 문자열들의 집합
for i in range(len(isPrime)):
    if isPrime[i]:
        primeStringSet.add(str(i))
        
nextInput = input()
while nextInput != "0":
    maxPrime = 0
    
    for i in range(len(nextInput)):
        for j in range(1, 6):
            target = nextInput[i:i+j]
            if target in primeStringSet and int(target) > maxPrime:
                maxPrime = int(target)
    print(maxPrime)
    
    nextInput = input()