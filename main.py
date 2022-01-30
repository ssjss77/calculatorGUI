import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button:
    def __init__(self, text, results):
        self.pushbut = QPushButton(str(text))
        self.text = text
        self.results = results
        self.pushbut.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):

        if v == '=':
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v== 'AC':
            self.results.setText("")
        elif v == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif v == "%":
            value = float(self.results.text())
            self.results.setText(str(value / 100))
        elif v == "DEL":
            curr_value = str(self.results.text())
            self.results.setText(curr_value[:-1])
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)
        print("clicked, ", v)

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Calculator")
        self.CreateApp()


    def CreateApp(self):

        # Create our grid:
        grid = QGridLayout()
        result = QLineEdit()
        grid.addWidget(result, 0, 0, 1, 4)

        buttons = ["AC", "√", "%", "/",
                    7, 8, 9, "*",
                    4, 5, 6, "+",
                    1, 2, 3, "-",
                    0, ".", "=", "DEL"]
        row = 1
        col = 0
        for button in buttons:
            if col > 3:
                row += 1
                col = 0
            buttonObject = Button(button, result)
            if button == 0:
                grid.addWidget( buttonObject.pushbut, row, col, 1, 2 )
                col += 1
            elif button == "DEL":
                grid.addWidget(buttonObject.pushbut, 6, 0, 1, 4 )
            else :
                grid.addWidget(buttonObject.pushbut, row, col, 1, 1 )
            col += 1



        self.setLayout( grid )
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())