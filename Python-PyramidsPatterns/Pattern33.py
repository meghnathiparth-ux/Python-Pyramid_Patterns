# A     A
#  B   B
#   C C
#    D

n = 4
for i in range(n):
    for j in range(n*2-1):
        if j == i or j == 2*n-2-i:
            print(chr(65+i), end="")
        else:
            print(" ", end="")
    print()
