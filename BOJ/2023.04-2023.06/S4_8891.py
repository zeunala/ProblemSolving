'''
점 숫자

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 두 점 숫자가 주어진다. 점 숫자는 0보다 크고, 10,000보다 작다.

출력
각 테스트 케이스마다 입력으로 주어진 두 점 숫자의 합을 출력한다. 결과는 10,000보다 클 수도 있다. 
'''

'''
- 우선 #(x, y)를 구하는 함수를 만들고, 이 함수를 이용하여 두 점 숫자의 합을 출력한다.
* Pass/1st/00:21:18
'''
import sys

def getStartScoreByYPos(yPos): # 점 숫자 #(1, y)의 값을 반환한다.
    result = 1
    idx = 1
    
    #(1, 1)은 1, #(1, 2)은 1+1, #(1, 3)은 1+1+2, #(1, 4)는 1+1+2+3과 같이 증가한다.
    for i in range(2, yPos + 1):
         result += idx
         idx += 1
         
    return result

def getScoreByPos(x, y): # 점 숫자 #(x, y)의 값을 반환한다.
    startScore = getStartScoreByYPos(x + y - 1) # ex. #(5, 7)이면 대각선 시작점인 #(1, 11)의 숫자부터 확인한다.
    return startScore + (x - 1)
    
def getPosByScore(n): # n에 해당하는 점 (x, y)를 반환한다.
    startYPos = 0
    currentScore = 0
    nextScore = 1
    idx = 1
    
    # (currentScore, nextScore)가 (1, 2), (2, 4), (4, 7)과 같이 변화, n이 [currentScore, nextScore)에 있도록 한다.
    while n >= nextScore:
        currentScore = nextScore
        nextScore += idx
        idx += 1
        startYPos += 1
    
    return (1 + n - currentScore, startYPos - (n - currentScore))
        

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    (x1, y1) = getPosByScore(a)
    (x2, y2) = getPosByScore(b)
    print(getScoreByPos(x1 + x2, y1 + y2))