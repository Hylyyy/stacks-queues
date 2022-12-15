print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

from queues2 import Queue

fifo = Queue("1st", "2nd", "3rd")
print(len(fifo))

for element in fifo:
    print(element)

print("The current queues:", len(fifo))