from kivy.app import App
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock

Builder.load_string("""
<MenuScreen>:
    Screen:
        Image:
            source: "bg.png"
            size: self.size
            pos: self.pos
            size: root.size
            allow_stretch: True
            keep_ratio: False

        Image:
            source: "logo.png"
            pos_hint: {'center_x':0.5, 'center_y':0.65}
            


        MDFillRoundFlatButton:
            text:"start"
            font_size: '32sp'
            pos_hint: {'center_x':0.5,'center_y':0.4}
            on_press: root.manager.current = 'game'
            size_hint: (.5,.1)

        
        MDFillRoundFlatButton:
            text:"options"
            font_size: '32sp'
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press: root.manager.current = 'settings'
            size_hint: (.5,.1)

<SettingsScreen>:
    Screen:
        Image:
            source: "bg.png"
            size: self.size
            pos: self.pos
            size: root.size
            allow_stretch: True
            keep_ratio: False

        MDLabel:
            text: "Time Between Flashes"
            font_size: '32sp'
            pos_hint: {'center_x':0.5,'center_y':0.6}
            halign: "center"
            font_style: 'H2'
            theme_text_color: "Custom"
            text_color: 1,1,1,1


        MDSlider:
            min: 1
            max: 10
            value: 2

        
        MDFillRoundFlatButton:
            text:"save"
            font_size: '32sp'
            pos_hint: {'center_x':0.5,'center_y':0.4}
            on_press: root.manager.current = 'menu'
            size_hint: (.5,.1)

        MDFillRoundFlatButton:
            text:"back"
            font_size: '32sp'
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press: root.manager.current = 'menu'
            size_hint: (.5,.1)

<GameScreen>:
    Screen:
        Image:
            source: "bg.png"
            size: self.size
            pos: self.pos
            size: root.size
            allow_stretch: True
            keep_ratio: False

        MDLabel:
            text: "Game Started"
            font_size: '32sp'
            pos_hint: {'center_x':0.5,'center_y':0.9}
            halign: "center"
            font_style: 'H2'
            theme_text_color: "Custom"
            text_color: 1,1,1,1

            
""")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class GameScreen(Screen):
    pass


class design(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "50"
        self.title = ("Simon Game - By Gregory Porceng")

        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(GameScreen(name='game'))
        return sm



if __name__ == '__main__':
    design().run()