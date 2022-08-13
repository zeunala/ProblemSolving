'''
입력
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

출력
정답을 출력한다.
'''

'''
- 1부터 N까지 차례대로 체크하여 최선의 전략을 찾도록 한다.
* Pass/1st/00:15:25(use PyPy3)
'''
def allSubString(N): # 모든 부분문자열들의 배열 리턴
    result = set()
    
    temp = str(N)
    for i in range(len(temp)):
        for j in range(i + 1, len(temp) + 1):
            subNum = int(temp[i:j])
            if subNum != 0 and subNum != N:
                result.add(int(temp[i:j]))
    
    return sorted(list(result))

N = int(input())

caseArr = [-1] * (N + 1) # caseArr[i]는 i가 있는 상태에서 이길 수 없다면 -1, 이길 수 있다면 골라야 하는 숫자를 가진다.
for i in range(1, len(caseArr)):
    if i < 10: # 한 자리 수이면 무조건 져야한다.
        continue
    
    allCase = allSubString(i)
    for e in allCase: # 만약 수를 하나 골라서 상대방에게 필패수를 준다면 그 수를 고르면 이긴다.
        if caseArr[i - e] == -1:
            caseArr[i] = e
            break
        
print(caseArr[-1])