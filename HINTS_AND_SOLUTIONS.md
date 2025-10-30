# Hints and Solutions

This file provides hints and sample solutions for exercises. **Try to solve problems yourself first!** Only look at hints when truly stuck.

---

## Basic Exercises

### Exercise 1.1: Temperature Converter

<details>
<summary>Click for Hint</summary>

**Hint:** 
- Formula for C to F: `(celsius * 9/5) + 32`
- Formula for F to C: `(fahrenheit - 32) * 5/9`
- Use `try-except` to handle invalid inputs
- Use `input()` to get user input

</details>

<details>
<summary>Click for Solution</summary>

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Enter unit (C/F): ").upper()
        
        if unit == 'C':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
        elif unit == 'F':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")
        else:
            print("Invalid unit! Use C or F")
    except ValueError:
        print("Invalid temperature! Please enter a number")
```

</details>

---

### Exercise 1.2: Variable Swapping

<details>
<summary>Click for Hint</summary>

**Hint:** In Python, you can use tuple unpacking: `a, b = b, a`

</details>

<details>
<summary>Click for Solution</summary>

```python
def swap_variables():
    a = 10
    b = 20
    print(f"Before: a = {a}, b = {b}")
    
    # Tuple unpacking - Pythonic way!
    a, b = b, a
    
    print(f"After: a = {a}, b = {b}")
```

</details>

---

### Exercise 1.3: String Manipulation

<details>
<summary>Click for Hint</summary>

**Hints:**
- **Palindrome:** Remove spaces, convert to lowercase, compare with reverse
- **Vowels/Consonants:** Use `in` to check if character is in a string of vowels
- **Reverse Words:** Use `.split()` and `.join()` with slicing

</details>

<details>
<summary>Click for Solution</summary>

```python
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]

def count_vowels_consonants(text):
    vowels = 'aeiouAEIOU'
    v_count = sum(1 for char in text if char in vowels)
    c_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return (v_count, c_count)

def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])
```

</details>

---

## Data Structure Exercises

### Exercise 2.1: List Operations

<details>
<summary>Click for Hint</summary>

**Hints:**
- Use `range(1, 101)` to create numbers 1-100
- List comprehension: `[x for x in numbers if condition]`
- For tuples: `[(x, x**2, x**3) for x in range(1, 21)]`
- Flatten: Use nested list comprehension

</details>

<details>
<summary>Click for Solution</summary>

```python
def list_operations():
    numbers = list(range(1, 101))
    
    evens = [x for x in numbers if x % 2 == 0]
    
    div_by_three = [x for x in numbers if x % 3 == 0]
    
    number_powers = [(x, x**2, x**3) for x in range(1, 21)]
    
    print(f"Even numbers: {evens[:10]}...")
    print(f"Divisible by 3: {div_by_three[:10]}...")
    print(f"Number powers: {number_powers[:5]}...")

def flatten_nested_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
```

</details>

---

### Exercise 2.2: Dictionary Practice

<details>
<summary>Click for Hint</summary>

**Hints:**
- **Word frequency:** Use a dictionary and `.get()` method or `defaultdict`
- **Top N words:** Use `sorted()` with `key=lambda x: x[1]` and reverse
- **Inverted index:** Enumerate words and build dict with lists as values

</details>

<details>
<summary>Click for Solution</summary>

```python
def word_frequency(paragraph):
    words = paragraph.lower().split()
    freq = {}
    for word in words:
        # Remove punctuation
        word = word.strip('.,!?')
        freq[word] = freq.get(word, 0) + 1
    return freq

def top_n_words(word_freq, n=5):
    # Sort by frequency (value) in descending order
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

def inverted_index(paragraph):
    words = paragraph.lower().split()
    index = {}
    for pos, word in enumerate(words):
        word = word.strip('.,!?')
        if word not in index:
            index[word] = []
        index[word].append(pos)
    return index
```

</details>

---

### Exercise 2.3: Set Operations

<details>
<summary>Click for Hint</summary>

**Hints:**
- Convert lists to sets: `set(list1)`
- Intersection: `set1 & set2` or `set1.intersection(set2)`
- Difference: `set1 - set2`
- Union: `set1 | set2`

</details>

<details>
<summary>Click for Solution</summary>

```python
def set_operations():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [6, 7, 8, 9, 10, 11, 12]
    
    set1 = set(list1)
    set2 = set(list2)
    
    common = set1 & set2
    only_first = set1 - set2
    only_second = set2 - set1
    all_unique = set1 | set2
    
    print(f"Common elements: {common}")
    print(f"Only in first: {only_first}")
    print(f"Only in second: {only_second}")
    print(f"All unique: {all_unique}")
```

</details>

---

### Exercise 2.4: Cache System (Challenge)

<details>
<summary>Click for Hint</summary>

**Hints:**
- Use a dictionary for key-value storage
- Use a list to track insertion order (FIFO)
- Use another dictionary for access counts
- When full, remove the first item from the order list

</details>

<details>
<summary>Click for Solution</summary>

```python
class SimpleCache:
    def __init__(self, max_size=5):
        self.max_size = max_size
        self.cache = {}  # key -> value
        self.order = []  # track insertion order
        self.access_count = {}  # key -> count
        
    def get(self, key):
        if key in self.cache:
            self.access_count[key] = self.access_count.get(key, 0) + 1
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            return
        
        if len(self.cache) >= self.max_size:
            # Remove oldest (FIFO)
            oldest = self.order.pop(0)
            del self.cache[oldest]
            if oldest in self.access_count:
                del self.access_count[oldest]
        
        self.cache[key] = value
        self.order.append(key)
        self.access_count[key] = 0
    
    def get_stats(self):
        return self.access_count
```

</details>

---

## NVIDIA-Focused Exercises

### Exercise 8.1: Matrix Multiplication

<details>
<summary>Click for Hint</summary>

**Hints:**
- Naive: Triple nested loop (i, j, k)
- NumPy: Use `@` operator or `np.matmul()`
- Use `time.time()` to measure execution time
- Expected speedup: 50-1000x for 100×100 matrices

</details>

<details>
<summary>Click for Solution</summary>

```python
import time
import numpy as np

def naive_matrix_multiply(A, B):
    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])
    
    if n != n2:
        raise ValueError("Matrix dimensions don't match")
    
    # Initialize result matrix
    C = [[0 for _ in range(p)] for _ in range(m)]
    
    # Triple nested loop
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def benchmark_matrix_operations():
    size = 100
    
    # Python lists
    A_list = [[float(i+j) for j in range(size)] for i in range(size)]
    B_list = [[float(i-j) for j in range(size)] for i in range(size)]
    
    # NumPy arrays
    A_np = np.random.rand(size, size)
    B_np = np.random.rand(size, size)
    
    # Benchmark naive
    start = time.time()
    C_naive = naive_matrix_multiply(A_list, B_list)
    naive_time = time.time() - start
    
    # Benchmark NumPy
    start = time.time()
    C_numpy = A_np @ B_np
    numpy_time = time.time() - start
    
    print(f"Naive implementation: {naive_time:.4f} seconds")
    print(f"NumPy implementation: {numpy_time:.6f} seconds")
    print(f"Speedup: {naive_time/numpy_time:.1f}x")
```

</details>

---

### Exercise 8.2: Memory Management

<details>
<summary>Click for Hint</summary>

**Hints:**
- Use generator: `yield` instead of `return`
- Process chunks: Use slicing `array[i:i+chunk_size]`
- Compare memory using `sys.getsizeof()` or memory_profiler

</details>

<details>
<summary>Click for Solution</summary>

```python
def process_large_array_chunked(size=10_000_000, chunk_size=1000):
    for i in range(0, size, chunk_size):
        chunk = range(i, min(i + chunk_size, size))
        # Process chunk
        result = sum(x**2 for x in chunk)
    return "Processed in chunks"

def memory_efficient_generator(n):
    for i in range(n):
        yield i**2  # Only generates one value at a time

# Usage
gen = memory_efficient_generator(1000000)
# Only computes values as needed
first_10 = [next(gen) for _ in range(10)]
```

</details>

---

### Exercise 8.4: Element-wise Operations

<details>
<summary>Click for Hint</summary>

**Hints:**
- Loop version: Use list comprehension or for loop
- Vectorized: `(array ** 2 + array) / 255.0` in one line
- This shows why GPUs are so fast - they do vectorized ops in hardware!

</details>

<details>
<summary>Click for Solution</summary>

```python
import numpy as np
import time

def element_wise_operation_loops(array):
    result = []
    for val in array:
        result.append((val ** 2 + val) / 255.0)
    return result

def element_wise_operation_vectorized(array):
    return (array ** 2 + array) / 255.0

def compare_element_wise_methods():
    size = 1_000_000
    
    # Python list
    data_list = list(range(size))
    
    # NumPy array
    data_np = np.arange(size, dtype=float)
    
    # Time loop version
    start = time.time()
    result_loop = element_wise_operation_loops(data_list)
    loop_time = time.time() - start
    
    # Time vectorized version
    start = time.time()
    result_vec = element_wise_operation_vectorized(data_np)
    vec_time = time.time() - start
    
    print(f"Loop-based: {loop_time:.4f} seconds")
    print(f"Vectorized: {vec_time:.6f} seconds")
    print(f"Speedup: {loop_time/vec_time:.1f}x")
    print("\nThis is similar to how GPUs process data in parallel!")
```

</details>

---

### Exercise 8.7: Neural Network

<details>
<summary>Click for Hint</summary>

**Hints:**
- ReLU: `np.maximum(0, x)`
- Softmax: `np.exp(x) / np.sum(np.exp(x))`
- Forward pass: `z1 = X @ W1 + b1`, then `a1 = relu(z1)`
- Use small random weights: `np.random.randn() * 0.01`

</details>

<details>
<summary>Click for Solution</summary>

```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize with small random weights
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
    
    def forward(self, X):
        # Hidden layer
        self.z1 = X @ self.W1 + self.b1
        self.a1 = relu(self.z1)
        
        # Output layer
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = softmax(self.z2)
        
        return self.a2
    
    def predict(self, X):
        probs = self.forward(X)
        return np.argmax(probs, axis=1)

# Example usage
nn = SimpleNeuralNetwork(input_size=10, hidden_size=20, output_size=3)
X = np.random.randn(5, 10)  # 5 samples
predictions = nn.predict(X)
print(f"Predictions: {predictions}")
```

</details>

---

## General Problem-Solving Strategies

### When You're Stuck:

1. **Break It Down**
   - Solve a simpler version first
   - Work with smaller data
   - Test each part separately

2. **Debug Effectively**
   ```python
   # Add print statements
   print(f"Variable value: {var}")
   print(f"Type: {type(var)}")
   print(f"Length: {len(var)}")
   ```

3. **Use Python's Built-in Help**
   ```python
   help(function_name)
   dir(object)  # See available methods
   ```

4. **Test Edge Cases**
   - Empty inputs
   - Single element
   - Very large inputs
   - Invalid inputs

5. **Common Patterns**
   ```python
   # Accumulator pattern
   result = []
   for item in items:
       result.append(process(item))
   
   # Counter pattern
   count = 0
   for item in items:
       if condition(item):
           count += 1
   
   # Dictionary pattern
   d = {}
   for item in items:
       d[key] = d.get(key, 0) + 1
   ```

---

## Performance Tips

### Make Your Code Faster:

1. **Use Built-in Functions** - They're implemented in C
   ```python
   # Slow
   total = 0
   for x in numbers:
       total += x
   
   # Fast
   total = sum(numbers)
   ```

2. **Use List Comprehensions**
   ```python
   # Slower
   squares = []
   for x in range(100):
       squares.append(x**2)
   
   # Faster
   squares = [x**2 for x in range(100)]
   ```

3. **Use NumPy for Numerical Work**
   ```python
   # Slow
   result = [x**2 for x in range(1000000)]
   
   # Fast
   result = np.arange(1000000) ** 2
   ```

4. **Avoid Repeated Lookups**
   ```python
   # Slow
   for i in range(len(my_list)):
       result += my_list[i] * 2
   
   # Fast
   for item in my_list:
       result += item * 2
   ```

---

## Remember:

- **Try yourself first** - Struggling is part of learning!
- **Understand, don't memorize** - Know why it works
- **Practice daily** - Consistency beats intensity
- **Build projects** - Apply what you learn

Good luck with your learning journey! 🚀
