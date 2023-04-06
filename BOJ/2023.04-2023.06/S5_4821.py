'''
페이지 세기

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 문서의 총 페이지 수가 주어진다.
둘째 줄에는 인쇄 범위가 문제 설명에 나온 형식과 같이 주어진다. 입력의 마지막에는 0이 하나 주어진다.
문서는 많아야 1000페이지이고, 인쇄 범위의 길이는 1000글자를 넘지 않는다.

출력
각 테스트 케이스에 대해서, 출력해야 하는 페이지의 수를 출력한다.
'''

'''
- 문제의 요구사항을 그대로 구현하면 된다. 문서가 최대 1000페이지까지이므로 출력여부를 각 페이지별로 True/False로 저장한다.
* Fail/1st/00:07:12/RuntimeError
- 한 페이지만 인쇄하는 경우 체크조건을 수정하고 범위도 체크하도록 하였다.
* Pass/2nd/00:11:04
'''
import sys

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    
    needPrint = [False] * (N + 1) # needPrint[i]는 i페이지를 인쇄하는지 여부
    
    pages = sys.stdin.readline().rstrip().split(",")
    for page in pages:
        if "-" not in page: # 한 페이지만 인쇄하는 경우 (ex. 5)
            if int(page) > N:
                continue
            needPrint[int(page)] = True
        else: # 구간으로 주어지는 경우 (ex. 5-6)
            start, end = map(int, page.split("-"))
            if start > end:
                continue
            for i in range(start, end + 1):
                if i > N:
                    break
                needPrint[i] = True
                
    print(len([i for i in range(len(needPrint)) if needPrint[i]]))