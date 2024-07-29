from pygame import sprite, Vector2

from .enums import enum_animal_type


class Vision():
    def __init__(self, angles: list[int], vision_length: float, animal_type: enum_animal_type):

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
            return_values += vision_angle.get_distanceValues(
                self.vision_length, self.animal_type)

        return return_values


class Vision_Angle():
    def __init__(self, angle: int) -> None:
        self.angle = angle

        self.sprite: sprite.Sprite

        self.distance: Vector2

    def get_distanceValues(self, max_distance: float, animal_type: enum_animal_type) -> list[float]:
        """ returns a list of 2 values first is distance to sprite, second is if its the same type of animal.
        
        :param max_distance: maximum distance animal can see.
        :param animal_type: the type of animal vision is from.

        """
        return_values = []

        if (self.distance):
            return_values.append(max_distance / self.distance)
        else:
            return_values.append(max_distance)

        if (self.sprite.animal_type == animal_type or self.sprite is None):
            return_values.append(1.0)
        else:
            return_values.append(0.0)

        return return_values
