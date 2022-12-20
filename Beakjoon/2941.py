import sys

input = sys.stdin.readline
croAlpabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
inputstring = str(input().rstrip())

for i in range(len(croAlpabet)):
    inputstring = inputstring.replace(str(croAlpabet[i]), 'a')

print(len(inputstring))



