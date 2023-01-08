'''
아스키 도형

입력
첫째 줄에 h와 w가 주어진다. h는 그림의 높이, w는 너비이다. (2 ≤ h,w ≤ 100)
다음 h개 줄에는 창영이가 메모장에 그린 다각형이 주어진다. 
창영이가 그린 다각형은 1개이고, 변과 변이 서로 교차하는 경우는 없고, 자기 자신과 접하는 경우도 없다.

출력
첫째 줄에 다각형의 넓이를 출력한다.
'''

'''
- 넓이를 /나 \로 주어진 곳은 1/2, 그 안에 있는 빈 칸은 1로 보고 계산하면 된다.
각 줄에 대하여 선분(/나 \)과 선분 사이에 있는 점을 모두 안에 있는 빈칸으로 계산하도록 한다.
* Pass/1st/00:14:47
'''
h, w = map(int, input().split()) # h: 높이, w: 너비
arr = []

for i in range(h):
    arr.append(list(input()))

oneArea = 0 # 넓이가 1인 구역의 수
halfArea = 0 # 넓이가 0.5인 구역의 수
for i in range(h):
    lineNum = 0 # 그 줄에서 선분(/나 \)을 몇 번 만났는지(만약 홀수개 있다면 현재 도형 안을 보고 있는 것임)
    for j in range(w):
        if arr[i][j] == "/" or arr[i][j] == "\\":
            halfArea += 1
            lineNum += 1
        else:
            if lineNum % 2 == 1:
                oneArea += 1

print(oneArea + (halfArea // 2)) # /나 \의 개수는 짝수개여야 하므로 나머지는 신경쓰지 않아도 된다.