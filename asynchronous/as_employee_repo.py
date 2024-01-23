import asyncio
import time

async def fetch_collect_employee_data():
    await asyncio.sleep(2)
    return f"data of employee"


async def fetch_analyze_attendance():
    await asyncio.sleep(3)
    return f"Analysis of attendance"

async def fetch_compile_report():
    await asyncio.sleep(2)
    return f"Report based on analysis"

async def generate_monthly_reports():
        collect_employee_data, analyze_attendance, compile_report = await asyncio.gather(
            fetch_collect_employee_data(),
            fetch_analyze_attendance(),
            fetch_compile_report()
        )
            
        report = f"{collect_employee_data}, {analyze_attendance}, {compile_report}"
        return report

async def main():
    report = await generate_monthly_reports()
    print(f"Generated Report: {report}")

t1 = time.time()

asyncio.run(main())

t2 = time.time()
print(f"time taken by main function {t2-t1}")