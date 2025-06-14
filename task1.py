number = int(input("Enter an integer: "))


if number % 2 == 0:
    print(" is an even number.")
else:
    print(" is an odd number.")

    total_sum = 0

    for number in range(1, 51):
        total_sum += number
    print("The sum of numbers from 1 to 50 is:", total_sum)


