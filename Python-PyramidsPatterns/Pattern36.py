#   A
#  B B
# C   C
#  B B
#   A

n = 3
for i in range(1, n+1):
    print(" "*(n-i) + chr(64+i), end="")
    if i > 1:
        print(" "*(2*i-3) + chr(64+i))
    else:
        print()
for i in range(n-1, 0, -1):
    print(" "*(n-i) + chr(64+i), end="")
    if i > 1:
        print(" "*(2*i-3) + chr(64+i))
    else:
        print()
