from datetime import datetime
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.clock import Clock

Window.size=[600, 300]
class DigitalClock(MDApp):
    def update_time(self, *args):
        nowtime = datetime.now()
        pt = nowtime.strftime("%I:%M:%S, %p")
        self.timelabel.text = pt
        dt = nowtime.strftime("%B %d, %Y")
        self.datelabel.text=dt
    def build(self):
        sc = MDScreen()
        self.theme_cls.theme_style = "Dark"
        self.timelabel = MDLabel(
                font_style="H1",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 1, 1),
                md_bg_color=[0, 0, 0, 1],
                pos_hint={"center_x": .5, "center_y": .6}
            )
        sc.add_widget(self.timelabel)
        self.datelabel = MDLabel(
                font_style="H5",
                halign="center",
                theme_text_color="Custom",
                text_color=(0, 1, 0, 1),
                pos_hint={"center_x": .5, "center_y": .36}
            )
        sc.add_widget(self.datelabel)
        Clock.schedule_interval(self.update_time, 1)
        return sc
        
if __name__ == '__main__':
    DigitalClock().run()