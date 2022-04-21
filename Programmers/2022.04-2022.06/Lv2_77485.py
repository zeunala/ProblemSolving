'''
행렬 테두리 회전하기

- 문제에서 제시한 그대로 구현해보자. 회전 대상 범위를 반복문을 이용하여 하나하나 바꿔나간다.
* Fail/1st/00:25:49
- 잘못 작성한 부분을 수정하였다.
* Pass/2nd/00:30:45
'''

def solution(rows, columns, queries):
    field = [[] for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            field[i].append(count)
            count += 1
    
    answer = []
    for query in queries:
        (x1, y1, x2, y2) = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        backup = field[x1 + 1][y1]
        minNum = backup
        
        for j in range(y1, y2 + 1):
            field[x1][j], backup = backup, field[x1][j]
            if minNum > backup:
                minNum = backup
        
        for i in range(x1 + 1, x2):
            field[i][y2], backup = backup, field[i][y2]
            if minNum > backup:
                minNum = backup
        
        for j in range(y2, y1 - 1, -1):
            field[x2][j], backup = backup, field[x2][j]
            if minNum > backup:
                minNum = backup
        
        for i in range(x2 - 1, x1, -1):
            field[i][x1], backup = backup, field[i][x1]
            if minNum > backup:
                minNum = backup
        
        answer.append(minNum)
              
    return answer