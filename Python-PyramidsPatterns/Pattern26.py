#    A
#   BBB
#  CCCCC
# DDDDDDD

n = 4
for i in range(n):
    print(" "*(n-i-1) + chr(65+i)*(2*i+1))
