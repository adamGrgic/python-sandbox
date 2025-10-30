"""
Python Learning Guide - Basic Exercises
Work through these exercises to master Python fundamentals
"""

# ============================================================
# EXERCISE 1.1: Temperature Converter
# ============================================================
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    # TODO: Implement this function
    # Formula: F = (C × 9/5) + 32
    pass


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    # TODO: Implement this function
    # Formula: C = (F - 32) × 5/9
    pass


def temperature_converter():
    """Main temperature converter with user input"""
    # TODO: 
    # 1. Ask user for temperature and unit (C or F)
    # 2. Convert and display result
    # 3. Handle invalid inputs
    pass


# ============================================================
# EXERCISE 1.2: Variable Swapping
# ============================================================
def swap_variables():
    """Swap two variables without using a temp variable"""
    a = 10
    b = 20
    print(f"Before: a = {a}, b = {b}")
    
    # TODO: Swap a and b using tuple unpacking
    
    print(f"After: a = {a}, b = {b}")


# ============================================================
# EXERCISE 1.3: String Manipulation
# ============================================================
def is_palindrome(text):
    """Check if text is a palindrome (ignoring spaces and case)"""
    # TODO: Implement palindrome checker
    pass


def count_vowels_consonants(text):
    """Count vowels and consonants in text"""
    # TODO: Return a tuple (vowels, consonants)
    pass


def reverse_words(sentence):
    """Reverse the order of words in a sentence"""
    # Example: "Hello World" -> "World Hello"
    # TODO: Implement word reversal
    pass


# ============================================================
# TEST YOUR SOLUTIONS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Testing Basic Exercises")
    print("=" * 60)
    
    # Test temperature conversion
    print("\n--- Temperature Converter ---")
    # Uncomment when ready:
    # print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    # print(f"32°F = {fahrenheit_to_celsius(32)}°C")
    
    # Test variable swapping
    print("\n--- Variable Swapping ---")
    # Uncomment when ready:
    # swap_variables()
    
    # Test string manipulation
    print("\n--- String Manipulation ---")
    # Uncomment when ready:
    # print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    # print(f"Vowels and consonants in 'Hello': {count_vowels_consonants('Hello')}")
    # print(f"Reversed words: {reverse_words('Hello World')}")
