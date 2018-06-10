from random import random, randint
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ReferenceListProperty
from components.game import PongGame
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


BASE_X = 10
BASE_Y = 16


class Menu(Widget):
    StartBtn = ObjectProperty(None)
    b1 = ObjectProperty()
    b2 = ObjectProperty()
    b3 = ObjectProperty()
    b4 = ObjectProperty()
    b5 = ObjectProperty()
    b6 = ObjectProperty()
    b7 = ObjectProperty()
    b8 = ObjectProperty()
    b9 = ObjectProperty()
    b10 = ObjectProperty()
    balls = ReferenceListProperty(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10)

    def start_balls(self):
        for ball in self.balls:
            ball.velocity = random() * randint(BASE_X, BASE_Y), random() * randint(BASE_X, BASE_Y)
        self.balls_event = Clock.schedule_interval(self.background_ball, 1.0 / 60.0)

    def background_ball(self, *args, **kwargs):
        for ball in self.balls:
            ball.move()

    def cancel_balls(self):
        print('cancel balls')
        self.balls_event.cancel()


class MenuScreen(Screen):
    menu = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu.start_balls()

    def start_game(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        self.root.start_game(game)