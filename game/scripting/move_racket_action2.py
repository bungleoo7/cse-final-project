from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction2(Action):

    def __init__(self):
        pass
#need to change positions 
#create a new player
#add score for the game 

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP_2)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()

        x = position.get_x()
        position = position.add(velocity)
        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - RACKET_WIDTH):
            position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
        
        body.set_position(position)