# 우선순위 큐는 멀티스레드에 최적화 대신 느림
# heapq는 멀티스레드 고려되진 않지만 빠름.
# 동작은 Queue와 같다 먼저 들어온게 먼저 빠짐.
# 파이썬의 heapq 는 최소힙임. 최대힙을 사용하고 싶으면 부호를 반대로 사용 하면 됨.
import heapq
h = []
heapq.heappush(h, 123)
heapq.heappush(h, 456)
heapq.heappush(h, 789)
print(h)
while len(h):
    print(heapq.heappop(h))
