import enum

class BicycleType(str, enum.Enum):
    MOUNTAIN = "MOUNTAIN"
    ROAD = "ROAD"
    CITY = "CITY"
    ELECTRIC = "ELECTRIC"
