import time

class Timer:

    def __enter__(self):
        self.start_time = time.time()
        print("Timer started")

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Timer stopped! Elapsed time: {elapsed_time:.2f} seconds")

    

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(limit):
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

# Example usage

with Timer() as t:
    for prime in prime_generator(1000):
        print(prime)
