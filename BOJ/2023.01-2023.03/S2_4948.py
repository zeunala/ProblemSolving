'''
베르트랑 공준

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
'''

'''
- n의 범위가 최대 123456까지이므로 넉넉하게 25만까지의 소수를 미리 구해놓으면 쉽게 계산할 수 있다.
* Pass/1st/00:09:30
'''
import sys
import math
from bisect import bisect_left, bisect_right

MAX_N = 250000
isPrime = [True] * MAX_N # isPrime[i]는 i가 소수인지 유무를 나타냄
isPrime[0] = False
isPrime[1] = False

for i in range(math.floor(math.sqrt(MAX_N))):
    if isPrime[i] == False:
        continue
    j = 2
    while i * j < MAX_N:
        isPrime[i * j] = False
        j += 1
        
primeArr = [i for i in range(MAX_N) if isPrime[i] == True] # 소수들만 모은 배열

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    
    print(bisect_right(primeArr, 2 * n) - bisect_right(primeArr, n)) # n초과 2n이하 소수의 개수