#    A
#   B B
#  C   C
# DDDDDDD

n = 4
for i in range(1, n+1):
    for j in range(1, n*2):
        if j == n-i+1 or j == n+i-1 or i == n:
            print(chr(64+i), end="")
        else:
            print(" ", end="")
    print()
