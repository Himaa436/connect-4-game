import sys
from PyQt6.QtWidgets import QApplication, QWidget
from main import Game
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Initialize the game logic
        self.game = Game()

        # Connect the UI buttons to the game logic
        self.setup_ui_connections()

    def setup_ui_connections(self):
        # Connect each button's click signal to the corresponding method
        for col in range(7):  # Columns A-G
            for row in range(6):  # Rows 1-6
                self.ui.buttons[(row, col)].clicked.connect(lambda checked, col=col: self.make_move(col))

    def make_move(self, col):
        # Make the move using the backend logic and get the position
        result = self.game.make_move(col)
        self.setWindowTitle(f"` \t \t \t \t \t Y Score is {self.game.check('Y')} \t and \t R Score is {self.game.check('R')} \n")
        if result:
            row, col = result
            # Get the token and update the button appearance
            token = self.game.get_token(row, col)

            # Update the UI button with the token image
            if token == "Y":
                self.ui.buttons[(row, col)].setStyleSheet("background-color: yellow;")
            elif token == "R":
                self.ui.buttons[(row, col)].setStyleSheet("background-color: red;")
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
