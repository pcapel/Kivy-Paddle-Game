from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from utils import MyKeyboardListener, build_board
from components.game.ball import Ball
from components.game.paddle import Paddle
from components.game.blocks import BasicBlock
from kivy.uix.screenmanager import Screen


class PongGame(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)
    screen = ObjectProperty(None)
    keyboard_manager = MyKeyboardListener()

    def init_game(self):
        self.board = [BasicBlock(pos=pos) for pos in build_board((12, 5))]
        for block in self.board:
            self.add_widget(block)
        self.keyboard_manager.register(self.paddle_move, 'left', -10)
        self.keyboard_manager.register(self.paddle_move, 'right', 10)
        self.keyboard_manager.register(self.player.serve_ball, 'spacebar', self.ball, speed=7)
        self.game_runner = Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        if self.ball.served:
            self.ball.move()
        self.player.bounce_ball(self.ball)
        self.board_bounce()
        self.check_death()

    def board_bounce(self):
        for block in self.board:
            block.bounce_ball(self.ball)
            if block.is_destroyed:
                self.player.score += block.score
                self.remove_widget(block)
                del self.board[self.board.index(block)]

    def on_touch_move(self, touch):
        if touch.x < self.width:
            self.player.center_x = touch.x
            if not self.ball.served:
                self.ball.center_x = touch.x

    def paddle_move(self, direction):
        self.player.center_x += direction

    def check_death(self):
        if self.player.lives == 0:
            self.screen.clear_widgets()
            self.screen.add_widget(Label(text='You died.'))


class GameScreen(Screen):
    game = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
