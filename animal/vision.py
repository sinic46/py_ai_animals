import math
from pygame import sprite, Vector2
from math import sqrt

from .enums import Enum_Animal_Type


class Vision():
    def __init__(self, angles: list[int], vision_length: float, animal_type: Enum_Animal_Type):

        self.animal_type = animal_type

        self.vision_length = vision_length

        self.vision_angles: list[Vision_Angle] = []

        for angle in angles:
            self.vision_angles.append(Vision_Angle(angle))

    def get_vision(self) -> list[float]:
        """ returns a list of floats for each vision angle that alternate between
        1. the distance to then animal as a percentage of max, max distance if nothing there
        2. If there is no sprite or same type return 1 else 0.
        """
        return_values: list[float] = []

        for vision_angle in self.vision_angles:
            return_values += vision_angle.get_distance_normalised_values(
                self.vision_length, self.animal_type)

        return return_values


class Vision_Angle():
    def __init__(self, angle: int) -> None:
        self.angle = angle

        self.sprite: sprite.Sprite

        self.distance: Vector2

    def get_distance_vector_length(self) -> float:
        if (self.distance is not None):
            return math.sqrt((self.distance[0][0] - self.distance[1][0])**2 + (self.distance[0][1] - self.distance[1][1])**2)
        else:
            return 0

    def get_distance_normalised_values(self, max_distance: float, animal_type: Enum_Animal_Type) -> list[float]:
        """ returns a list of 2 values first is a normalised distance to sprite, second is true/false if its the same type of animal.

        :param max_distance: maximum distance animal can see.
        :param animal_type: the type of animal vision is from.

        """
        return_values = []

        if (self.distance) and self.get_distance_vector_length() > 0:
            return_values.append(
                float(self.get_distance_vector_length()/max_distance))
        elif (self.get_distance_vector_length() == 0):
            return_values.append(0)
        else:
            return_values.append(1.0)

        if (self.sprite is None):
            return_values.append(0.0)

        elif (self.sprite.animal_type == animal_type):
            return_values.append(1.0)
        else:
            return_values.append(0.0)

        return return_values
