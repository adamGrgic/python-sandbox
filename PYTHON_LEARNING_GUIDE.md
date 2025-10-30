# Python Learning Guide for NVIDIA

Welcome! This guide will take you from Python basics to skills relevant for working at NVIDIA. Work through each section, complete the exercises, and check your understanding before moving forward.

---

## 📚 Table of Contents

1. [Python Basics](#1-python-basics)
2. [Data Structures](#2-data-structures)
3. [Control Flow](#3-control-flow)
4. [Functions and Scope](#4-functions-and-scope)
5. [Object-Oriented Programming](#5-object-oriented-programming)
6. [File I/O and Error Handling](#6-file-io-and-error-handling)
7. [Essential Libraries](#7-essential-libraries)
8. [🎯 NVIDIA-Focused Topics](#8-nvidia-focused-topics)

---

## 1. Python Basics

### Variables and Types

Python is dynamically typed - you don't need to declare variable types explicitly.

**Key Concepts to Learn:**
- Basic types: `int`, `float`, `str`, `bool`
- Type conversion: `int()`, `float()`, `str()`
- Multiple assignment: `x, y, z = 1, 2, 3`

### 💪 Exercise 1.1: Temperature Converter
```python
# Create a program that:
# 1. Converts Celsius to Fahrenheit
# 2. Converts Fahrenheit to Celsius
# 3. Handles user input and validates it's a number

# Formula: F = (C × 9/5) + 32
# Your code here:
```

### 💪 Exercise 1.2: Variable Swapping
```python
# Swap two variables WITHOUT using a temporary variable
# Hint: Use Python's tuple unpacking
a = 10
b = 20
# Your code here:

print(f"a = {a}, b = {b}")  # Should print: a = 20, b = 10
```

### Strings

**Key Concepts:**
- String indexing and slicing: `s[0]`, `s[1:5]`, `s[::-1]`
- String methods: `.lower()`, `.upper()`, `.strip()`, `.split()`, `.join()`
- f-strings (Python 3.6+): `f"Hello {name}"`
- String formatting: `.format()`

### 💪 Exercise 1.3: String Manipulation
```python
# Given a string, write functions to:
# 1. Check if it's a palindrome (reads same forwards and backwards)
# 2. Count vowels and consonants
# 3. Reverse words in a sentence (not just characters)

text = "A man a plan a canal Panama"
# Your code here:
```

---

## 2. Data Structures

### Lists

Lists are mutable, ordered collections.

**Key Concepts:**
- Creation: `[]`, `list()`, list comprehensions
- Methods: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`
- Slicing: `lst[start:end:step]`
- List comprehensions: `[x**2 for x in range(10)]`

### 💪 Exercise 2.1: List Operations
```python
# Create a list of numbers from 1 to 100
# 1. Extract all even numbers
# 2. Extract all numbers divisible by 3
# 3. Create a list of tuples (number, square, cube) for numbers 1-20
# 4. Flatten a nested list: [[1,2], [3,4], [5,6]] -> [1,2,3,4,5,6]

# Your code here:
```

### Tuples

Tuples are immutable, ordered collections. Great for fixed data.

**Key Concepts:**
- Creation: `()`, `tuple()`, single element: `(x,)`
- Unpacking: `a, b, c = (1, 2, 3)`
- Use cases: returning multiple values, dictionary keys

### Dictionaries

Dictionaries store key-value pairs. Very fast lookups!

**Key Concepts:**
- Creation: `{}`, `dict()`, dict comprehensions
- Methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`
- Dict comprehensions: `{k: v for k, v in items}`

### 💪 Exercise 2.2: Dictionary Practice
```python
# Create a program that:
# 1. Counts word frequency in a paragraph
# 2. Finds the top 5 most common words
# 3. Creates an inverted index (word -> list of positions)

paragraph = """
Python is an amazing programming language. Python is used in 
machine learning, web development, and scientific computing. 
Many companies love Python for its simplicity and power.
"""

# Your code here:
```

### Sets

Sets are unordered collections of unique elements.

**Key Concepts:**
- Creation: `{1, 2, 3}`, `set()`
- Operations: union `|`, intersection `&`, difference `-`
- Methods: `.add()`, `.remove()`, `.discard()`

### 💪 Exercise 2.3: Set Operations
```python
# Given two lists of numbers:
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [6, 7, 8, 9, 10, 11, 12]

# Find:
# 1. Common elements
# 2. Elements only in list1
# 3. Elements only in list2
# 4. All unique elements from both lists

# Your code here:
```

### 🎯 Challenge 2.4: Data Structure Selection
```python
# Implement a simple cache system that:
# 1. Stores key-value pairs
# 2. Has a maximum size (e.g., 5 items)
# 3. When full, removes the oldest item (FIFO)
# 4. Tracks access count for each key

# Which data structures would you use and why?
# Implement it below:
```

---

## 3. Control Flow

### If-Elif-Else

**Key Concepts:**
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- Membership: `in`, `not in`
- Identity: `is`, `is not`
- Ternary operator: `x if condition else y`

### 💪 Exercise 3.1: Conditional Logic
```python
# Create a grade calculator that:
# 1. Takes a score (0-100)
# 2. Returns letter grade (A, B, C, D, F)
# 3. Handles invalid inputs
# 4. Gives special message for perfect score

# Your code here:
```

### Loops

**For Loops:**
- Iterate over sequences: `for item in sequence:`
- `range()`: `range(start, stop, step)`
- `enumerate()`: get index and value
- `zip()`: iterate over multiple sequences

**While Loops:**
- Continue while condition is true
- Be careful of infinite loops!

### 💪 Exercise 3.2: Loop Practice
```python
# 1. Print multiplication table for numbers 1-12
# 2. Find all prime numbers under 100
# 3. Calculate Fibonacci sequence up to n terms
# 4. Implement FizzBuzz (1-100): 
#    - "Fizz" for multiples of 3
#    - "Buzz" for multiples of 5  
#    - "FizzBuzz" for multiples of both

# Your code here:
```

### Loop Control

**Key Concepts:**
- `break`: exit loop entirely
- `continue`: skip to next iteration
- `else`: runs if loop completes without `break`

### 💪 Exercise 3.3: Advanced Loops
```python
# Find the first number divisible by both 7 and 13 between 1-1000
# Print all numbers up to it, but skip multiples of 3
# Use break, continue, and else clause

# Your code here:
```

---

## 4. Functions and Scope

### Function Basics

**Key Concepts:**
- Definition: `def function_name(parameters):`
- Return values: `return value`
- Default arguments: `def func(x=10):`
- `*args` and `**kwargs`
- Type hints (Python 3.5+): `def func(x: int) -> int:`

### 💪 Exercise 4.1: Function Fundamentals
```python
# Create functions for:
# 1. Calculate factorial (recursive and iterative)
# 2. Check if a number is prime
# 3. Find GCD (Greatest Common Divisor) of two numbers
# 4. Generate n terms of Fibonacci sequence

# Your code here:
```

### Scope and Closures

**Key Concepts:**
- LEGB rule: Local, Enclosing, Global, Built-in
- `global` and `nonlocal` keywords
- Closures: functions that remember enclosing scope

### 💪 Exercise 4.2: Closures and Decorators
```python
# 1. Create a counter function using closures
#    counter() should return 1, 2, 3, ... on successive calls
# 2. Create a decorator that times function execution
# 3. Create a decorator that caches function results

# Your code here:
```

### Lambda Functions

**Key Concepts:**
- Anonymous functions: `lambda x: x**2`
- Used with `map()`, `filter()`, `reduce()`
- Keep them simple!

### 💪 Exercise 4.3: Functional Programming
```python
# Given a list of numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map, filter, and lambda to:
# 1. Square all numbers
# 2. Filter even numbers and cube them
# 3. Calculate sum of squares of odd numbers

# Your code here:
```

---

## 5. Object-Oriented Programming

### Classes and Objects

**Key Concepts:**
- Class definition: `class ClassName:`
- `__init__` constructor
- `self` parameter
- Instance vs class variables
- Methods vs functions

### 💪 Exercise 5.1: Basic Classes
```python
# Create a BankAccount class with:
# 1. Properties: account_number, balance, owner
# 2. Methods: deposit, withdraw, get_balance
# 3. Validation: can't withdraw more than balance
# 4. Track transaction history

# Your code here:
```

### Inheritance

**Key Concepts:**
- Parent and child classes
- `super()` function
- Method overriding
- Multiple inheritance (use carefully!)

### 💪 Exercise 5.2: Inheritance
```python
# Create a shape hierarchy:
# 1. Base class: Shape (abstract)
#    - Methods: area(), perimeter()
# 2. Subclasses: Circle, Rectangle, Triangle
# 3. Each implements area() and perimeter()
# 4. Add a method to compare shapes by area

# Your code here:
```

### Special Methods

**Key Concepts:**
- `__str__` and `__repr__`
- `__len__`, `__getitem__`, `__setitem__`
- `__eq__`, `__lt__`, etc.
- `__call__` (make object callable)

### 💪 Exercise 5.3: Magic Methods
```python
# Create a Vector class for 2D/3D vectors with:
# 1. Addition, subtraction (overload + and -)
# 2. Dot product and cross product
# 3. Magnitude calculation
# 4. Nice string representation
# 5. Comparison by magnitude

# Your code here:
```

---

## 6. File I/O and Error Handling

### File Operations

**Key Concepts:**
- Opening files: `open(filename, mode)`
- Modes: 'r', 'w', 'a', 'r+', 'b' (binary)
- Context managers: `with open() as f:`
- Reading: `.read()`, `.readline()`, `.readlines()`
- Writing: `.write()`, `.writelines()`

### 💪 Exercise 6.1: File Processing
```python
# Create a log analyzer that:
# 1. Reads a log file line by line
# 2. Counts different log levels (INFO, WARNING, ERROR)
# 3. Extracts timestamps and creates a summary
# 4. Writes summary to a new file

# Your code here:
```

### Exception Handling

**Key Concepts:**
- `try-except` blocks
- Multiple except clauses
- `else` and `finally`
- `raise` exceptions
- Custom exceptions

### 💪 Exercise 6.2: Robust Error Handling
```python
# Create a safe calculator that:
# 1. Takes two numbers and an operation
# 2. Handles division by zero
# 3. Handles invalid operations
# 4. Handles non-numeric inputs
# 5. Logs errors to a file

# Your code here:
```

### Working with JSON and CSV

**Key Concepts:**
- `json.loads()`, `json.dumps()`
- `csv.reader()`, `csv.writer()`
- `csv.DictReader()`, `csv.DictWriter()`

### 💪 Exercise 6.3: Data File Processing
```python
# Create a data converter that:
# 1. Reads CSV data about GPU performance
# 2. Calculates statistics (mean, median, max)
# 3. Converts to JSON format
# 4. Handles missing or invalid data gracefully

# Sample CSV structure:
# GPU_Model,CUDA_Cores,Memory_GB,TFLOPs,Price
# RTX_4090,16384,24,82.6,1599
# RTX_4080,9728,16,48.7,1199

# Your code here:
```

---

## 7. Essential Libraries

### NumPy - Numerical Computing

**Why it's critical for NVIDIA:** NVIDIA GPUs accelerate NumPy operations through libraries like CuPy!

**Key Concepts:**
- Arrays: `np.array()`, `np.zeros()`, `np.ones()`
- Array operations: broadcasting, vectorization
- Indexing and slicing
- Mathematical functions
- Linear algebra: `np.dot()`, `np.linalg`

### 💪 Exercise 7.1: NumPy Basics
```python
import numpy as np

# 1. Create a 10x10 matrix of random numbers (0-1)
# 2. Find mean, std, min, max along different axes
# 3. Normalize the matrix (scale to 0-1 range)
# 4. Create a 3D array and perform operations
# 5. Matrix multiplication practice

# Your code here:
```

### 💪 Exercise 7.2: NumPy for GPU Simulation
```python
# Simulate GPU operations:
# 1. Create two large matrices (1000x1000)
# 2. Perform matrix multiplication
# 3. Time the operation
# 4. Try element-wise operations
# 5. Compare performance of vectorized vs loop-based code

# Your code here:
```

### Pandas - Data Manipulation

**Key Concepts:**
- DataFrames and Series
- Reading data: `pd.read_csv()`, `pd.read_json()`
- Filtering and selection
- GroupBy operations
- Merging and joining

### 💪 Exercise 7.3: Pandas for Data Analysis
```python
import pandas as pd

# Create a dataset of GPU benchmarks:
# 1. Load/create data with columns: GPU, Cores, Memory, Price, Performance
# 2. Calculate price-to-performance ratio
# 3. Group by manufacturer
# 4. Find best GPUs in each price range
# 5. Create pivot tables

# Your code here:
```

### Matplotlib - Visualization

**Key Concepts:**
- `plt.plot()`, `plt.scatter()`, `plt.bar()`
- Subplots and figures
- Customization: labels, titles, legends
- Saving figures

### 💪 Exercise 7.4: Visualizing Performance Data
```python
import matplotlib.pyplot as plt

# Create visualizations:
# 1. Line plot: GPU performance over generations
# 2. Bar chart: Compare different GPU models
# 3. Scatter plot: Price vs Performance
# 4. Histogram: Distribution of CUDA core counts
# 5. Heatmap: Correlation between GPU specs

# Your code here:
```

---

## 8. 🎯 NVIDIA-Focused Topics

### 8.1 Performance and Optimization

**Why it matters:** NVIDIA is all about high-performance computing!

### 💪 Exercise 8.1: Algorithm Optimization
```python
# Optimize matrix operations:
# 1. Write a naive matrix multiplication (triple nested loop)
# 2. Time it for 100x100 matrices
# 3. Use NumPy to do the same operation
# 4. Compare performance (should be 100x+ faster)
# 5. Understand why vectorization matters for GPUs

import time
import numpy as np

# Your code here:
```

### 💪 Exercise 8.2: Memory Management
```python
# Practice memory-efficient operations:
# 1. Create a large array (10 million elements)
# 2. Process it in chunks instead of all at once
# 3. Use generators for memory efficiency
# 4. Profile memory usage

# Your code here:
```

### 8.2 Parallel Processing Concepts

**Why it matters:** GPUs excel at parallel processing!

### 💪 Exercise 8.3: Understanding Parallelism
```python
# Simulate parallel processing concepts:
# 1. Create a task that can be parallelized (e.g., image processing)
# 2. Use multiprocessing module to run in parallel
# 3. Compare serial vs parallel execution time
# 4. Understand the concept of data parallelism

from multiprocessing import Pool
import time

# Your code here:
```

### 8.3 Introduction to GPU Computing (Conceptual)

**Key Concepts to Understand:**
- CUDA: NVIDIA's parallel computing platform
- Kernels: Functions that run on GPU
- Thread blocks and grids
- Memory hierarchy: Global, Shared, Local
- Data transfer overhead (CPU ↔ GPU)

### 💪 Exercise 8.4: GPU Simulation
```python
# Simulate GPU-like operations in Python:
# 1. Create a function that processes each element independently
# 2. Apply it to a large array
# 3. Think about how this would map to GPU threads
# 4. Identify potential bottlenecks

# Example: Element-wise operation that could be parallelized
def process_pixel(pixel_value):
    # Some complex operation
    return (pixel_value ** 2 + pixel_value) / 255.0

# Your code here:
```

### 8.4 PyTorch/TensorFlow Basics

**Why it matters:** Deep learning frameworks that use NVIDIA GPUs!

### 💪 Exercise 8.5: Tensor Operations
```python
# If you have PyTorch installed, try this:
# import torch

# 1. Create tensors (similar to NumPy arrays)
# 2. Move tensors to GPU (if available)
# 3. Perform operations on GPU
# 4. Understand automatic differentiation (autograd)

# Basic example structure:
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# tensor = torch.randn(1000, 1000).to(device)

# Your code here:
```

### 8.5 Real-World NVIDIA Applications

### 💪 Exercise 8.6: Image Processing Pipeline
```python
# Create an image processing pipeline:
# 1. Load an image (use PIL or OpenCV)
# 2. Apply filters (grayscale, blur, edge detection)
# 3. Batch process multiple images
# 4. Measure processing time
# 5. Think about how GPU acceleration would help

# Your code here:
```

### 💪 Exercise 8.7: Neural Network Forward Pass
```python
# Implement a simple neural network forward pass from scratch:
# 1. Create weight matrices
# 2. Implement ReLU activation
# 3. Forward propagation through layers
# 4. Understand matrix operations (what GPUs accelerate!)

import numpy as np

def relu(x):
    return np.maximum(0, x)

def forward_pass(X, weights, biases):
    # Your code here:
    pass

# Your code here:
```

### 8.6 Performance Profiling

### 💪 Exercise 8.8: Code Profiling
```python
# Profile your code:
# 1. Use timeit for benchmarking
# 2. Use cProfile for detailed profiling
# 3. Identify bottlenecks
# 4. Optimize hot paths

import cProfile
import timeit

# Your code here:
```

---

## 🎓 Final Projects

### Project 1: GPU Benchmark Analyzer
Create a complete application that:
1. Reads GPU benchmark data from CSV
2. Analyzes performance metrics
3. Generates comparison charts
4. Identifies best value GPUs
5. Exports results to JSON and HTML report

### Project 2: Image Batch Processor
Create an image processing pipeline:
1. Reads directory of images
2. Applies multiple filters/transformations
3. Processes in batches for efficiency
4. Handles errors gracefully
5. Logs processing time and statistics

### Project 3: Simple Neural Network Simulator
Build from scratch:
1. Matrix operations for forward/backward pass
2. Multiple layer types (Dense, ReLU, Softmax)
3. Training loop with gradient descent
4. Visualize training progress
5. Test on a simple dataset (e.g., XOR problem)

### Project 4: Performance Comparison Tool
Create a tool that:
1. Compares NumPy vs pure Python performance
2. Tests different array sizes
3. Visualizes results
4. Generates recommendations
5. Simulates what GPU acceleration could provide

---

## 📖 Learning Path Recommendations

### Week 1: Foundations
- Complete sections 1-3 (Basics, Data Structures, Control Flow)
- Do all exercises, don't skip any!
- Practice typing code, don't just read

### Week 2: Intermediate Concepts  
- Complete sections 4-6 (Functions, OOP, File I/O)
- Start thinking in terms of objects and abstractions
- Build small projects combining concepts

### Week 3: Libraries and Tools
- Complete section 7 (NumPy, Pandas, Matplotlib)
- Focus heavily on NumPy - it's crucial for NVIDIA work
- Practice data manipulation and visualization

### Week 4: NVIDIA-Focused Topics
- Complete section 8
- Research CUDA basics (conceptual understanding)
- Learn about GPU architecture (high level)
- Start one of the final projects

### Week 5-6: Deep Dive and Projects
- Complete all final projects
- Read NVIDIA technical blogs
- Learn PyTorch or TensorFlow basics
- Study GPU computing concepts

---

## 🔗 Additional Resources

### Python Documentation
- Official Python Tutorial: https://docs.python.org/3/tutorial/
- Real Python: https://realpython.com/

### NVIDIA-Specific
- NVIDIA Developer Blog: https://developer.nvidia.com/blog/
- CUDA Python: https://developer.nvidia.com/cuda-python
- Rapids (GPU-accelerated data science): https://rapids.ai/

### Books
- "Python Crash Course" by Eric Matthes
- "Fluent Python" by Luciano Ramalho
- "Programming Massively Parallel Processors" (CUDA focus)

### Practice Platforms
- LeetCode (algorithm practice)
- HackerRank (Python practice)
- Project Euler (mathematical problems)

---

## ✅ Self-Assessment Checklist

Before considering yourself ready:

**Python Fundamentals:**
- [ ] Can use all basic data types confidently
- [ ] Understand list/dict comprehensions
- [ ] Can manipulate strings efficiently
- [ ] Comfortable with all control flow structures

**Data Structures:**
- [ ] Know when to use list vs tuple vs set vs dict
- [ ] Can implement complex nested structures
- [ ] Understand time complexity basics

**Functions:**
- [ ] Can write clean, reusable functions
- [ ] Understand scope and closures
- [ ] Can use decorators
- [ ] Familiar with lambda and functional programming

**OOP:**
- [ ] Can design class hierarchies
- [ ] Understand inheritance and composition
- [ ] Can implement magic methods

**Libraries:**
- [ ] Comfortable with NumPy for numerical work
- [ ] Can manipulate data with Pandas
- [ ] Can create visualizations with Matplotlib

**NVIDIA-Relevant Skills:**
- [ ] Understand why GPUs are fast (parallel processing)
- [ ] Can write vectorized code
- [ ] Understand performance optimization basics
- [ ] Familiar with PyTorch or TensorFlow concepts
- [ ] Know basics of memory management

---

## 🚀 Tips for Success

1. **Type, Don't Copy:** Write every line yourself
2. **Break Things:** Experiment and see what happens
3. **Debug:** Use print statements and debuggers
4. **Read Code:** Study well-written Python projects
5. **Build Projects:** Apply what you learn immediately
6. **Time Yourself:** Some operations should be fast
7. **Think Parallel:** Always ask "could this be parallelized?"
8. **Profile First:** Measure before optimizing
9. **Learn Git:** Version control is essential
10. **Ask Why:** Understand the reasoning behind patterns

---

## 💡 Interview Preparation for NVIDIA

### Topics to Master:
1. **Algorithms:** Sorting, searching, dynamic programming
2. **Data Structures:** Arrays, trees, graphs, hash tables
3. **Python Specifics:** Memory management, GIL, performance
4. **Linear Algebra:** Matrix operations (GPU bread and butter!)
5. **Parallel Computing:** Concepts of parallelism and concurrency
6. **System Design:** Scalability, performance considerations

### Sample Interview Questions:
1. "How would you optimize this Python code for GPU execution?"
2. "Explain the difference between list and generator comprehension"
3. "Design a system to process 1 billion images"
4. "What makes matrix multiplication suitable for GPUs?"
5. "How would you profile and optimize a slow Python function?"

---

Good luck with your Python journey and NVIDIA interview! Remember: **consistency beats intensity**. Code every day, even if just for 30 minutes. 🚀

---

*Last Updated: 2025-10-30*
