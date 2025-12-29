# ABCD
#  BCD
#   CD
#    D

n = 4
for i in range(n):
    print(" "*i, end="")
    for j in range(i, n):
        print(chr(65+j), end="")
    print()
