from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

from utils import rectangle_bounce


class BasicBlock(Widget):

    DURA_MAX = 10
    durability = NumericProperty(None)

    def __init__(self, *args, **kwargs):
        self.pos = kwargs.pop('pos', (50, 50))
        self.durability = kwargs.pop('durability', 5)
        self.worth = self.durability
        super().__init__(*args, **kwargs)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            self.durability -= 1
            ball.velocity = rectangle_bounce(self, ball)

    @property
    def is_destroyed(self):
        return self.durability <= 0

    @property
    def score(self):
        return self.worth
