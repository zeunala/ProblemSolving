'''
되돌리기

입력
첫째 줄에 명령의 개수 N이 주어진다.
둘째 줄부터 N개의 줄에 명령과 수행한 시간이 주어진다.
항상 시간이 오름차순으로 주어지고, type c에서 c는 알파벳 소문자, undo t에서 t는 1보다 크거나 같고 109보다 작거나 같은 자연수이다.
N은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 명령을 수행한 후에 남아있는 텍스트를 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현해본다.
* Pass/1st/00:26:33
'''
N = int(input())
statusArr = [("", 0) for _ in range(N)] # statusArr[i]는 i번째줄 명령 수행 이후 텍스트 상태와 지난 시간을 나타낸다.

commandText, targetText, spendTime = input().split()

# 초기세팅
if commandText == "type":
    statusArr[0] = (targetText, int(spendTime))
elif commandText == "undo":
    statusArr[0] = ("", int(spendTime))


for i in range(1, N):
    commandText, targetText, spendTime = input().split()
    spendTime = int(spendTime)
    
    if commandText == "type":
        statusArr[i] = (statusArr[i - 1][0] + targetText, spendTime)
    elif commandText == "undo":
        targetText = int(targetText)
        statusArr[i] = ("", spendTime) # 아무 것도 없는 경우로 undo하는 경우 대비
        
        for j in range(i - 1, -1, -1):
            if spendTime - targetText <= statusArr[j][1]:
                continue
            else:
                statusArr[i] = (statusArr[j][0], spendTime)
                break

print(statusArr[-1][0])