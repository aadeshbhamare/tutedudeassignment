num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
print("Another method to print two outputs simultaneously")

while True:
    user_input = input("Enter a number")
    if user_input.lower() == 'q':
        print("Program terminated.")
        break
    num = int(user_input)
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

total = 0
for i in range(1, 51):
    total = total + i
print("The sum of integers from 1 to 50 is:", total)
