'''
연산자 끼워넣기

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
'''

'''
- 수의 개수가 11개 밖에 안되니 모든 경우의 수를 하나하나 다 대입해서 최소값과 최대값을 구할 수 있다.
* Pass/1st/00:22:58
Python3로는 시간초과가 발생하였으나 삼성역량테스트에 쓰는 pypy3으로는 정답처리되었다.
같은 연산자가 중복되는 경우로 인한 중복되는 경우의 수가 많은 것이 원인으로 추정되며, 이후 다른 사람의 풀이를 확인하니 DFS로 푸는게 더 적합할 것으로 보인다.
'''

from itertools import permutations

def cal(num, op): # num은 숫자의 배열, op은 연산자의 배열. 넘긴 값에 대하여 연산한다 (음수/양수만 조심)
    result = num[0]
    for i in range(len(op)):
        if op[i]=="add":
            result+=num[i+1]
        elif op[i]=="sub":
            result-=num[i+1]
        elif op[i]=="mul":
            result*=num[i+1]
        elif op[i]=="div":
            if(result>=0):
                result//=num[i+1]
            else: # 음수/양수일 경우 양수로 먼저 고쳐줘야 한다.
                result=-((-result)//num[i+1])
    return result

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

ops=[] # 우선 연산자들을 여기에 넣고
for i in range(add):
    ops.append("add")
for i in range(sub):
    ops.append("sub")
for i in range(mul):
    ops.append("mul")
for i in range(div):
    ops.append("div")

opsArr=list(permutations(ops)) # 가능한 모든 경우의 수를 순열로 뽑아낸다. (같은 연산자가 여러개 있을 때 중복될 수 있지만 결과엔 영향을 미치지 않는다)

max = int(-(1e9+1)) # 조건에서 결과는 항상 -10억이상 10억미만이라고 했으므로
min = int(1e9+1)
for e in opsArr:
    temp = cal(A, e)
    if(temp>max):
        max=temp
    if(temp<min):
        min=temp

print(max)
print(min)