test_str = 'youngjinyoon'

print(test_str[0])
print(test_str[1])
print(test_str[-1])
print(test_str[-2])
print(test_str[2:5])

if test_str == 'test':
    print('hello test!')
elif test_str == 'youngjin':
    print('hello yougnjin')
else:
    print('hello unknown')


a = []
b = [1, 3, 5]
c = ['youngjin', 'dongbeom']
d = [7, 9, ['youngjin', 'dongbeom']]
print(b[-1])
print(d[2][0])

test = [1, 2, 3, 4, 5]
test[3] = 6
print(test)

test1 = [1, 2, 3, 4, 5]
print(test1)
test1[2:3] = ['a', 'b']
print(test1)
test1[2:5] = ['c']
print(test1)
del test[2]
print(test1)

print("======")
test2 = [3, 1, 2]
test2.sort()
print(test2)
test2.sort(reverse=True) # == test2.reverse()
print(test2)




