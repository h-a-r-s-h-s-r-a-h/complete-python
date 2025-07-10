# When to Use Multiprocessing:

# 1. CPU-Bound Tasks
    # Use multiprocessing for tasks like:
    # Image processing
    # Data analysis (large datasets)
    # Machine learning model training
    # Complex mathematical calculations
    # Video encoding
    # These tasks benefit from parallel execution across multiple CPU cores.

# Why Not Threads for CPU-bound Work?

    # In languages like Python, the Global Interpreter Lock (GIL) prevents multiple threads from executing Python bytecode in true parallel — so multithreading doesn't speed up CPU-heavy tasks.
    # Multiprocessing creates separate processes with their own memory space, allowing true parallelism.


# Don’t Use Multiprocessing When:
    # Your tasks are I/O-bound (e.g., waiting for a network or disk)

    # Your tasks require frequent data sharing (since processes don’t share memory easily)


import multiprocessing
import time

def square_numbers():
    for i in range(1, 6):
        print(f"Square: {i * i}")
        time.sleep(1)  # Simulating a delay

def cube_numbers():
    for i in range(1, 6):
        print(f"Cube: {i * i * i}")
        time.sleep(1)  # Simulating a delay

if __name__ == '__main__':
    # This block ensures that the code runs only when the script is executed directly,
    # not when imported as a module.

    # create two separate processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    p1.start()
    p2.start()
    # Wait for both processes to finish
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"Finished in {finished_time} seconds")
