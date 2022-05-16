'''
2×2×2 큐브

입력
첫째 줄에 2×2×2 루빅스 큐브 각 면의 각 칸 색상이 주어진다. 색상은 1부터 6까지의 자연수로 나타내며, 각 자연수는 총 4번 등장한다.

출력
루빅스 큐브를 정확히 한 번 돌려서 풀 수 있으면 1, 없으면 0을 출력한다.
'''

'''
- 총 돌리는 경우의 수는 4가지이므로 4가지 경우만 체크해본다.
* Fail/1st/00:18:50
- 돌리는 경우의 수가 2가지 더 있어 총 6가지의 경우를 생각해야한다.
* Fail/2nd/00:30:19
- 잘못된 코드를 발견하여 수정하였다.
* Fail/3rd/00:40:53
- 해당 코드를 재수정하였다.
* Pass/4th/00:42:45
'''
def checkValid(arr):
    # 세로방향으로 위/아래 회전
    if arr[1] == arr[3] == arr[6] == arr[8] and arr[5] == arr[7] == arr[10] == arr[12] and arr[9] == arr[11] == arr[21] == arr[23] and arr[22] == arr[24] == arr[2] == arr[4] and arr[13] == arr[14] == arr[15] == arr[16] and arr[17] == arr[18] == arr[19] == arr[20]:
        return 1
    
    # 세로방향으로 아래/위 회전
    if arr[1] == arr[3] == arr[21] == arr[23] and arr[5] == arr[7] == arr[2] == arr[4] and arr[9] == arr[11] == arr[6] == arr[8] and arr[22] == arr[24] == arr[10] == arr[12] and arr[13] == arr[14] == arr[15] == arr[16] and arr[17] == arr[18] == arr[19] == arr[20]:
        return 1
    
    # 가로방향으로 왼쪽/오른쪽 회전
    if arr[5] == arr[6] == arr[19] == arr[20] and arr[17] == arr[18] == arr[23] == arr[24] and arr[21] == arr[22] == arr[15] == arr[16] and arr[13] == arr[14] == arr[7] == arr[8] and arr[1] == arr[2] == arr[3] == arr[4] and arr[9] == arr[10] == arr[11] == arr[12]:
        return 1
    
    # 가로방향으로 오른쪽/왼쪽 회전
    if arr[5] == arr[6] == arr[15] == arr[16] and arr[17] == arr[18] == arr[7] == arr[8] and arr[21] == arr[22] == arr[19] == arr[20] and arr[13] == arr[14] == arr[23] == arr[24] and arr[1] == arr[2] == arr[3] == arr[4] and arr[9] == arr[10] == arr[11] == arr[12]:
        return 1
    
    # 정면방향으로 시계방향 회전
    if arr[1] == arr[2] == arr[17] == arr[19] and arr[18] == arr[20] == arr[9] == arr[10] and arr[11] == arr[12] == arr[14] == arr[16] and arr[13] == arr[15] == arr[3] == arr[4] and arr[5] == arr[6] == arr[7] == arr[8] and arr[21] == arr[22] == arr[23] == arr[24]:
        return 1
    
    # 정면방향으로 반시계방향 회전
    if arr[1] == arr[2] == arr[14] == arr[16] and arr[18] == arr[20] == arr[3] == arr[4] and arr[11] == arr[12] == arr[17] == arr[19] and arr[13] == arr[15] == arr[9] == arr[10] and arr[5] == arr[6] == arr[7] == arr[8] and arr[21] == arr[22] == arr[23] == arr[24]:
        return 1
    
    return 0

arr = [0] # 편의상 arr[1]~arr[24]까지 생각
tempArr = map(int, input().split())
arr.extend(tempArr)

print(checkValid(arr))
