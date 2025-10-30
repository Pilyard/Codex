number = int(input("Write any integer number: "))
total = 0
for i in range(1, number + 1):
    square = i ** 2
    total = total + square
print(total)
