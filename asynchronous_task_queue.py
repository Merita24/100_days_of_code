import threading
import queue

q=queue.Queue()

urls=["url1","url2","url3","url4","url5"]


def worker():
    while not q.empty():
        task=q.get()
        print(f"Processing task:{task}")
        q.task_done()
        
        
for url in urls:
    q.put(url)
    
    
threads=[]

for _ in range(3):
    t=threading.Thread(target=worker)
    t.start()
    threads.append(t)


q.join()


#--------ASYNCHRONOUS---------
import asyncio

queue=asyncio.Queue()

async def producer():
    for url in urls:
        await queue.put(url)
        print(f"Produced task:{url}")
        
        
async def consumer():
    while True:
        url=await queue.get()
        print(f"Consumed task:{url}")
        queue.task_done()
        
        
async def main():
    workers=[asyncio.create_task(consumer()) for _ in range(3)]
    await producer()
    await queue.join()
    for w in workers:
        w.cancel()
        
asyncio.run(main())


