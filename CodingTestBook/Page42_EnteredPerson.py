import sys

input = sys.stdin.readline
# 몇명 받기
s = set()
for _ in range(int(input())):
    log = input().strip()
    anal = log.split(" ")
    name = anal[0]
    value = anal[1]
    if value == "enter":
        s.add(name)
    elif value == "leave":
        # s.remove(name)
        if name in s:
            s.remove(name)

for name in sorted(s, reverse=True):
    print(name)

# for _ in range(len(s)):
#    print(s.pop())
