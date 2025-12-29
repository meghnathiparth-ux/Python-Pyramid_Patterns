# 1
# 3 5
# 7 9 11
# 13 15 17 19

num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
