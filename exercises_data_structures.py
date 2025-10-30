"""
Python Learning Guide - Data Structures Exercises
Master Python's built-in data structures
"""

# ============================================================
# EXERCISE 2.1: List Operations
# ============================================================
def list_operations():
    """Practice various list operations"""
    # TODO: Create a list of numbers from 1 to 100
    numbers = []
    
    # TODO: Extract all even numbers using list comprehension
    evens = []
    
    # TODO: Extract numbers divisible by 3
    div_by_three = []
    
    # TODO: Create list of tuples (number, square, cube) for 1-20
    number_powers = []
    
    print(f"Even numbers: {evens[:10]}...")  # Show first 10
    print(f"Divisible by 3: {div_by_three[:10]}...")
    print(f"Number powers: {number_powers[:5]}...")


def flatten_nested_list(nested_list):
    """Flatten a nested list into a single list"""
    # Example: [[1,2], [3,4], [5,6]] -> [1,2,3,4,5,6]
    # TODO: Implement flattening (can use list comprehension)
    pass


# ============================================================
# EXERCISE 2.2: Dictionary Practice
# ============================================================
def word_frequency(paragraph):
    """Count word frequency in a paragraph"""
    # TODO: 
    # 1. Split paragraph into words
    # 2. Convert to lowercase
    # 3. Count frequency of each word
    # 4. Return dictionary {word: count}
    pass


def top_n_words(word_freq, n=5):
    """Find the top N most common words"""
    # TODO: Sort dictionary by values and return top N
    # Hint: Use sorted() with key parameter
    pass


def inverted_index(paragraph):
    """Create an inverted index: word -> list of positions"""
    # Example: "hello world hello" -> {"hello": [0, 2], "world": [1]}
    # TODO: Implement inverted index
    pass


# ============================================================
# EXERCISE 2.3: Set Operations
# ============================================================
def set_operations():
    """Practice set operations"""
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [6, 7, 8, 9, 10, 11, 12]
    
    # TODO: Convert to sets
    set1 = set()
    set2 = set()
    
    # TODO: Find common elements (intersection)
    common = set()
    
    # TODO: Elements only in list1 (difference)
    only_first = set()
    
    # TODO: Elements only in list2
    only_second = set()
    
    # TODO: All unique elements (union)
    all_unique = set()
    
    print(f"Common elements: {common}")
    print(f"Only in first: {only_first}")
    print(f"Only in second: {only_second}")
    print(f"All unique: {all_unique}")


# ============================================================
# EXERCISE 2.4: Cache System (Challenge)
# ============================================================
class SimpleCache:
    """Implement a simple cache with FIFO eviction policy"""
    
    def __init__(self, max_size=5):
        """Initialize cache with maximum size"""
        self.max_size = max_size
        # TODO: Choose appropriate data structures
        # Hint: You might need a dictionary and a list
        
    def get(self, key):
        """Get value from cache, return None if not found"""
        # TODO: Implement get and track access count
        pass
    
    def put(self, key, value):
        """Put key-value pair in cache"""
        # TODO: Implement put with FIFO eviction when full
        pass
    
    def get_stats(self):
        """Return cache statistics"""
        # TODO: Return access counts for each key
        pass


# ============================================================
# TEST YOUR SOLUTIONS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Testing Data Structure Exercises")
    print("=" * 60)
    
    # Test list operations
    print("\n--- List Operations ---")
    # Uncomment when ready:
    # list_operations()
    # print(flatten_nested_list([[1,2], [3,4], [5,6]]))
    
    # Test dictionary operations
    print("\n--- Dictionary Operations ---")
    paragraph = """
    Python is an amazing programming language. Python is used in 
    machine learning, web development, and scientific computing. 
    Many companies love Python for its simplicity and power.
    """
    # Uncomment when ready:
    # freq = word_frequency(paragraph)
    # print(f"Word frequency: {freq}")
    # print(f"Top 5 words: {top_n_words(freq)}")
    
    # Test set operations
    print("\n--- Set Operations ---")
    # Uncomment when ready:
    # set_operations()
    
    # Test cache
    print("\n--- Cache System ---")
    # Uncomment when ready:
    # cache = SimpleCache(max_size=3)
    # cache.put("a", 1)
    # cache.put("b", 2)
    # cache.put("c", 3)
    # print(f"Get 'a': {cache.get('a')}")
    # cache.put("d", 4)  # Should evict oldest
    # print(f"Cache stats: {cache.get_stats()}")
