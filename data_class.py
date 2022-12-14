print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

from dataclasses import dataclass

@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

print(wipers < hazard_lights)

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