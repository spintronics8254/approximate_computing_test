import library

num = [0,0,0,0]
for i in range(0,65536):
    a = library.random_sequence_generator(2)
    if a == 0:
        num[0] = num[0] + 1
    elif a == 1:
        num[1] = num[1] + 1
    elif a == 2:
        num[2] = num[2] + 1
    else:
        num[3] = num[3] + 1
    sum = num[0] + num[1] + num[2] + num[3]


ss = 2**5
print(ss)