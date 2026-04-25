import string
import itertools
import time

def function_timer(func):
  def wrapper(*args,**kwargs):
    start=time.time()
    result=func(*args,**kwargs)
    end=time.time()
    return f" function ran for {end-start:.6f} seconds"
  return wrapper
  
@function_timer
def brute_force_password(target):
    chars = string.ascii_lowercase
    
    for length in range(1, 5):  
        for attempt in itertools.product(chars, repeat=length):
            guess = ''.join(attempt)
            if guess == target:
                return guess
print(brute_force_password("cat"))