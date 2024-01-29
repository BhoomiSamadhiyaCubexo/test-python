import asyncio
import aiohttp  # Asynchronous HTTP Client/Library

async def send_email(recipient):
    await asyncio.sleep(1)  # Simulate the time taken to send an email
    print(f"Email sent to {recipient}")

async def generate_report():
    await asyncio.sleep(2)  # Simulate report generation time
    print("Report generated")

async def fetch_employee_data():
    url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Fetched sales data: {data}")  

async def perform_daily_tasks():
    tasks = [
        send_email('stakeholder@example.com'),
        generate_report(),
        fetch_employee_data()
    ]
    await asyncio.gather(*tasks)

asyncio.run(perform_daily_tasks())
