'''
홀수 홀릭 호석

입력
첫번째 줄에 호석이가 처음 시작할 때 가지고 있는 수 N 이 주어진다.

출력
첫 번째 줄에 호석이가 만들 수 있는 최종값 중에서 최솟값과 최댓값을 순서대로 공백으로 구분하여 출력한다.
'''

'''
- dp를 이용하여 풀이하면 된다.
* Pass/1st/00:25:54
'''
dpMax = dict()
dpMin = dict()
for i in range(10):
    dpMax[str(i)] = 1 if i % 2 == 1 else 0
    dpMin[str(i)] = 1 if i % 2 == 1 else 0

def countOdd(s):
    n = int(s)
    result = 0
    while n > 0:
        if n % 2 == 1:
            result += 1
        n //= 10
    return result

def solutionMax(s):
    if s in dpMax:
        return dpMax[s]
    
    result = countOdd(s)
    if len(s) == 2:
        result += solutionMax(str(int(s[0]) + int(s[1])))
    else:
        tempMax = 0
        
        for i in range(1, len(s) - 1):
            for j in range(i + 1, len(s)):
                newS = str(int(s[:i]) + int(s[i:j]) + int(s[j:]))
                temp = solutionMax(newS)
                tempMax = max(tempMax, temp)
                
        result += tempMax
    
    dpMax[s] = result
    return result

def solutionMin(s):
    if s in dpMin:
        return dpMin[s]
    
    result = countOdd(s)
    if len(s) == 2:
        result += solutionMin(str(int(s[0]) + int(s[1])))
    else:
        tempMin = 9999999999
        
        for i in range(1, len(s) - 1):
            for j in range(i + 1, len(s)):
                newS = str(int(s[:i]) + int(s[i:j]) + int(s[j:]))
                temp = solutionMin(newS)
                tempMin = min(tempMin, temp)
                
        result += tempMin
    
    dpMin[s] = result
    return result

N = input()
print(solutionMin(N), solutionMax(N))