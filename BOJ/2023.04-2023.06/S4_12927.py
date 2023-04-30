'''
배수 스위치

입력
첫째 줄에 전구의 상태가 1번 전구부터 차례대로 주어진다.
Y는 전구가 켜 있는 경우, N은 전구가 꺼져있는 경우이다.
전구의 개수는 1보다 크거나 같고 1,000보다 작거나 같은 자연수이다.

출력
모든 전구를 끄기 위해서 스위치를 몇 번 눌러야 하는지 출력한다. 만약, 모든 전구를 끌 수 없다면 -1을 출력한다.
'''

'''
- i번 스위치를 누르면 i-1번 전구까지는 영향을 주지 않는다.
그리디 알고리즘으로 1번 전구부터 탐색하며 i번 전구가 켜져있으면 i번 스위치를 누른다.
* Pass/1st/00:05:44
'''
status = list(input())
status.insert(0, "N") # 편의상 인덱스가 1부터 시작하도록 한다.

answer = 0
for i in range(1, len(status)):
    if status[i] == "Y": # i번 스위치를 눌러서 i의 배수의 전구들을 반전시킨다.
        answer += 1
        j = 1
        while i * j < len(status):
            if status[i * j] == "Y":
                status[i * j] = "N"
            else:
                 status[i * j] = "Y"
            j += 1
            
print(answer)