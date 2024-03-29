'''
캐시

- 문제 조건 그대로 구현만 하면 되는 문제이다.
캐시에 저장할 때 마지막 참조 시간을 저장하고 이 값이 적은것부터 빼면 된다.
캐시 크기가 작으므로 캐시에서 값을 뺄 때 O(n)이 시간이 걸려도 될 것이다.
* Fail/1st/00:18:00
- cache hit가 날 때도 cache를 최신 참조 시각으로 수정하는 것을 빠뜨려서 수정하였다.
* Pass/2st/00:20:00
- 다른 사람의 풀이를 보고 생각해보니 번거롭게 딕셔너리 쓸 필요 없이,
deque으로 큐를 구현해서 코드를 작성해도 충분할 것으로 보인다.
'''
def deleteLRU(arr):
    minValue = min(arr.values())
    for e in arr.keys():
        if arr[e] == minValue:
            del arr[e]
            return
        
def solution(cacheSize, cities):
    answer = 0
    cache = {} # (도시명, 마지막 참조 시각) 저장
    
    for i in range(len(cities)):
        if cities[i].lower() in cache:
            cache[cities[i].lower()] = i
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache[cities[i].lower()] = i
            else:
                if cacheSize >= 1:
                    deleteLRU(cache)
                    cache[cities[i].lower()] = i
            answer += 5
                
    return answer