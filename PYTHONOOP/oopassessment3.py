class LargestNumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers
        self.largest = None

    def find_largest(self):
        if not self.numbers:
            print("The list is empty.")
            return
        self.largest = self.numbers[0]
        for num in self.numbers:
            if num > self.largest:
                self.largest = num

    def display_result(self):
        if self.largest is not None:
            print(f"The largest number is: {self.largest}")

# --- Main Program ---

# Sample input list
array = [45, 78, 23, 56, 89, 12]

# Create object and find largest number
finder = LargestNumberFinder(array)
finder.find_largest()
finder.display_result()