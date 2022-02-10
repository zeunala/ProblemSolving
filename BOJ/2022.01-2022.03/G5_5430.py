'''
AC

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다.
p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)
전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
'''

'''
- 배열의 수의 개수가 10만이므로 단순히 배열을 가지고 reverse를 시키면 시간초과가 날 것으로 보인다.
어차피 버리기와 뒤집기만 있으므로 양옆에 일종의 포인터를 두어 좁혀나가는 방식으로 하자.
* Fail/1st/00:15:59
'''
import sys

T = int(input())
for i in range(T):
    currentCommand = sys.stdin.readline().rstrip()
    arrLen = int(sys.stdin.readline().rstrip())
    arrCommand = sys.stdin.readline().rstrip()
    arrCommand = arrCommand[1:-1]
    
    if arrCommand:
        arr = list(map(int, arrCommand.split(",")))
    else:
        arr = []
    
    startIdx = 0 # 맨 앞의 포인터 인덱스
    endIdx = arrLen - 1 # 맨 뒤의 포인터 인덱스
    pointIdx = 0 # 0이면 현재 앞을 향하고, 1이면 뒤를 향하는 상태
    
    for e in currentCommand:
        if e == "R":
            pointIdx = abs(pointIdx - 1) # 0이면 1로, 1이면 0으로 만들어준다.
        elif e == "D":
            if pointIdx == 0:
                startIdx += 1
            else:
                endIdx -= 1
            if startIdx > endIdx: # 0에서 삭제를 시도하는 경우
                break
            
    if startIdx > endIdx:
        print("error")
    else:
        result = arr[startIdx:endIdx+1]
        if pointIdx == 0:
            print(result)
        elif pointIdx == 1:
            result.reverse()
            print(result)
    
    