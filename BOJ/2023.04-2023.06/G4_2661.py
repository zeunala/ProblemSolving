'''
좋은수열

입력
입력은 숫자 N하나로 이루어진다. N은 1 이상 80 이하이다.

출력
첫 번째 줄에 1, 2, 3으로만 이루어져 있는 길이가 N인 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력한다.
수열을 이루는 1, 2, 3들 사이에는 빈칸을 두지 않는다.
'''

'''
- 가장 작은 수를 구해야하므로 DFS로 가장 작은 수를 우선으로 탐색하도록 한다.
길이가 N인 좋은 수열은 반드시 길이가 N-1인 좋은 수열로부터 등장할 수 없다는 것을 이용한다.
* Pass/1st/00:14:10
'''
def isValid(target): # target[:-1]은 좋은 수열임이 보장될 때, target문자열이 좋은 수열인지 여부를 리턴한다.
    if len(target) == 1:
        return True
    
    for i in range(1, len(target) // 2 + 1): # 뒤에서 i개의 문자열과, 그 바로 앞의 i개의 문자열이 같은지 확인한다.
        if target[-i:] == target[-2 * i:-i]:
            return False
    return True

def dfs(current, N):
    if len(current) == N:
        return current
    
    for e in ["1", "2", "3"]:
        next = current + e
        if isValid(next):
            tempResult = dfs(next, N)
            if tempResult != None:
                return tempResult
    return None
    
N = int(input())
print(dfs("", N))