from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDapp):
    def build(self):
        return MDLabel(text = "Hello, World", halign = "center")

if __name__=="__main__":
    MainApp().run()