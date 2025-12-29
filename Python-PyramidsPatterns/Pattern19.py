# 10
# 9 8
# 7 6 5
# 4 3 2 1

num = 10
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num -= 1
    print()
