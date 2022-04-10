from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from file import *


app = QApplication([])

start_win = FirstWin()








test_win = QWidget()
test_vertical = QVBoxLayout()


age_input = QLineEdit()
fio_input = QLineEdit()

test_vertical.addWidget(QLabel('ФИО'))
test_vertical.addWidget(fio_input)
test_vertical.addWidget(QLabel('Возраст'))
test_vertical.addWidget(age_input)


test_win.setLayout(test_vertical)


def show_test():
    start_win.hide()
    test_win.show()

app.exec()