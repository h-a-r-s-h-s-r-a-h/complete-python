import multiprocessing
import math
import sys
import time

# Maximum number of digits in an integer
# This is set to a high value to allow large factorial calculations without hitting the limit.
sys.set_int_max_str_digits(1000000)


# Function to calculate factorial using multiprocessing
def computer_factorial(number):
    print(
        f"Computing factorial of {number} in process {multiprocessing.current_process().name}"
    )
    result = math.factorial(number)
    print(
        f"Factorial of {number} is {result} in process {multiprocessing.current_process().name}"
    )
    return result


if __name__ == "__main__":
    # This block ensures that the code runs only when the script is executed directly,
    # not when imported as a module.

    numbers = [
        100000,
        20000,
        30000,
        40000,
        50000,
    ]  # List of numbers to calculate factorial

    t = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(computer_factorial, numbers)

    finished_time = time.time() - t
    print(f"Finished in {finished_time} seconds")
    print("Results:", results)
