# 1
# 10
# 101
# 1010

n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j % 2, end="")
    print()
