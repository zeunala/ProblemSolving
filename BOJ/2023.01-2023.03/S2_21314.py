'''
민겸 수

입력
민겸 수 하나가 주어진다. 민겸 수는 대문자 M과 K로만 이루어진 문자열이며, 길이는 3,000을 넘지 않는다.

출력
주어진 민겸 수가 십진수로 변환되었을 때 가질 수 있는 값 중 가장 큰 값과 가장 작은 값을 두 줄로 나누어 출력한다.
'''

'''
- 민겸 숫자를 정리하면 민겸 숫자는 n개의 M으로 이루어져있거나 n개의 M + 1개의 K으로만 구성될 수 있고,
민겸 숫자가 n자리면 십진수도 n자리고, 끝에 K가 붙었느냐 안붙었느냐에 따라 100.../500... 중 하나로 갈리게 된다.
주어진 민겸 수가 n자리면 십진수도 반드시 n자리이고,
가장 큰 십진수를 만드려면 맨 앞부터 M과 K를 최대한 한 번에 포함해서 5가 앞으로 가도록 해야 한다.
반면 가장 작은 십진수를 만드려면 맨 앞부터 최대한 M만을 포함해서 1이 앞으로 가도록 해야한다.
예를 들어, MKKMMK이면 가장 큰 십진수는 MK/K/MMK, 가장 작은 십진수는 M/K/K/MM/K 이다.
* Fail/1st/00:22:36
'''
def mnumToIntstring(num): # 민겸 숫자를 십진수 문자열로 변환해서 리턴 (ex. "MK" -> "50")
    if len(num) == 0:
        return ""
    
    if num[-1] == "K":
        return str(5 * (10 ** (len(num) - 1)))
    else:
        return str(10 ** (len(num) - 1))
    
target = input()
minValue = ""
maxValue = ""

minScanStart = 0 # 숫자에 반영될 첫 위치
maxScanStart = 0
for i in range(len(target)):
    if target[i] == "K":
        minValue += mnumToIntstring(target[minScanStart:i])
        minValue += mnumToIntstring(target[i])
        maxValue += mnumToIntstring(target[maxScanStart:i + 1])
        
        minScanStart = i + 1
        maxScanStart = i + 1
        
    if target[i] == "M" and i == len(target) - 1:
        minValue += mnumToIntstring(target[minScanStart:i + 1])
        maxValue += mnumToIntstring(target[maxScanStart:i + 1])
        
print(maxValue)
print(minValue)