# When to Use Multithreading:

    # 1. I/O-Bound Tasks
    # Use multithreading when your tasks spend a lot of time waiting — for example:
    # Downloading multiple files
    # Reading/writing from disk or database
    # Handling many web requests (e.g., web servers)
    # Waiting for user input or network response
    # 🧠 Because threads share memory and are lightweight, they’re great for I/O-bound operations.

    # 2. Concurrency in UI Applications
    # In apps like games or GUI software:
    # Use one thread for the UI
    # Use another thread for background tasks (like loading data)
    # This keeps the UI responsive while tasks run in the background.



# ❌ When NOT to Use Multithreading (or be careful):
    # 1. CPU-Bound Tasks
    # If your task involves heavy computations (like image processing, complex math, ML model training), threads may not help due to the Global Interpreter Lock (GIL) in languages like Python.
    # 🛠 Instead, use:
    # Multiprocessing (separate processes instead of threads)
    # Async programming (for even better control over I/O)


import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulating a delay
        
def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulating a delay
        
t = time.time()
print_numbers()
print_letters()
finished_time = time.time() - t
print(f"Finished in {finished_time} seconds")

# This will run sequentially, not concurrently.
# To run them concurrently, we need to use threads.