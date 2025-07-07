PRICE_PER_PACKAGE = 99

units_sold = int(input("Enter the number of units sold: "))

if 10 <= units_sold <= 19:
    discount_rate = 0.20
elif 20 <= units_sold <= 49:
    discount_rate = 0.30
elif 50 <= units_sold <= 99:
    discount_rate = 0.40
elif units_sold >= 100:
    discount_rate = 0.50
else:
    discount_rate = 0.0

total_cost = units_sold * PRICE_PER_PACKAGE
discount_amount = total_cost * discount_rate
final_cost = total_cost = discount_amount

final_cost = round(final_cost, 2)

print(f"Total cost for {units_sold} units is: ${final_cost}")
