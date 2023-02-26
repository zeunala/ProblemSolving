'''
놀라운 문자열

입력
입력의 각 줄에는 알파벳 대문자로만 구성된 문자열이 주어진다.
모든 문자열의 길이는 80을 넘지 않으며, 입력의 마지막 줄에는 마지막을 나타내는 *가 주어진다.
입력은 마지막 줄을 포함해서 101줄을 넘지 않는다.

출력
각 줄에 이 문자열이 놀라운(surprising) 문자열인지 아닌지를 아래의 예제와 같이 출력한다.
'''

'''
- 문자열 길이조건이 크지 않으므로 문제의 요구사항을 그대로 구현하면 되는 문제이다.
* Pass/1st/00:06:29
'''
def isDUnique(str, D): # D-쌍이 유일한지 여부 리턴
    history = set()
    
    for i in range(len(str) - 1 - D):
        onePair = (str[i], str[i + 1 + D])
        if onePair in history:
            return False
        history.add(onePair)
        
    return True
    
def isSurprising(str):
    for i in range(len(str) - 1): # 길이가 N이면 0-쌍 ~ (N - 2)쌍이 정의됨
        if not isDUnique(str, i):
            return False
        
    return True

while True:
    str = input()
    if str == "*":
        break
    
    if isSurprising(str):
        print(str + " is surprising.")
    else:
        print(str + " is NOT surprising.")