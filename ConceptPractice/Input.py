import sys

input = sys.stdin.readline

# 개수 입력 받기
for _ in range(int(input())):
    # 값 입력 받기 -> youngjin enter
    name, act = input().split()
    # int 값 여러개 입력 받기
    a = list(int, map(input().split()))
    