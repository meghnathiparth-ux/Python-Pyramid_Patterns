# A   C
#   B
# D   F
#   E

n = 6
for i in range(3):
    for j in range(n):
        if (i+j)%4==0 or (i==1 and j%2==0):
            print(chr(65+j), end=" ")
        else:
            print(" ", end=" ")
    print()
