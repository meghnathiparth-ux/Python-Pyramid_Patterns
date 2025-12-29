#    1
#   121
#  12321
# 1234321

n = int(input("Enter number of rows ==> "))

for i in range(1, n + 1):
    # print spaces
    print(" " * (n - i), end="")

    # print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()