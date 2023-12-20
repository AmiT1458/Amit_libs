import mouse
import time
import math

start_pos = (964, 305)
# start_pos = (964, 225)
direction = 0
speed = 0.02
current_pos = mouse.get_position()
start_time = time.time()
go_to_x = start_pos[0]
go_to_y = start_pos[1]

time.sleep(3)


def run_circle(direction, go_to_x, go_to_y):
    mouse.move(start_pos[0], start_pos[1])

    mouse.press(button='left')

    while True:
        current_pos = mouse.get_position()
        direction += 0.005
        current_time = time.time()

        go_to_x -= math.cos(math.radians(direction)) * speed
        go_to_y += math.sin(math.radians(direction)) * speed

        mouse.move(go_to_x, go_to_y)

        if direction >= 366:
            break

        if (current_time - start_time) >= 15:
            print("time's out")
            break


run_circle(direction, go_to_x, go_to_y)