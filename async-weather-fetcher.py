import asyncio
import aiohttp

API_KEY="a670150490e63f6ae532eced4cbc17df"
async def fetch_weather(session,url):
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()


async def main():
    urls=["https://api.openweathermap.org/data/2.5/weather?q=London&appid=a670150490e63f6ae532eced4cbc17df",
          "https://api.openweathermap.org/data/2.5/weather?q=New%20York&appid=a670150490e63f6ae532eced4cbc17df",
          "https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=a670150490e63f6ae532eced4cbc17df"
          ]
    
    async with aiohttp.ClientSession() as session:
        tasks=[fetch_weather(session,url)for url in urls]
        results=await asyncio.gather(*tasks)
    for result in results:
        print(result["name"], result["main"]["temp"])

        
asyncio.run(main())