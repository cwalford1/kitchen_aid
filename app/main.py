from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen

COLUMN_DATA = [
    ("Item Name", dp(30)),
    ("In Stock?", dp(30)),
    ("Recipes In", dp(30)),
    ("Importance", dp(20)),
]
ROW_DATA = [
    (
        "salt",
        ("checkbox-marked-circle", [39 / 256, 174 / 256, 96 / 256, 1], "Yes"),
        100,
        4,
    ),
    ("mushrooms", ("alert-circle", [1, 0, 0, 1], "No"), 10, 3),
    (
        "Coffee",
        ("alert", [255 / 256, 165 / 256, 0, 1], "Running Low"),
        2,
        5,
    ),
]

""


class MainApp(MDApp):
    def build(self):
        layout = AnchorLayout(anchor_x="right", anchor_y="bottom")
        screen = MDScreen()
        self.data_table = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=COLUMN_DATA,
            row_data=ROW_DATA,
            sorted_on="item name",
            sorted_order="ASC",
            elevation=2,
        )
        layout.add_widget(self.data_table)
        # screen.add_widget(self.data_table)
        return layout


if __name__ == "__main__":
    MainApp().run()
