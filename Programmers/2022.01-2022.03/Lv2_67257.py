'''
수식 최대화

- 우선 expression과 우선순위가 주어졌을 때 결과를 계산하는 함수를 만들자.
이후 모든 우선순위에 대하여 계산해서 절댓값이 최대인 것을 리턴한다.
* Pass/1st/00:24:53
'''
def evalSingle(operand1, operator, operand2): # ex. evalSingle(3,"+",2)는 5
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    else:
        return operand1 * operand2
    
def evalExpression(expressionArr, opArr): # 첫번째 인자는 토큰화된 expression, 두번째는 우선순위별로 배열된 operator들
    tempArr = expressionArr[:]
    
    for op in opArr:
        i = 0
        while i < len(tempArr):
            if tempArr[i] == op: # 우선순위가 높은것부터 앞뒤를 계산
                # tempArr[i], tempArr[i+1] 번째 원소가 사라지고 tempArr[i-1]에 결과가 들어감
                tempArr[i - 1] = evalSingle(tempArr[i - 1], tempArr[i], tempArr[i + 1])
                tempArr = tempArr[:i] + tempArr[i+2:]
            else:
                i += 1 # if문에서는 i를 안 더해주는데, 그 자리가 바로 다음 operator가 되기 때문
    
    return tempArr[0] # 결국 하나의 원소만 남게 된다.
    
    

def solution(expression):
    answer = 0
    
    expressionArr = []
    
    i = 0
    val = 0
    for i in range(len(expression)):
        if expression[i] in "0123456789":
            val *= 10
            val += int(expression[i])
        else:
            expressionArr.append(val)
            val = 0
            expressionArr.append(expression[i])
    expressionArr.append(val)
    
    
    # 모든 가능한 우선순위 경우의 수
    opArr = [["+", "-", "*"], ["+", "*", "-"], ["-", "+", "*"], ["-", "*", "+"], ["*", "+", "-"], ["*", "-", "+"]]
    
    for op in opArr:
        temp = abs(evalExpression(expressionArr, op))
        if answer < temp:
            answer = temp
    
    return answer