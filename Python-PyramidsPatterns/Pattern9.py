# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

n = 5
for i in range(n, 0, -1):
    print(' ' * (n-i) + ' '.join(str(x) for x in range(1, i+1)))
