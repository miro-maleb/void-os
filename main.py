from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.core.window import Window

Window.size = (1080, 1920)


class VoidApp(App):
    def build(self):
        root = Widget()
        with root.canvas.before:
            Color(0.1, 0.09, 0.07)
            Ellipse(pos=root.pos, size=root.size)
        return root


if __name__ == '__main__':
    VoidApp().run()
