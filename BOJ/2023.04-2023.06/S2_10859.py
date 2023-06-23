'''
뒤집어진 소수

입력
첫 번째 줄에 N이 주어진다 (1 ≤ N ≤ 10^16).
N의 첫 숫자는 0이 아니다.

출력
첫 번째 줄에 N이 소수이고 뒤집혀서도 소수이면 "yes"를 출력하고, 아니면 "no"를 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현해본다.
* Pass/1st/00:10:53
'''
import math

def getReversedNum(num): # 뒤집어진 수 리턴, 수가 아닌 경우 None 리턴
    target = str(num)
    result = ""
    
    for i in range(len(target) - 1, -1, -1):
        if target[i] in ["3", "4", "7"]:
            return None
        elif target[i] == "6":
            result += "9"
        elif target[i] == "9":
            result += "6"
        else:
            result += target[i]
    
    return int(result)

def isPrime(num): # 주어진 수가 소수인지
    # 최적화를 위해 2로 나눠떨어지는지 먼저 확인하고, 3부터 2씩 증가시켜가며 나눠 떨어지는지 확인한다.
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
    

N = int(input())
reversedN = getReversedNum(N)

if isPrime(N) and reversedN != None and isPrime(reversedN):
    print("yes")
else:
    print("no")