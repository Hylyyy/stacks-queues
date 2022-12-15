print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

from queues3 import Stack

lifo = Stack("1st", "2nd", "3rd")
print("Number of stack:", len(lifo))

for element in lifo:
    print(element)

print("The current number of stack:", len(lifo))
