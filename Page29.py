"""
스택 문제
()() YES
(()) YES
(((() NO
제대로 닫힌 괄호 찾기 문제
"""
for _ in range(int(input())):
    stk = []
    ans = 'YES'
    for c in input():
        if c == '(':
            stk.append(c)
        else:
            if len(stk) > 0:
                stk.pop()
            else:
                ans = 'NO'

    if len(stk) > 0:
        ans = 'NO'

    print(ans)

