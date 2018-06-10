from kivy.app import App
from components.menu import MenuScreen
from components.game import GameScreen
from kivy.uix.screenmanager import ScreenManager


class PongBlockApp(App):
    def build(self, app=None):
        manager = ScreenManager()
        manager.add_widget(MenuScreen(name='Menu'))
        manager.add_widget(GameScreen(name='Game'))
        manager.current = 'Menu'
        return manager


if __name__ == '__main__':
    PongBlockApp().run()