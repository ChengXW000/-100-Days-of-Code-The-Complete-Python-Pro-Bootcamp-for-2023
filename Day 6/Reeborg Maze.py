def turn_right():
    turn_left()
    turn_left()
    turn_left()

def over_the_corner():
    turn_right()
    move()
    turn_right()

def jump():
    turn_left()
    while wall_on_right():
        move()
    over_the_corner()
    while front_is_clear():
        move()
    turn_left()

while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
