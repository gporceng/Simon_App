from kivy.app import App
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class design(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "50"
        self.title = ("Simple 5 Start Menu Design - By Gregory Porceng")
    pass



if __name__ == '__main__':
    design().run()