from PySide2.QtWidgets import *


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    label = QLabel('Hello World!')
    label.show()

    app.exec_()
    sys.exit()
