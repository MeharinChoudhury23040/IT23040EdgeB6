import threading
import queue
import time


class Order:
    order_count = 0

    def __init__(self):
        Order.order_count += 1
        self.order_id = Order.order_count

    def get_order_id(self):
        return self.order_id


class OrderQueue:
    def __init__(self):
        self.orders = queue.Queue()

    def add_order(self, order):
        self.orders.put(order)

    def get_order(self):
        return self.orders.get()


class DeliveryAgent(threading.Thread):
    def __init__(self, name, order_queue):
        super().__init__()
        self.agent_name = name
        self.order_queue = order_queue

    def run(self):
        while True:
            order = self.order_queue.get_order()
            if order is None:
                break
            print(f"{self.agent_name} is delivering Order-{order.get_order_id()}")
            time.sleep(2)


order_queue = OrderQueue()

# Create 3 delivery agents
agents = [DeliveryAgent(f"Agent-{i}", order_queue) for i in range(1, 4)]

for agent in agents:
    agent.start()

# Simulate order creation
for _ in range(10):
    input("Press Enter to place a new order... ")
    order_queue.add_order(Order())

# Notify agents to stop
for _ in agents:
    order_queue.add_order(None)

for agent in agents:
    agent.join()

print("All orders delivered.")
