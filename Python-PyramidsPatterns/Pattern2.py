#     1
#    12
#   123
#  1234
# 12345

n = int(input("Enter number of rows ==> "))

for i in range(1, n + 1):
    # print spaces
    print(" " * (n - i), end="")

    # print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    print()