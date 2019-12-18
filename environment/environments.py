from environment.constants import ROTATE_LEFT, RIGHT, LEFT, ROTATE_RIGHT, FIRE, BREAK, DOWN, UP


class Enviroment:

    def __init__(self):

        self.action_space = self.create_action_space()

    def create_action_space(self):

        action_space = [LEFT, RIGHT, UP, DOWN, ROTATE_LEFT, ROTATE_RIGHT, FIRE, BREAK]

        return action_space

