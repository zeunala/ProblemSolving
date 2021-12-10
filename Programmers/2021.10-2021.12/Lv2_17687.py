'''
n진수 게임
- 문제 그대로 구현하면 된다. 일단 총 문자열을 구하고(최대길이 t*m),
이 중 튜브가 말해야 하는 숫자를 추출해내자.
* Pass/1st/00:18:04
'''
def changeNum(num, n): # 10진법의 수 num을 n진법으로 바꾸고 해당 문자열 리턴
    result = ""
    
    if num == 0:
        return "0"
    
    while num > 0:
        nextChar = num % n
        
        if nextChar < 10:
            result = str(num % n) + result
        elif nextChar == 10:
            result = "A" + result
        elif nextChar == 11:
            result = "B" + result
        elif nextChar == 12:
            result = "C" + result
        elif nextChar == 13:
            result = "D" + result
        elif nextChar == 14:
            result = "E" + result
        elif nextChar == 15:
            result = "F" + result
        num //= n
        
    return result
    

def solution(n, t, m, p):
    answer = ""
    allString = ""

    i = 0
    while len(allString) <= t * m:
        allString += changeNum(i, n)
        i += 1
        
    # allString중 튜브가 말해야 하는 수를 뽑아낸다.
    for i in range(t):
        answer += allString[i * m + p - 1]

    return answer