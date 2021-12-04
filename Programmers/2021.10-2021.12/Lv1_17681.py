'''
비밀지도

- 문제 요구사항 그대로 구현만 하면 되는 문제이다.
n의 범위가 작으므로 시간 복잡도는 신경쓰지 않아도 된다.
* Pass/1st/00:12:23
'''
def numToMap(num, n): # ex. numToMap(9,5)는 " #  #"를 리턴한다.
    result = ""
    for i in range(n):
        if num % 2 == 1:
            result = "#" + result
        else:
            result = " " + result
        num //= 2
            
    return result

def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]
    
    map1 = []
    map2 = []
    
    for i in range(n):
        map1.append(numToMap(arr1[i], n))
        map2.append(numToMap(arr2[i], n))
        
        for j in range(n):
            if map1[i][j] == "#" or map2[i][j] == "#":
                answer[i] += "#"
            else:
                answer[i] += " "
    return answer