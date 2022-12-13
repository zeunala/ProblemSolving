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
- 출력초과 오류가 나서 printMax함수를 수정하였다.
* Fail/2nd/00:19:21
- 숫자를 중간에 뺄 수 있는 것으로 잘못 이해하였다. 숫자를 내림차순으로 정렬하면 0은 자동으로 맨 끝에 오므로,
숫자 내림차순으로 배치하고 0이 존재하고, 모든 숫자를 다 합쳤을 때 3의 배수인지만 체크하면 된다.
* Pass/3rd/00:27:08
'''
import sys

def getMaxNum(digitArr): # 현재 digitArr에서 나올 수 있는 최댓값 출력
    result = ""
    for i in range(9, -1, -1):
        while digitArr[i] > 0:
            digitArr[i] -= 1
            result += str(i)
    return result
    
N = sys.stdin.readline().rstrip()
digitArr = [0] * 10 # digitArr[i]는 i가 몇 번 나왔는지 카운트함
digitSum = 0 # 모든 숫자들의 합

for i in range(len(N)):
    digitArr[int(N[i])] += 1
    digitSum += int(N[i])
    
if digitArr[0] == 0 or digitSum % 3 != 0: # 0이 없을 경우(10의 배수X) 또는 3의 배수가 아닌 경우
    print(-1)
else:
    print(getMaxNum(digitArr))
