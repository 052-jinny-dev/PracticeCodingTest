'''
요세푸스
'''
N, K = map(int, input().split())
peo = [i for i in range(1, N + 1)]
print("peo : " + str(peo))
pt = 0
'''리스트 초기화'''
ans = []
for _ in range(N):
    pt += K - 1
    pt %= len(peo)
    print("pt :" + str(pt))
    temp = peo.pop(pt)
    print("pop : " + str(temp))
    print("peo : " + str(peo))
    print("===================")
    ans.append(temp)

print(f"<{', '.join(map(str, ans))}>")
