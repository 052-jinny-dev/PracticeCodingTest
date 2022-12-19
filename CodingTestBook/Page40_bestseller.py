import sys

# 개수 입력

books = dict()
input = sys.stdin.readline
for _ in range(int(input())):
    # 책제목 입력
    name = input().strip()
    # 책 제목 key로잡고 값이 있다면 value cont++
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

maxValue = max(books.values())
arr = []
for n, v in books.items():
    if v == maxValue:
        arr.append(n)

arr.sort()

for i in range(len(arr)):
    print(arr[i])
    
