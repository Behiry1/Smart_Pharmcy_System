from PySide6.QtCore import QTimer


def show_registration_error(ui, message):
    ui.ErrorMessage.setText(message)
    ui.ErrorMessage.setStyleSheet("color: red;")
    QTimer.singleShot(5000, lambda: clear_errors(ui))
def show_registration_success(ui, message):
    ui.ErrorMessage.setText(message)
    ui.ErrorMessage.setStyleSheet("color: green;")
    QTimer.singleShot(5000, lambda: clear_errors(ui))
def show_login_error(ui, message):
    ui.ErrorMessage_2.setText(message)
    ui.ErrorMessage_2.setStyleSheet("color: red;")
    QTimer.singleShot(5000, lambda: clear_errors(ui))
def show_login_success(ui, message):
    ui.ErrorMessage_2.setText(message)
    ui.ErrorMessage_2.setStyleSheet("color: green;")
    QTimer.singleShot(5000,lambda: clear_errors(ui))
def clear_errors(ui):
    ui.ErrorMessage.setText("")
    ui.ErrorMessage_2.setText("")