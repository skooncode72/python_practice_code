num = int(input("Enter the number: "))

num_digits = len(str(num))
temp = num
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** num_digits
    num = num // 10

if temp == total:
    print("Armstrong")
else:
    print("Not Armstrong")