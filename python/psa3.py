# 1. Print the sum of all the numbers from 1-15
total = 0
for i in range(1, 16):
    total += i
print("The sum of all the numbers from 1-15 is:", total)

# 2. Use a for loop to count from 1-100.
# Print "FIZZ" if odd, "BUZZ" if even
for i in range(1, 101):
    if i % 2 == 0: 
        print("BUZZ")
    else: 
        print("FIZZ")
# 3. create a list of variable with 5 numbers and find the min, max, and average.
numbers = [8, 21, 5, 14, 10]
minimum = min(numbers)
maximum = max(numbers)
average = sum(numbers) / len(numbers)
print("Numbers:", numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)