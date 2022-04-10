from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from txt import *

class FirstWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Начало теста')
        self.initUI()
        self.show()

    def initUI(self):
        start_vertical = QVBoxLayout()
        start_title = QLabel(HELLOW_TXT)
        start_info = QLabel(FIRST)
        start_button = QPushButton('ПОНЕСЛАСЬ')

        start_vertical.addWidget(start_title)
        start_vertical.addWidget(start_info)
        start_vertical.addWidget(start_button)
        self.setLayout(start_vertical)

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Тестирование')
        self.initUI()
        self.show()
    def initUI(self):
        test_vertical = QVBoxLayout()

        age_input = QLineEdit()
        fio_input = QLineEdit()

        test_vertical.addWidget(QLabel('ФИО'))
        test_vertical.addWidget(fio_input)
        test_vertical.addWidget(QLabel('Возраст'))
        test_vertical.addWidget(age_input)

        test_vertical.addWidget(QLabel(HELP1))
        first_test_btn = QPushButton('первый тест')
        test_vertical.addWidget(first_test_btn)

        first_plus_input = QLineEdit('0')
        test_vertical.addWidget(first_plus_input)

        test_vertical.addWidget(QLabel(HELP2))

        squat_btn = QPushButton('начть приседания')
        test_vertical.addWidget(squat_btn)

        test_vertical.addWidget(QLabel())