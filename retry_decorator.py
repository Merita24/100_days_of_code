import time
from functools import wraps
import logging


class MaxRetriesExceeded(Exception):
    pass

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')

def retry_api(max_retries=3,delay=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            attempt=1
            while attempt<=max_retries:
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    logging.error(f"Attempt{attempt} failed with error:{e}")
                    if attempt==max_retries:
                        logging.error("Max retries exceeded. Raising exception.")
                        raise MaxRetriesExceeded("Max retries exceeded") 
                    logging.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempt+=1
        return wrapper
    return decorator

if __name__=="__main__":
    import random
    @retry_api(max_retries=5,delay=2)
    def unstable_api():
        if random.random()<0.7:
            raise ValueError("Simulated API failure")
        return "Success!"
    print(unstable_api())   