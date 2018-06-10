from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.vector import Vector

from utils import rectangle_bounce


class Paddle(Widget):
    score = NumericProperty(0)
    lives = NumericProperty(3)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            # create an offset to have the ball angle more controllable
            offset = (ball.center_x - self.center_x) / (self.width / 10)
            bounced = rectangle_bounce(self, ball)
            ball.velocity = bounced.x + offset, bounced.y

    def serve_ball(self, ball, speed=7):
        if not ball.served:
            ball.center = self.center_x, self.center_y + 20
            ball.speed = speed
            at = Vector(0, speed)
            ball.velocity = at.x, at.y
            ball.served = True

    def reset_ball(self, ball):
        ball.center = self.center_x, self.center_y + 25
        ball.velocity = 0, 0
        ball.served = False
        ball.pos = ball.center
