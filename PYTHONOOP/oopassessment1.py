class TemperatureConverter:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
    
    def to_celsius(self):
        celsius = (self.fahrenheit - 32) * 5 / 9
        return round(celsius, 1) # rounded to 1 decimal place
    
# --- Main Program ---

# Ask user for input
try:
    temp_f = float(input("Enter the temperature in Fahrenheit: "))
    converter = TemperatureConverter(temp_f)
    temp_c = converter.to_celsius()

    # output
    print(f"Temperature in Celsius: {temp_c}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")



