#     P
#    A A
#   R   R
#  T     T
# H H H H H

name = "PARTH"
n = len(name)

for i in range(n):
    for j in range(2*n-1):
        if j == n-i-1 or j == n+i-1 or i == n-1:
            print(name[i], end="")
        else:
            print(" ", end="")
    print()
