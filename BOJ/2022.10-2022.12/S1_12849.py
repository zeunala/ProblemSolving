'''
본대 산책

입력
D 가 주어진다 (1 ≤ D ≤ 100,000) 

출력
가능한 경로의 수를 1,000,000,007로 나눈 나머지를 출력 한다.
'''

'''
- D를 1씩 증가시켜가며 각 지역마다의 경로의 수를 저장해놓고 갱신한다.
* Pass/1st/00:10:31
'''
D = int(input())

# 0정보과학관, 1전산관, 2미래관, 3신양관, 4한경직기념관
# 5진리관, 6학생회관, 7형남공학관
caseArr = [1] + [0] * 7

edges = [(0, 1), (1, 2), (0, 2), (1, 3), (2, 3), (3, 4),
         (2, 4), (3, 5), (4, 5), (5, 6), (4, 7), (6, 7)]

for i in range(D):
    newCaseArr = [0] * 8
    for (start, end) in edges:
        newCaseArr[start] += caseArr[end]
        newCaseArr[end] += caseArr[start]
    
    for j in range(len(newCaseArr)):
        newCaseArr[j] %= 1000000007
    
    caseArr = newCaseArr
    
print(caseArr[0])