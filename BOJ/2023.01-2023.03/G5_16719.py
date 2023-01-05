'''
ZOAC

입력
첫 번째 줄에 알파벳 대문자로 구성된 문자열이 주어진다. 문자열의 길이는 최대 100자이다.

출력
규칙에 맞게 순서대로 문자열을 출력한다.
'''

'''
- 주어지는 문자열의 길이가 최대 100이므로, 문자를 하나 추가하기 전에 모든 경우의 수를 확인하고 가장 앞서는 경우일 때 추가한다.
* Pass/1st/00:14:39
'''
def showActivateStr(target, isActivate): # ex. showActivateStr("CAT", [True, True, False])는 True에 해당하는 문자인 "CA"를 반환함
    result = ""
    for i in range(len(isActivate)):
        if isActivate[i]:
            result += target[i]
    return result

target = input()
isActivate = [False] * len(target) # 현재 문자는 isActivate[i]가 True인것들만을 모은것이다. ex. "CAT", [True, True, False] -> "CA"

for i in range(len(target)):
    # isActivate값이 False인것 하나하나에 대해서 추가했을 때의 가능한 문자열들을 모아놓고 가장 앞서는 경우를 확인
    tempResult = [] # (문자열, 그때 활성화 시킨 인덱스)
    
    for j in range(len(isActivate)):
        if isActivate[j] == False:
            isActivate[j] = True
            tempResult.append((showActivateStr(target, isActivate), j))
            isActivate[j] = False
    
    tempResult.sort() # tempResult의 가장 앞에는 (가장 앞서는 문자열, 그때 활성화 시킨 인덱스)가 될 것임
    print(tempResult[0][0])
    isActivate[tempResult[0][1]] = True