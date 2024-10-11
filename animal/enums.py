
from enum import Enum

class Enum_Animal_Type(Enum):
    HERBIVORE = 10
    CARNIVORE = 20
    OMNIVORE = 30
    
    
class Enum_Animal_Actions(Enum):
    NONE = 0
    MOVE_FORWARD = 10
    TURN_LEFT = 20
    TURN_RIGHT = 30
    


if(__name__ == '__main__'):
    print(Enum_Animal_Type(10))