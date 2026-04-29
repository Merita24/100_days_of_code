import requests
import os
from concurrent.futures import ThreadPoolExecutor

url=["https://images.unsplash.com/photo-1503264116251-35a269479413",
    "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa",
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa",
    "https://images.unsplash.com/photo-1462331940025-496dfbfc7564",
    "https://images.unsplash.com/photo-1504208434309-cb69f4fe52b0",
    "https://images.unsplash.com/photo-1454789548928-9efd52dc4031"
     

]
def download_image(url):
    try:
        response=requests.get(url,stream=True,timeout=10)
        response.raise_for_status()
        
        filename = url.split("/")[-1].split("?")[0] + ".jpg"
        with open(filename,"wb")as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            print(f"Download successful: {filename}")
        else:
            print("Download failed or empty file")
                
                
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        
if __name__=="__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_image,url)