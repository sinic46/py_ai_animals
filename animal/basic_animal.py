from numpy.random import randint
from pygame import sprite, image, Vector2, transform, Rect
import math
from .enums import enum_animal_type
from .settings import *
from .vision import Vision, Vision_Angle


class Screen_Size:
    def __init__(self,  max_x: int, min_x: int, max_y: int, min_y: int) -> None:

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y


class Animal(sprite.Sprite):

    def __init__(self, id, animal_type: enum_animal_type, image_file_path: str, velocity: int,
                 max_x: int = SCREEN_MAX_X, min_x: int = SCREEN_MIN_X, max_y: int = SCREEN_MAX_Y, min_y: int = SCREEN_MIN_Y, size: tuple[int, int] = (10, 20)) -> None:
        super().__init__()
        self.screen_size: Screen_Size = Screen_Size(max_x, min_x, max_y, min_y)
        self.image = image.load(image_file_path)
        self.rect: Rect = self.image.get_rect()
        self.original_image = image.load(image_file_path)
        self.animal_type: enum_animal_type = animal_type

        self.pos = Vector2(x=randint(min_x, max_x), y=randint(min_y, max_y))

        self.velocity_vector: Vector2 = Vector2(0, 0)

        self.rect.x = round(self.pos.x)
        self.rect.y = round(self.pos.y)

        self.orientation = randint(0, 361)
        self.set_orinentation()
        self.velocity = velocity

        self.move_energy_cost: int = 10
        self.energy: int = 100
        self.agility: int = 15
        self.sight_distance: int = 50
        self.vision: Vision = Vision([45, 90, 135, 225, 270, 315])

    def set_new_sprite_location(self, vector: Vector2):
        """ updates the sprite rect object to new location.

        :param vector: new position for the sprite to move too

        """
        if (vector.x > SCREEN_MAX_X):
            vector.x -= SCREEN_MAX_X
        elif (vector.x < SCREEN_MIN_X):
            vector.x += SCREEN_MAX_X

        if (vector.y > SCREEN_MAX_Y):
            vector.y -= SCREEN_MAX_Y
        elif (vector.y < SCREEN_MIN_Y):
            vector.y += SCREEN_MAX_Y

        self.rect.x = round(vector.x)
        self.rect.y = round(vector.y)

    def set_orinentation(self):
        """ updates sprites roations to match the orientation set in orientation variable

        """
        rot_image = transform.rotate(self.original_image, -self.orientation)
        self.image = rot_image
        self.rect = rot_image.get_rect(center=self.rect.center)

    def turn(self, angle: int):
        """turns sprite base on the angle, can be both positive or negative.

        :param angle: The angle to rotate the sprite in degrees.
        """

        new_orientation = self.orientation + angle

        if (new_orientation > 360):
            new_orientation -= 360
        elif (new_orientation < 0):
            new_orientation += 360

        self.orientation = new_orientation

        self.set_orinentation()

    def move_forward(self):
        """ Moves the sprite straigh forward based of the angle its facing.

        """
        new_pos_vector = self.get_vector_from_angle(
            self.orientation, self.velocity, True)

        self.set_new_sprite_location(new_pos_vector)

    def update(self, DEBUG: bool = False, ):
        """ selects an actionn for the animal to do.

        :param DEBUG: defaults to false, if true debug messages will show


        """
        if (DEBUG):
            print('update')

        choice = randint(1, 4)

        if (choice == 1):
            self.move_forward()
        elif (choice == 2):
            self.turn(self.agility)
        elif (choice == 3):
            self.turn(-self.agility)

    def get_location(self):
        """Returns a string with the location.
        """
        return f'location is X:{self.rect.x} and Y:{self.rect.y}'

    def check_collision(self, sprite_group: sprite.Group, DEBUG: bool = False):
        """Checks if any of the sprite group are colliding with the sprite.

        :param sprite_group: this is the sprite group to check against.
        """
        if sprite.spritecollide(self, sprite_group, False):
            if (DEBUG):
                print('A Collision!!')

            reverse_vector = self.pos - self.velocity_vector

            self.set_new_sprite_location(reverse_vector)

    def set_vision(self, sprite_group: sprite.Group) -> None:
        """ sets the vision object with the current visible sprites

        :param sprite_group: this is the spritegroup to check against.
        """
        for vision_angle in self.vision.vision_angles:
            self.check_collision_on_line(vision_angle, sprite_group)

    def check_collision_on_line(self, vision_angle: Vision_Angle, sprite_group: sprite.Group):
        """ checks if there are any collisions on long a vision angle from sprite.

        :param vision_angle: this is the vision angle to check against. 
        :param sprite_group: this is the sprites that are been checked.

        """
        end_point = self.get_vector_from_angle(
            vision_angle.angle, self.sight_distance)

        for sprite_object in sprite_group:
            sprite_object: sprite.Sprite
            collision_vector = sprite_object.rect.clipline(self.pos, end_point)

            if (collision_vector):
                vision_angle.sprite = sprite_object
                vision_angle.distance = collision_vector
            else:
                vision_angle.sprite = None
                vision_angle.distance = None

    def get_vector_from_angle(self, angle: int, distance: int, set_velocity: bool = False) -> Vector2:
        """ returns a vector based on the angle, distance and sprite postion. can set the sprite velocity_vector if required.
        
        :param angle: the angle in degrees for the vector.
        :param distance: how far the vector needs to be away from sprites position.
        :param set_velocity: boolean if true, sprite velocity_vector will be updated. default is false
        """
        current_pos = self.pos

        velocity_vector = Vector2(x=math.sin(math.radians(angle)) * distance,
                                  y=math.cos(math.radians(-angle)) * -distance)

        if (set_velocity):
            self.velocity_vector = velocity_vector

        return current_pos + velocity_vector


if (__name__ == "__main__"):

    animal1 = Animal(1, enum_animal_type.HERBIVORE, './animal/images/cow.png',
                     500, 0, 500, 0)
