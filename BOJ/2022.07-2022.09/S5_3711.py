'''
학번

입력
첫째 줄에 테스트 케이스의 개수 N이 주어진다.
각 테스트 케이스의 첫째 줄에는 상근이가 가르치는 학생의 수 G가 (1 ≤ G ≤ 300) 주어진다.
다음 G개 줄에는 학생의 학번이 한 줄에 하나씩 주어진다. 학번이 같은 경우는 없다.

출력
각 테스트 케이스마다, 학번을 m으로 나눈 나머지가 모두 다른 가장 작은 정수 m을 출력한다.
'''

'''
- 학생수가 많지 않으므로 나머지가 모두 다른지는 하나하나 체크하는 식으로 진행한다.
* Pass/1st/00:12:04
'''
def checkDiv(arr, m): # arr 배열에 대해 m으로 나눈 나머지들이 전부 다른지 체크
    temp = set()
    for e in arr:
        if e % m in temp:
            return False
        else:
            temp.add(e % m)
    return True
    
N = int(input())
for x1 in range(N):
    G = int(input())
    arr = []
    for x2 in range(G):
        arr.append(int(input()))
        
    answer = len(arr)
    while True:
        if checkDiv(arr, answer):
            print(answer)
            break
        else:        
            answer += 1