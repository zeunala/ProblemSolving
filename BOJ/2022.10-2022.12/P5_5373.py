'''
큐빙

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다. 각 테스트 케이스는 다음과 같이 구성되어져 있다.

첫째 줄에 큐브를 돌린 횟수 n이 주어진다. (1 ≤ n ≤ 1000)
둘째 줄에는 큐브를 돌린 방법이 주어진다. 각 방법은 공백으로 구분되어져 있으며, 첫 번째 문자는 돌린 면이다.
U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면이다.
두 번째 문자는 돌린 방향이다. +인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향이다.
출력
각 테스트 케이스에 대해서 큐브를 모두 돌린 후의 윗 면의 색상을 출력한다.
첫 번째 줄에는 뒷 면과 접하는 칸의 색을 출력하고, 두 번째, 세 번째 줄은 순서대로 출력하면 된다.
흰색은 w, 노란색은 y, 빨간색은 r, 오렌지색은 o, 초록색은 g, 파란색은 b.
'''

'''
- 시간초과 염려가 없으므로 문제 조건을 그대로 구현하면 되는 문제로 보인다.
* Pass/1st/01:40:27
- 문제풀이 이후 다른 사람의 풀이를 본 결과 시계 반대 방향을 시계 방향 3번으로 처리한다는 아이디어가 있음을 알게 되었다.
'''
import sys

def rotateRightOne(arrU): # arrU만을 시계방향으로 돌림
    arrCopy = arrU[:]
    arrU[0], arrU[1], arrU[2] = arrCopy[6], arrCopy[3], arrCopy[0] 
    arrU[3], arrU[4], arrU[5] = arrCopy[7], arrCopy[4], arrCopy[1]
    arrU[6], arrU[7], arrU[8] = arrCopy[8], arrCopy[5], arrCopy[2]
    
def rotateLeftOne(arrU): # arrU만을 반시계방향으로 돌림
    arrCopy = arrU[:]
    arrU[0], arrU[1], arrU[2] = arrCopy[2], arrCopy[5], arrCopy[8]
    arrU[3], arrU[4], arrU[5] = arrCopy[1], arrCopy[4], arrCopy[7]
    arrU[6], arrU[7], arrU[8] = arrCopy[0], arrCopy[3], arrCopy[6]

def doAction(action, arrU, arrD, arrF, arrB, arrL, arrR):
    if action == "U+":
        rotateRightOne(arrU)
        arrF[0:3], arrL[0:3], arrB[0:3], arrR[0:3] = arrR[0:3], arrF[0:3], arrL[0:3], arrB[0:3]
    elif action == "U-":
        rotateLeftOne(arrU)
        arrF[0:3], arrL[0:3], arrB[0:3], arrR[0:3] = arrL[0:3], arrB[0:3], arrR[0:3], arrF[0:3]
    elif action == "D+":
        rotateRightOne(arrD)
        arrF[6:9], arrR[6:9], arrB[6:9], arrL[6:9] = arrL[6:9], arrF[6:9], arrR[6:9], arrB[6:9]
    elif action == "D-":
        rotateLeftOne(arrD)
        arrF[6:9], arrR[6:9], arrB[6:9], arrL[6:9] = arrR[6:9], arrB[6:9], arrL[6:9], arrF[6:9]
    elif action == "F+":
        rotateRightOne(arrF)
        arrU[6:9], arrR[0:9:3], arrD[6:9], arrL[8::-3] = arrL[8::-3], arrU[6:9], arrR[0:9:3], arrD[6:9]
    elif action == "F-":
        rotateLeftOne(arrF)
        arrU[6:9], arrR[0:9:3], arrD[6:9], arrL[8::-3] = arrR[0:9:3], arrD[6:9], arrL[8::-3], arrU[6:9]
    elif action == "B+":
        rotateRightOne(arrB)
        arrU[0:3], arrL[6::-3], arrD[0:3], arrR[2:9:3] = arrR[2:9:3], arrU[0:3], arrL[6::-3], arrD[0:3]
    elif action == "B-":
        rotateLeftOne(arrB)
        arrU[0:3], arrL[6::-3], arrD[0:3], arrR[2:9:3] = arrL[6::-3], arrD[0:3], arrR[2:9:3], arrU[0:3]
    elif action == "L+":
        rotateRightOne(arrL)
        arrU[0:9:3], arrF[0:9:3], arrD[8::-3], arrB[8::-3] = arrB[8::-3], arrU[0:9:3], arrF[0:9:3], arrD[8::-3]
    elif action == "L-":
        rotateLeftOne(arrL)
        arrU[0:9:3], arrF[0:9:3], arrD[8::-3], arrB[8::-3] = arrF[0:9:3], arrD[8::-3], arrB[8::-3], arrU[0:9:3]
    elif action == "R+":
        rotateRightOne(arrR)
        arrU[8::-3], arrB[0:9:3], arrD[0:9:3], arrF[8::-3] = arrF[8::-3], arrU[8::-3], arrB[0:9:3], arrD[0:9:3]
    elif action == "R-":
        rotateLeftOne(arrR)
        arrU[8::-3], arrB[0:9:3], arrD[0:9:3], arrF[8::-3] = arrB[0:9:3], arrD[0:9:3], arrF[8::-3], arrU[8::-3]

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    n = int(sys.stdin.readline().rstrip()) # 큐브를 돌린 횟수
    actionArr = sys.stdin.readline().rstrip().split()
    
    # 큐브의 상태 저장(각 면을 본 상태에서 맨 윗줄부터)
    arrU = ["w"] * 9
    arrD = ["y"] * 9
    arrF = ["r"] * 9
    arrB = ["o"] * 9
    arrL = ["g"] * 9
    arrR = ["b"] * 9
    
    # 큐브 회전
    for action in actionArr:
        doAction(action, arrU, arrD, arrF, arrB, arrL, arrR)
    
    # 결과 출력
    for i in range(3):
        for j in range(3):
            print(arrU[i * 3 + j], end = "")
        print()