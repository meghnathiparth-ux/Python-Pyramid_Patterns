# ABCDE
#  BCD
#   C
#  BCD
# ABCDE

n = 3
for i in range(n):
    print(" "*i, end="")
    for j in range(i, 2*n-i-1):
        print(chr(65+j), end="")
    print()
for i in range(n-2, -1, -1):
    print(" "*i, end="")
    for j in range(i, 2*n-i-1):
        print(chr(65+j), end="")
    print()
