'''
행복한 소수

입력
첫 줄에 테스트 케이스의 수 P가 주어진다. (1 ≤ P ≤ 1000)
각 테스트 케이스는 테스트 케이스 번호와 행복한 소수인지 판정해야 할 정수인 M으로 이루어져 있다. (1 ≤ m ≤ 10000).

출력
각 테스트 케이스마다, 테스트 케이스의 번호, 입력받은 수, 만일 M이 행복한 소수라면 YES 아니라면 NO를 공백으로 각각 구분하여 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현한다. 자리수의 제곱의 합을 계속 구해서 1이 나오면 YES, 도중에 루프에 빠지게 되면 NO를 출력한다.
* Pass/1st/00:08:46
'''
import math

def getSquareSum(num): # 자리수의 제곱의 합을 리턴
    result = 0
    while num > 0:
        result += (num % 10) ** 2
        num //= 10
    return result

def isPrime(num): # 소수인지 여부 리턴
    if num == 1:
        return False
    
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def checkHappyPrime(num): # 행복한 소수이면 "YES"를, 아니면 "NO" 문자열 반환
    if not isPrime(num):
        return "NO"
    
    isVisited = set()
    while num != 1 and num not in isVisited:
        isVisited.add(num)
        num = getSquareSum(num)
        
    if num == 1:
        return "YES"
    else:
        return "NO"

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(N, M, checkHappyPrime(M))