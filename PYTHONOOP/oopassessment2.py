class EvenOddCounter:
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_count = 0
        self.odd_count = 0

    def count_even_odd(self):
        for num in self.numbers:
            if num % 2 == 0:
                self.even_count += 1
            else:
                self.odd_count += 1

    def display_counts(self):
        print(f"Even numbers: {self.even_count}")
        print(f"Odd numbers: {self.odd_count}")

# --- Main Program ---

# Sample input list
array = [2, 1, 4, 3, 6, 5]

# Create an object and run methods
counter = EvenOddCounter(array)
counter.count_even_odd()
counter.display_counts()
