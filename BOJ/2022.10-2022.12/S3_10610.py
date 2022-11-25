'''
30

입력
N을 입력받는다. N는 최대 10^5개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

출력
미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라.
그 수가 존재하지 않는다면, -1을 출력하라.
'''

'''
- 30의 배수가 되려면 3의 배수이고 10의 배수여야 한다. 우선 0~9 각 숫자별로 몇 개 나오는지 기록해둔다.
0이 하나라도 있으면 10의 배수 조건은 만족하게 된다.
또한 모든 숫자를 다 합쳤을 때 3의 배수이면 그냥 숫자를 내림차순으로 정렬하면 끝난다.
만약 3k+1꼴인 경우, 1/4/7 중 1개를 빼거나, 못 뺄 경우 2/5/8 중 2개를 뺀다.
3k+2꼴인 경우, 2/5/8 중 1개를 빼거나, 못 뺄 경우 2/5/8 중 2개를 뺀다.
* Fail/1st/00:14:58
'''
import sys

def printMax(digitArr): # 현재 digitArr에서 나올 수 있는 최댓값 출력
    for i in range(9, -1, -1):
        while digitArr[i] > 0:
            digitArr[i] -= 1
            print(i, end = "")
    
N = sys.stdin.readline().rstrip()
digitArr = [0] * 10 # digitArr[i]는 i가 몇 번 나왔는지 카운트함
digitSum = 0 # 모든 숫자들의 합

for i in range(len(N)):
    digitArr[int(N[i])] += 1
    digitSum += int(N[i])
    
if digitArr[0] == 0: # 0이 없을 경우, 즉 10의 배수가 될 수 없는 경우
    print(-1)
else:
    if digitSum % 3 == 0: # 숫자들 합이 3k꼴인 경우
        pass
    elif digitSum % 3 == 1: # 숫자들 합이 3k+1꼴인 경우
        if digitArr[1] > 0:
            digitArr[1] -= 1
        elif digitArr[4] > 0:
            digitArr[4] -= 1
        elif digitArr[7] > 0:
            digitArr[7] -= 1
        else:
            for i in range(2):
                if digitArr[2] > 0:
                    digitArr[2] -= 1
                elif digitArr[5] > 0:
                    digitArr[5] -= 1
                elif digitArr[8] > 0:
                    digitArr[8] -= 1
    elif digitSum % 3 == 2: # 숫자들 합이 3k+2꼴인 경우
        if digitArr[2] > 0:
            digitArr[2] -= 1
        elif digitArr[5] > 0:
            digitArr[5] -= 1
        elif digitArr[8] > 0:
            digitArr[8] -= 1
        else:
            for i in range(2):
                if digitArr[1] > 0:
                    digitArr[1] -= 1
                elif digitArr[4] > 0:
                    digitArr[4] -= 1
                elif digitArr[7] > 0:
                    digitArr[7] -= 1
            
    if sum(digitArr[1:]) == 0: # 220같이 숫자들을 다 뺐을 때 0만 남는 경우가 있을 수 있다.
        print(-1)
    else:
        printMax(digitArr)
