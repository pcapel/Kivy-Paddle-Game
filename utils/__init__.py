from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.vector import Vector


class MyKeyboardListener(Widget):

    def __init__(self, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self._callback_dict = dict()

    def register(self, func, name, *args, **kwargs):
        """
        register a callback function for a keypress name
        :param func: callback
        :param name: keypress event text name
        :param args: the args to provide the callback
        :return:
        """
        self._callback_dict[name] = {'callback': func, 'args': args, 'kwargs': kwargs}
        return None

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        holder = self._callback_dict[keycode[1]]
        holder['callback'](*holder['args'], **holder['kwargs'])
        return True


def build_board(dim):
    x_start, y_start = dim
    x = 50
    y = 350
    for i in range(x_start):
        for j in range(y_start):
            yield x, y
            y = y + 21
        x = x + 51
        y = 350


def between(val, x1, x2):
    return val >= x1 and val <= x2


def rectangle_bounce(rect, ball):
    """
    Generalized bounce algorithm for a rectangle.  Doesn't seem to work very well.

    :param rect: the rectangle to collision check
    :param ball: the ball to collision check
    :return: Noramlized vector multiplied by ball.speed
    """
    top = rect.get_top()
    bottom = top - rect.height
    left = rect.get_right() - rect.width
    right = rect.get_right()

    vx, vy = ball.velocity

    if between(ball.center_x, left, right):
        return Vector(vx, -1 * vy).normalize() * ball.speed
    elif between(ball.center_y, bottom, top):
        return Vector(vx * -1, vy).normalize() * ball.speed
    else:
        return Vector(vx * -1, vy * -1).normalize() * ball.speed


def circle_bounce(circle, ball):
    """
    generalized bouncing of the ball from circles
    :param circle: circle to collide with
    :param ball: ball to collide with
    :return: a normalized Vector times ball speed
    """
    pass