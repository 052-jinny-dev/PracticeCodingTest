# 카드를 순서대로 쌓아두고(1-2-3-4) 위카드 1제거, 그다음 2가장아래둠(3,4,2) 반복 마지막카드?
from collections import deque

dq = deque()
for i in range(1, int(input()) + 1):
    dq.append(i)

while len(dq) > 1:
    # 가장 위 카드 POP
    dq.popleft()
    # 그다음 가장 위카드 POP하고 가장아래에 append
    dq.append(dq.popleft())

# 마지막 남은 카드
print(dq.popleft())
