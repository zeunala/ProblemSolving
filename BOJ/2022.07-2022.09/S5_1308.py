'''
D-Day

입력
첫째 줄에 오늘의 날짜가 주어지고, 두 번째 줄에 D-Day인 날의 날짜가 주어진다.
날짜는 연도, 월, 일순으로 주어지며, 공백으로 구분한다.
입력 범위는 1년 1월 1일부터 9999년 12월 31일 까지 이다.
오늘의 날짜는 항상 D-Day보다 앞에 있다.

출력
오늘부터 D-Day까지 x일이 남았다면, "D-"를 출력하고 그 뒤에 공백 없이 x를 출력한다.
만약 캠프가 천년 이상 지속된다면 (오늘이 y년 m월 d일이고, D-Day가 y+1000년 m월 d일과 같거나 늦다면) 대신 "gg"를 출력한다.
오늘이 2월 29일인 경우는 주어지지 않는다.
'''

'''
- datetime을 이용하여 쉽게 계산할 수 있다.
* Pass/1st/00:07:46
'''
import datetime

year1, month1, day1 = map(int, input().split())
year2, month2, day2 = map(int, input().split())

if (year2 - year1 > 1001) or (year2 - year1 == 1000 and month2 > month1) or (year2 - year1 == 1000 and month2 == month1 and day2 >= day1):
    print("gg")
else:
    a = datetime.date(year1, month1, day1)
    b = datetime.date(year2, month2, day2)
    c = b- a
    print("D-" + str(c.days))