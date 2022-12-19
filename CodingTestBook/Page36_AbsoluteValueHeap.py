import heapq
import sys

hq = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        # print안에 if조건 print(참 if 조건 else 거짓)
        print(heapq.heappop(hq)[1] if len(hq) > 0 else 0)
    else:
        # abs 절대값 함수
        heapq.heappush(hq, (abs(x), x)) 
