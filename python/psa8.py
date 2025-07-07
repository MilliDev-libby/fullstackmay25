# pt. 1: Calculate results using the formula result = 3x + 5y

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

result = 3 * x + 5 * y 

print(f"The calculated result is{result}.")

# Pt. 2: Pay calculator

hours_worked = float(input("Enter total hours worked: "))
hourly_rate = float(input("Enter hourly pay rate: "))

if hours_worked <= 40:
    regular_pay = hours_worked * hourly_rate
    print(f"Regular pay: {regular_pay}")
else:
    regular_pay = 40 * hourly_rate
    overtime_hours = hours_worked - 40 
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    print(f"Regular pay: {regular_pay}")
    print(f"Overtime pay: {overtime_pay}")
    print(f"Total pay: {total_pay}")