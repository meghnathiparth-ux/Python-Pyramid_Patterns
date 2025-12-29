# ABCD
# EFGH
# IJKL
# MNOP

n = 4
ch = 65
for i in range(n):
    for j in range(n):
        print(chr(ch), end="")
        ch += 1
    print()
