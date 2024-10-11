import os
import pygame
from pygame.locals import *

import animal
from animal.settings import *

window_x = 2000
window_y = 100

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (window_x, window_y)


pygame.init()

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption(TITLE)


cows = [animal.Cow(count, max_x=SCREEN_MAX_X, min_x=SCREEN_MIN_X,
                   max_y=SCREEN_MAX_Y, min_y=SCREEN_MIN_Y) for count in range(20)]

cows_group: animal.CowGroup = animal.CowGroup()

all_animals_group: pygame.sprite.Group = pygame.sprite.Group()

cows_group.add(cows)

all_animals_group.add(cows)

print(cows_group)
counter = 0

# Loop until the user clicks the close button.
active = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while active:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    screen.fill(GREEN)
    counter += 1

    print(f'counter:{counter}')
    # update sprite group

    for loop_animal in all_animals_group:
        all_animals_group.remove(loop_animal)
        loop_animal.check_collision(all_animals_group)

        loop_animal.set_vision(all_animals_group)
        all_animals_group.add(loop_animal)

    cows_group.update()

    # draw sprite group
    cows_group.draw(screen)

    # cow.move_random()

    # pygame.draw.circle(screen, constants.WHITE, (cow.location.get()), 10)

    # cows = list(map(lambda animal: animal.map_move_random(debug=True) , cows))

    # map(lambda cow: cow.move(), cows )

    if (counter > 5000):
        active = False

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    # --- Limit to 60 frames per second
    # clock.tick(60)

# Close the window and quit.
pygame.quit()
