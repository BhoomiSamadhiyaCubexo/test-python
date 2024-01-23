import time
import asyncio

async def fetch_take_order():
    time.sleep(2)
    return "taking order"

async def fetch_prepare_order():
    time.sleep(2)
    return "preparing order"

async def fetch_dispatched_order():
    time.sleep(2)
    return "dispatching order"

async def fetch_delivered_order():
    time.sleep(2)
    return "delivering order"

async def processing_orders():
        take_order, prepare_order, dispatched_order, delivered_order = await asyncio.gather(
             fetch_take_order(),
             fetch_prepare_order(),
             fetch_dispatched_order(),
             fetch_delivered_order()
        )

        summary = f"{take_order}, {prepare_order}, {dispatched_order}, {delivered_order}"
        return summary
    
async def main():
     summary = await processing_orders()
     print(f"order summary: {summary}")

t1 = time.time()

asyncio.run(main())

t2 = time.time()
print(f"time taken by main function {t2-t1}")
