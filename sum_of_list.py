# Sum of all numbers in a list using for loop

def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total

numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)

print("List:", numbers)
print("Sum =", result)
