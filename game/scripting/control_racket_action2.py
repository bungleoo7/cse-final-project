from constants import *
from game.scripting.action import Action


class ControlRacketAction2(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP_2)

        if self._keyboard_service.is_key_down(LEFT_PLAYER_TWO): 
            racket.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT_PLAYER_TWO): 
            racket.swing_right()  
        else: 
            racket.stop_moving()