'''
방 번호

입력
첫째 줄에 N이 주아진다. 둘째 줄에는 공백으로 구분된 P0, ..., PN-1이 주어진다.
마지막 줄에는 M이 주어진다.

출력
첫째 줄에 M원을 사용해서 만들 수 있는 가장 큰 방 번호를 출력한다. 적어도 하나의 숫자를 살 수 있는 입력만 주어진다.
'''

'''
- 상향식 방법으로 접근하여 1원부터 가장 큰 방 번호를 구하도록 한다.
* Fail/1st/00:32:10
- 빼먹는 경우의 수가 없도록 수정하였다.
* Pass/2nd/00:49:13
'''
def addNumber(a, b): # 방 번호가 a일 때 숫자 b를 더한다고 했을 때 가장 큰 방번호 출력
    if a == 0 and b == 0: # 유효하지 않은 경우
        return None
    
    temp = list(str(a))
    temp.append(str(b))
    temp.sort(reverse=True)
    temp = list(map(int, temp)) # 만약 a가 521, b가 3이라면 temp는 [5,3,2,1]이 됨
    
    result = 0
    for e in temp:
        result *= 10
        result += e
    return result

N = int(input())
arrP = list(map(int, input().split())) # arrP[i]는 i번(0~N-1) 숫자의 가격
M = int(input())
maxNumber = [None] * (M + 1) # maxNumber[m]은 m원으로 만들 수 있는 가장 큰 방 번호

for i in range(N):
    if arrP[i] <= M:
        maxNumber[arrP[i]] = i # 한 자리만 있는 케이스 (작은 숫자부터 체크하므로 같은 가격이 있으면 큰 숫자가 후에 덮어쓰게 됨)

# maxNumber배열을 누적해서 최댓값으로 갱신
maxNum = -1
for i in range(1, M + 1):
    if maxNumber[i] == None:
        if maxNum == -1:
            continue
        else:
            maxNumber[i] = maxNum
    else:
        if maxNum < maxNumber[i]:
            maxNum = maxNumber[i]
        else:
            maxNumber[i] = maxNum

maxNum = -1
for i in range(1, M + 1):
    if maxNumber[i] == None:
        continue
    
    if maxNum < maxNumber[i]:
        maxNum = maxNumber[i]
    else:
        maxNumber[i] = maxNum
    
    for j in range(len(arrP)):
        temp = addNumber(maxNumber[i], j)
        if temp == None:
            continue
        elif i + arrP[j] <= M and temp > maxNumber[i + arrP[j]]:
            maxNumber[i + arrP[j]] = temp
            
print(maxNumber[M]) 