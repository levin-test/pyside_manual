import sys
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QTableWidget

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(1,3)
        self.columnLabels = ["One","Two","Three"]
        self.table.setHorizontalHeaderLabels(self.columnLabels)
        self.setCentralWidget(self.table)
        self.setGeometry(50,50,700,400)
        self.setWindowTitle("Show Table")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Example()
    ui.show()
    app.exec_()