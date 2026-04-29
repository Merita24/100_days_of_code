import requests
import random
from multiprocessing import Pool

BACKENDS=["http://localhost:8001","http://localhost:8002","http://localhost:8003"]

def make_request(_):
    server=random.choice(BACKENDS)
    try:
        response=requests.get(server)
        print(f"Request to {server} returned status code {response.status_code}")
        return response.status_code
    
    except Exception as e:
        print(f"Request failed with error:{e}")
   

        
if __name__=="__main__":
  
    with Pool(processes=5) as pool:
        pool.map(make_request,range(100))  
        
    
