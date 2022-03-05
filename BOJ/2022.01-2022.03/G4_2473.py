'''
세 용액

입력
첫째 줄에는 전체 용액의 수 N이 입력된다. N은 3 이상 5,000 이하의 정수이다.
둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다.
이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다.
N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

출력
첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 세 용액의 특성값을 출력한다.
출력해야하는 세 용액은 특성값의 오름차순으로 출력한다.
특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.
'''

'''
- 용액을 만드는 경우의 수는 (산, 산, 산), (산, 산, 염), (산, 염, 염), (염, 염, 염) 중 하나이다.
(산, 산, 산), (염, 염, 염)은 쉽게 구할 수 있으며,
(산, 산, 염)과 같은 경우는 일단 산성 2개를 합친 값들을 나열하고 염기를 그 안에서 끼우는 형태로 생각할 수 있다.
* Fail/1st/00:32:48
'''
import sys
from bisect import bisect_left

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

plus = [] # 산성들의 배열
minus = [] # 염기성들의 배열
plus2 = [] # 산성 2개를 합친 경우들
plus2Comp = [] # plus2Comp[i]는 plus2[i]가 어떤 두 용액에서 나왔는지 저장함
minus2 = [] # 염기성 2개를 합친 경우들
minus2Comp = [] # minus2Comp[i]는 minus2[i]가 어떤 두 용액에서 나왔는지 저장함

for e in arr:
    if e >= 0:
        plus.append(e)
    else:
        minus.append(e)
        
plus.sort()
minus.sort()

for i in range(len(plus)):
    for j in range(i+1, len(plus)):
        plus2.append(plus[i]+plus[j])
        plus2Comp.append((plus[i], plus[j]))
        
for i in range(len(minus)):
    for j in range(i+1, len(minus)):
        minus2.append(minus[i]+minus[j])
        minus2Comp.append((minus[i],minus[j]))
        
PPPCase = int(1e20) # (산, 산, 산)
MMMCase = int(1e20) # (염, 염, 염)
PPMCase = int(1e20) # (산, 산, 염)
PPMCaseComp = None # 그 최소가 될 때의 용액들의 값
PMMCase = int(1e20) # (산, 염, 염)
PMMCaseComp = None # 그 최소가 될 때의 용액들의 값

if len(plus) >= 3:
    PPPCase = abs(plus[0] + plus[1] + plus[2])
if len(minus) >= 3:
    MMMCase = abs(minus[-1] + minus[-2] + minus[-3])
    
for e in minus: # (산, 산, 염)의 경우를 찾음
    idx = bisect_left(plus2, -e) # -e에 가장 가까운 걸 찾는다
    if idx < len(plus2) and PPMCase > abs(e + plus2[idx]):
        PPMCase = abs(e + plus2[idx])
        PPMCaseComp = (e, plus2Comp[idx][0], plus2Comp[idx][1])
    if idx - 1 >= 0 and PPMCase > abs(e + plus2[idx - 1]): # idx 앞뒤로도 찾아본다
        PPMCase = abs(e + plus2[idx - 1])
        PPMCaseComp = (e, plus2Comp[idx - 1][0], plus2Comp[idx - 1][1])
    if idx + 1 < len(plus2) and PPMCase > abs(e + plus2[idx + 1]):
        PPMCase = abs(e + plus2[idx + 1])
        PPMCaseComp = (e, plus2Comp[idx + 1][0], plus2Comp[idx + 1][1])
        
for e in plus: # (산, 염, 염)의 경우를 찾음
    idx = bisect_left(minus2, -e) # -e에 가장 가까운 걸 찾는다
    if idx < len(minus2) and PMMCase > abs(e + minus2[idx]):
        PMMCase = abs(e + minus2[idx])
        PMMCaseComp = (minus2Comp[idx][0], minus2Comp[idx][1], e)
    if idx - 1 >= 0 and PMMCase > abs(e + minus2[idx - 1]): # idx 앞뒤로도 찾아본다
        PMMCase = abs(e + minus2[idx - 1])
        PMMCaseComp = (minus2Comp[idx - 1][0], minus2Comp[idx - 1][1], e)
    if idx + 1 < len(minus2) and abs(PMMCase > e + minus2[idx + 1]):
        PMMCase = abs(e + minus2[idx + 1])
        PMMCaseComp = (minus2Comp[idx + 1][0], minus2Comp[idx + 1][1], e)


# 결과 출력
if PPPCase <= PPMCase and PPPCase <= PMMCase and PPPCase <= MMMCase:
    print(plus[0], plus[1], plus[2])
elif MMMCase <= PPPCase and MMMCase <= PPMCase and MMMCase <= PMMCase:
    print(minus[-3], minus[-2], minus[-1])
elif PPMCase <= PPPCase and PPMCase <= PMMCase and PPMCase <= MMMCase:
    print(PPMCaseComp[0], PPMCaseComp[1], PPMCaseComp[2])
elif PMMCase <= PPPCase and PMMCase <= PPMCase and PMMCase <= MMMCase:
    print(PMMCaseComp[0], PMMCaseComp[1], PMMCaseComp[2])