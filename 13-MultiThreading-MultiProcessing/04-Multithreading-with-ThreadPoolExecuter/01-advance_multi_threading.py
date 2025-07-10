# MultiThreading with ThreadpoolExecutor
#   Multithreading with ThreadPoolExecutor is a way to run multiple threads concurrently using a pool of worker threads, which makes thread management easier and more efficient.

# What is ThreadPoolExecutor?
#   ThreadPoolExecutor is part of Python's concurrent.futures module. It simplifies running functions in multiple threads by:
#       Automatically managing a pool of threads
#       Reusing threads instead of creating new ones each time
#       Providing a clean and readable way to run code concurrently

from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers(numbers):
    time.sleep(1)  # Simulating a delay
    return [f"Number: {numbers}"]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)
