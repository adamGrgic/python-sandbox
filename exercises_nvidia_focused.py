"""
Python Learning Guide - NVIDIA-Focused Exercises
Practice skills relevant for NVIDIA roles
"""

import time
import numpy as np


# ============================================================
# EXERCISE 8.1: Algorithm Optimization
# ============================================================
def naive_matrix_multiply(A, B):
    """Naive matrix multiplication using triple nested loops"""
    # TODO: Implement matrix multiplication from scratch
    # A is m×n, B is n×p, result is m×p
    # Remember: C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    pass


def benchmark_matrix_operations():
    """Compare naive vs NumPy matrix multiplication"""
    size = 100
    
    # Create random matrices
    # TODO: Create two random matrices using both Python lists and NumPy
    
    # Benchmark naive implementation
    # TODO: Time your naive implementation
    
    # Benchmark NumPy implementation
    # TODO: Time NumPy's matrix multiplication
    
    # TODO: Print comparison and speedup factor


# ============================================================
# EXERCISE 8.2: Memory Management
# ============================================================
def process_large_array_naive(size=10_000_000):
    """Process large array all at once (memory-intensive)"""
    # TODO: Create large array and process it
    # This will use a lot of memory!
    pass


def process_large_array_chunked(size=10_000_000, chunk_size=1000):
    """Process large array in chunks (memory-efficient)"""
    # TODO: Process array in chunks using generators
    # This should use much less memory
    pass


def memory_efficient_generator(n):
    """Create a generator for memory-efficient processing"""
    # TODO: Yield values one at a time instead of creating full list
    pass


# ============================================================
# EXERCISE 8.3: Understanding Parallelism
# ============================================================
def process_single(value):
    """A simple function that simulates some work"""
    # Simulate some computation
    result = 0
    for i in range(1000):
        result += value * i
    return result % 1000


def serial_processing(data):
    """Process data serially (one at a time)"""
    # TODO: Process each element in the list one by one
    # Measure the time taken
    pass


def parallel_processing(data):
    """Process data in parallel using multiprocessing"""
    # TODO: Use multiprocessing.Pool to process in parallel
    # Compare time with serial processing
    # from multiprocessing import Pool
    pass


# ============================================================
# EXERCISE 8.4: GPU Simulation
# ============================================================
def element_wise_operation_loops(array):
    """Element-wise operation using loops (slow)"""
    # TODO: Apply operation to each element using loop
    # result[i] = (array[i] ** 2 + array[i]) / 255.0
    pass


def element_wise_operation_vectorized(array):
    """Element-wise operation using NumPy (fast, GPU-like)"""
    # TODO: Use NumPy vectorized operations
    # This is similar to how GPUs process data in parallel
    pass


def compare_element_wise_methods():
    """Compare loop-based vs vectorized operations"""
    # TODO: Create large array and compare both methods
    # This demonstrates why GPUs are so effective
    pass


# ============================================================
# EXERCISE 8.6: Image Processing Pipeline
# ============================================================
def create_dummy_image(width=1000, height=1000):
    """Create a dummy image for processing"""
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)


def grayscale_filter(image):
    """Convert RGB image to grayscale"""
    # TODO: Implement grayscale conversion
    # Formula: gray = 0.299*R + 0.587*G + 0.114*B
    pass


def blur_filter(image, kernel_size=5):
    """Apply simple blur filter"""
    # TODO: Implement a simple average blur
    # (simplified version - don't need full convolution)
    pass


def batch_process_images(num_images=10):
    """Process multiple images and measure time"""
    # TODO: 
    # 1. Create multiple dummy images
    # 2. Apply filters to each
    # 3. Measure total processing time
    # 4. Think about how GPU would parallelize this
    pass


# ============================================================
# EXERCISE 8.7: Neural Network Forward Pass
# ============================================================
def relu(x):
    """ReLU activation function"""
    # TODO: Implement ReLU: max(0, x)
    pass


def softmax(x):
    """Softmax activation function"""
    # TODO: Implement softmax: e^x / sum(e^x)
    pass


class SimpleNeuralNetwork:
    """A simple neural network implementation from scratch"""
    
    def __init__(self, input_size, hidden_size, output_size):
        """Initialize network with random weights"""
        # TODO: Initialize weight matrices and biases
        # Use small random values (e.g., np.random.randn * 0.01)
        self.W1 = None  # input to hidden
        self.b1 = None
        self.W2 = None  # hidden to output
        self.b2 = None
    
    def forward(self, X):
        """Forward pass through the network"""
        # TODO: Implement forward pass
        # 1. Hidden layer: h = ReLU(X @ W1 + b1)
        # 2. Output layer: out = h @ W2 + b2
        # 3. Apply softmax for classification
        pass
    
    def predict(self, X):
        """Make predictions"""
        # TODO: Run forward pass and return predicted classes
        pass


# ============================================================
# EXERCISE 8.8: Code Profiling
# ============================================================
def inefficient_function(n):
    """An intentionally inefficient function"""
    result = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(i * j)
        result.append(sum(temp))
    return result


def optimized_function(n):
    """Optimized version of the above function"""
    # TODO: Optimize the inefficient_function
    # Hint: Use NumPy or mathematical simplification
    pass


def profile_functions():
    """Profile and compare function performance"""
    # TODO: Use timeit or time module to compare
    import timeit
    
    # Time inefficient version
    # Time optimized version
    # Print speedup
    pass


# ============================================================
# GPU CONCEPTS: Understanding CUDA Basics
# ============================================================
class GPUSimulator:
    """
    Simulates basic GPU concepts in Python
    Real GPUs have thousands of cores; this is just for understanding
    """
    
    def __init__(self, num_threads=32):
        """Initialize simulator with thread count"""
        self.num_threads = num_threads
    
    def parallel_map(self, func, data):
        """Simulate parallel execution on GPU"""
        # TODO: Simulate how GPU would process data in parallel
        # In reality, this runs on CPU, but shows the concept
        # Think about dividing work among threads
        pass
    
    def memory_transfer_overhead(self, data):
        """Simulate CPU to GPU memory transfer"""
        # TODO: Demonstrate that data transfer has overhead
        # This is why we try to minimize CPU-GPU transfers
        pass


# ============================================================
# BONUS: Performance Comparison Tool
# ============================================================
def compare_implementations():
    """
    Compare different implementation strategies
    Shows importance of choosing right approach
    """
    sizes = [100, 500, 1000, 2000]
    
    print("\n" + "=" * 70)
    print("Performance Comparison: Matrix Operations")
    print("=" * 70)
    print(f"{'Size':<10} {'Naive (s)':<15} {'NumPy (s)':<15} {'Speedup':<15}")
    print("-" * 70)
    
    # TODO: For each size, compare implementations and print results
    pass


# ============================================================
# TEST YOUR SOLUTIONS
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("NVIDIA-Focused Exercises")
    print("=" * 70)
    
    # Matrix multiplication benchmark
    print("\n--- Matrix Multiplication Benchmark ---")
    # Uncomment when ready:
    # benchmark_matrix_operations()
    
    # Memory management
    print("\n--- Memory Management ---")
    # Uncomment when ready:
    # print("Processing with chunks...")
    # process_large_array_chunked()
    
    # Parallelism comparison
    print("\n--- Serial vs Parallel Processing ---")
    # Uncomment when ready:
    # test_data = list(range(1000))
    # serial_processing(test_data)
    # parallel_processing(test_data)
    
    # Element-wise operations
    print("\n--- Element-wise Operations (GPU-like) ---")
    # Uncomment when ready:
    # compare_element_wise_methods()
    
    # Image processing
    print("\n--- Image Processing Pipeline ---")
    # Uncomment when ready:
    # batch_process_images(num_images=5)
    
    # Neural network
    print("\n--- Neural Network Forward Pass ---")
    # Uncomment when ready:
    # nn = SimpleNeuralNetwork(input_size=10, hidden_size=20, output_size=3)
    # X = np.random.randn(5, 10)  # 5 samples, 10 features
    # predictions = nn.predict(X)
    # print(f"Predictions: {predictions}")
    
    # Profiling
    print("\n--- Code Profiling ---")
    # Uncomment when ready:
    # profile_functions()
    
    # Performance comparison
    print("\n--- Performance Comparison Tool ---")
    # Uncomment when ready:
    # compare_implementations()
    
    print("\n" + "=" * 70)
    print("Complete the TODOs above to implement all exercises!")
    print("=" * 70)
