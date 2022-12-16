from typing import NamedTuple

print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")


class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )

