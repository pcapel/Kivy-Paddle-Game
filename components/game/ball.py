from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    left = NumericProperty(None)
    bottom = NumericProperty(None)
    right = NumericProperty(None)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    speed = 3
    served = False
    in_game = NumericProperty(0)

    def lock_to(self, pos):
        """
        locks this ball instance to an x, y positiion
        :param pos: x, y coordinates to lock to
        :return: None
        """
        self.pos = pos
        self.velocity = Vector(0,0)

    def wall_bounce(self):
        window = self.get_root_window()
        height, width = window.height, window.width
        vx, vy = self.velocity
        if self.get_right() >= width:
            self.velocity = vx * -1, vy
        elif self.top >= height:
            self.velocity = vx, vy * -1

        if self.left < 0:
            self.velocity = vx * -1, vy
        elif self.bottom < 0:
            if self.in_game:
                self.player.lives -= 1
                self.player.reset_ball(self)
            self.velocity = vx, vy * -1

    def move(self, *args, **kwargs):
        """
        moves the ball in the window, bouncing as required
        :param args:
        :param kwargs:
        :return:
        """
        self.right = self.get_right()
        self.wall_bounce()
        self.pos = Vector(*self.velocity) + self.pos