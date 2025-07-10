# MultiProcessing with ThreadPoolExecuter

from concurrent.futures import ProcessPoolExecutor
import time


def square_number(number):
    time.sleep(1)  # Simulating a delay
    return number * number


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    # This block ensures that the code runs only when the script is executed directly,
    # not when imported as a module.

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(f"Square: {result}")
    # This code uses ProcessPoolExecutor to run the square_number function concurrently across multiple processes.
