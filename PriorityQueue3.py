print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

from priority_queue import PriorityQueue
from collections import deque
from heapq import heappop, heappush

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
    
    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))

    def dequeue(self):
        return heappop(self._elements)[1]

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())