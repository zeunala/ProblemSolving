'''
물건 팔기

입력
첫째 줄에 세준이의 물건을 구매할 의향이 있는 사람의 수 N이 주어진다.
이 값은 50보다 작거나 같다.
둘째 줄부터 각 사람이 지불할 최대 금액과 배송비가 공백을 사이에 두고 주어진다.
두 값은 모두 10^6보다 작거나 같은 음이 아닌 정수이고, 배송비는 0이 될 수도 있다.

출력
첫째 줄에 최대 이익을 만들어주는 가격을 출력한다.
이익이 최대인 가격이 여러개라면, 가장 낮은 가격을 출력한다.
또, 어떤 가격으로 팔아도 이익을 남길 수 없다면 0을 출력한다.
'''

'''
- 지불할 최대 금액들을 기준으로 각 가격별로 이익들을 계산하도록 한다.
* Fail/1st/00:10:00
'''
N = int(input())
arr = []
availablePrice = [] # 후보가 될 수 있는 가격들
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
    availablePrice.append(a)
    
bestPrice = 0 # 이익이 최대인 가격
bestScore = 0 # 그 때의 이익
for e in availablePrice:
    tempScore = 0
    for (a, b) in arr:
        if a >= e: # 지불가능한 사람들에 한해 배송비를 뺀 금액만큼 금액을 받음
            tempScore += max(0, e - b)
            
    if bestScore < tempScore:
        bestPrice = e
        bestScore = tempScore
        
print(bestPrice)