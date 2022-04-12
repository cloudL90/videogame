i = 1
while i <= 10:
    print(i)
    i += 1

row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end='')
    print("")

s = 0
n = int(input("Enter number "))
for i in range(1, n + 1):
    s += i
    print("n:", n, "i:", i, "s:", s)


n = input()
for i in range(1, 11):
    product = int(n) * i
    print(product)

numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)