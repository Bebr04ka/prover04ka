from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

app = QApplication([])
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
app.exec()