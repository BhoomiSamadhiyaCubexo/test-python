import time

def take_order(order_no):
    print(f"order taken for {order_no}")
    time.sleep(2)

def prepare_order(order_no):
    print(f"preparing order {order_no}")
    time.sleep(5)

def dispatched_order(order_no):
    print(f"dispatching order {order_no}")
    time.sleep(2)

def delivered_order(order_no):
    print(f"delivered order {order_no}")
    time.sleep(2)

def processing_orders(order_list):
    for order in order_list:
        take_order(order)
        prepare_order(order)
        dispatched_order(order)
        delivered_order(order)
    
#list of order numbers 
orders = [1, 2, 3, 4]

#synchronously processes the orders
processing_orders(orders)
