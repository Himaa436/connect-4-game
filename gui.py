import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect 4")
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("hello")
        self.layout().addWidget(my_label)

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec()