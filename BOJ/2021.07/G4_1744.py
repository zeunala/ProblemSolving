'''
수 묶기

입력
첫째 줄에 수열의 크기 N이 주어진다. N은 10,000보다 작은 자연수이다. 둘째 줄부터 N개의 줄에, 수열의 각 수가 주어진다. 수열의 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 2^31보다 작다.
'''

'''
- 처음에 수열의 위치가 고정인줄 알고 시간낭비를 했다. 일단 큰 수 부터 정렬해서 절댓값이 큰 것부터 0,1이 아닌 양수는 0,1이 아닌 양수끼리, 음수는 음수끼리만 묶는다.
만약 음수의 개수가 짝수개인 경우: 위 방법대로 묶으면 된다. 0,1을 묶지 않도록 조심하자.
만약 음수의 개수가 홀수개인 경우: 음수가 1개 남는다. 0이 있을 경우 그거와 묶고, 나머지 양수는 0이 아닌 양수끼리 묶는다.
* Pass/1st/00:45:43
'''
import sys

N = int(input())
moreThanOne = []
lessThanZero = []
one = []
zero = []
answer = 0

for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if(temp>1):
        moreThanOne.append(temp)
    elif(temp==1):
        one.append(temp)
    elif(temp==0):
        zero.append(temp)
    else:
        lessThanZero.append(temp)

moreThanOne.sort(reverse=True) # 절댓값이 큰 것부터 정렬
lessThanZero.sort()

i=0
while(i<len(moreThanOne)):
    if((i+1)>=len(moreThanOne)): # 마지막 남은 하나에 대한 처리
        answer+=moreThanOne[i]
        break
    answer+=(moreThanOne[i]*moreThanOne[i+1])
    i+=2

i=0
while(i<len(lessThanZero)):
    if((i+1)>=len(lessThanZero)): # 마지막 남은 하나에 대한 처리
        if(len(zero)!=0): # 0이 있으면 그거랑 묶는다.
            answer+=0
        else:
            answer+=lessThanZero[i]
        break
    answer+=(lessThanZero[i]*lessThanZero[i+1])
    i+=2

answer+=len(one) # 마지막으로 1들을 그냥 더한다.

print(answer)