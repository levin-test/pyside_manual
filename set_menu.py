import sys
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QTableWidget

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        open_act = QAction(self.style().standardIcon(QStyle.SP_DialogOpenButton), 'Open', self)
        open_act.triggered.connect(self.open)

        save_act = QAction(self.style().standardIcon(QStyle.SP_DialogSaveButton), 'Save', self)
        save_act.triggered.connect(self.save)

        menu_bar = self.menuBar()
        menu = menu_bar.addMenu('File')
        menu.addAction(open_act)
        menu.addAction(save_act)

    def open(self):
        print('Open')

    def save(self):
        print('Save')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    app.exec_()
