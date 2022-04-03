from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

app = QApplication([])
test_win = QWidget()
start_win = QWidget()


start_vertical = QVBoxLayout()


start_title = QLabel('Sheesh!!!')
start_info = QLabel('ЧЕКНЕТ ВАШЕ ЗДОРОВЬЕ ЗА 45 СЕК')
start_button = QPushButton('ПОНЕСЛАСЬ')

start_vertical.addWidget(start_title)
start_vertical.addWidget(start_info)
start_vertical.addWidget(start_button)


start_win.setLayout(start_vertical)
start_win.show()

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

start_button.clicked.connect(show_test)
app.exec()