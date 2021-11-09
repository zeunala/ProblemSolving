'''
용액

입력
첫째 줄에는 전체 용액의 수 N이 입력된다.
N은 2 이상 100,000 이하의 정수이다.
둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 오름차순으로 입력되며, 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다.
N개의 용액들의 특성값은 모두 서로 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

출력
첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다.
출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다.
특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.
'''

'''
- 일단 음수인 것들과 양수인 것들 두 분류로 나눠보자. 음수 용액들을 순차적으로 탐색해가며 그에 대응하는 특성값이 가장 0에 가까운 양수 용액을 찾아본다.
이 때 산성만 주어지거나 알칼리성만 주어지는 경우에 주의하자. 또한 0인 것들도 따로 빼내자.
* Pass/1st/00:38:31
- 문제는 맞췄으나 특수 케이스에 대한 예외처리들이 많아 다소 비직관적이다.
다른 사람의 풀이를 찾아보니 양 끝에서 시작하여 합이 양수냐 음수냐에 따라 양 끝중 하나를 앞으로 당기고,
절댓값 갱신여부를 확인하는 식으로 푸는 것이 더 좋아보인다.
'''
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arrZero = []
arrPlus = []
arrMinus = []
minValue = 9999999999
firstElement = 0 # 값이 낮은 용액
secondElement = 0 # 값이 높은 용액

for e in arr:
    if e > 0:
        arrPlus.append(e)
    elif e < 0:
        arrMinus.append(e)
    else:
        arrZero.append(e)

arrPlus.sort() # 절댓값이 작은 것부터 정렬
arrMinus.sort(reverse=True)

if len(arrZero) >= 2:
    print("0 0")
elif len(arrPlus) == 0: # 음수 용액만 있을 경우
    print(str(arrMinus[1]) + " " + str(arrMinus[0]))
elif len(arrMinus) == 0: # 양수 용액만 있을 경우
    print(str(arrPlus[0])+ " " + str(arrPlus[1]))
else:
    arrPlusIdx = 0
    for i in range(len(arrMinus)):
        while arrPlusIdx < len(arrPlus) - 1:
            if abs(arrMinus[i] + arrPlus[arrPlusIdx]) < abs(arrMinus[i] + arrPlus[arrPlusIdx + 1]):
                if abs(arrMinus[i] + arrPlus[arrPlusIdx]) < minValue:
                    minValue = abs(arrMinus[i] + arrPlus[arrPlusIdx])
                    firstElement = arrMinus[i]
                    secondElement = arrPlus[arrPlusIdx]
                break
            else:
                arrPlusIdx += 1
                
        if arrPlusIdx == len(arrPlus) - 1:
            if abs(arrMinus[i] + arrPlus[arrPlusIdx]) < minValue:
                minValue = abs(arrMinus[i] + arrPlus[arrPlusIdx])
                firstElement = arrMinus[i]
                secondElement = arrPlus[arrPlusIdx]
            continue
        
    if len(arrMinus)>=2 and abs(arrMinus[0] + arrMinus[1]) < minValue: # 음수, 양수끼리만 있는 경우도 체크
        minValue = abs(arrMinus[0] + arrMinus[1])
        firstElement = arrMinus[1]
        secondElement = arrMinus[0]
    if len(arrPlus)>=2 and abs(arrPlus[0] + arrPlus[1] < minValue):
        minValue = abs(arrPlus[0] + arrPlus[1])
        firstElement = arrPlus[0]
        secondElement = arrPlus[1]
    
    if len(arrZero) == 1: # 0이 한 개 있는 경우도 체크
        if arrPlus[0] < arrMinus[0] and arrPlus[0] < minValue: # 절댓값이 제일 작은 원소와 0이 결과가 될 수 있다.
            minValue = arrPlus[0]
            firstElement = 0
            secondElment = arrPlus[0]
        if arrPlus[0] >= arrMinus[0] and abs(arrMinus[0]) < minValue:
            minValue = abs(arrMinus[0])
            firstElement = arrMinus[0]
            secondElement = 0
        
    print(str(firstElement)+ " "+ str(secondElement))