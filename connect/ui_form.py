from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(700, 600)

        # Create a grid layout for the game board
        self.gridLayout = QGridLayout(Widget)

        # Create buttons to represent each slot in the grid
        self.buttons = {}
        for row in range(6):
            for col in range(7):
                button = QPushButton()
                button.setFixedSize(100, 100)  # Set the button size
                self.gridLayout.addWidget(button, row, col)
                button.clicked.connect(self.make_move)
                self.buttons[(row, col)] = button

    def make_move(self):
        # This will be overridden in the main app to pass the column to backend
        pass
    def Row_check(self):

        pass

    def col_check(self,x , color):
        pass


    def all_row(self,color):
        pass

    def valid(self,x , y):
        pass

    def diagonal_check(self,x, y, color):
        pass

    def x_diagonal_check(self,x, y, color):
        pass

    def all_x(self,color):
        pass


    def all_col(self,color):
        pass

    def check(self,color):
        pass

