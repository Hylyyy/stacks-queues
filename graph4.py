print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

from typing import NamedTuple
import networkx as nx

class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float
    longitude: float