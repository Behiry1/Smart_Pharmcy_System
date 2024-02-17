import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Login_SignUp_Ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
        self.ui.pushButton_3.clicked.connect(self.GoReg)
        self.ui.pushButton_2.clicked.connect(self.GoLog)

    def GoReg(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.RegisterPage)


    def GoLog(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
