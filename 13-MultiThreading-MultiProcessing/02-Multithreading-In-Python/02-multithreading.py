import threading
import time


def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulating a delay


def print_letters():
    for letter in "abcde":
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulating a delay


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

# If you don't call join(), the whole program might finish before the threads complete.

finished_time = time.time() - t
print(f"Finished in {finished_time} seconds")
