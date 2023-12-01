from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from base_win import BaseWin
from instr import *
from main_test import MainTest

class HelloWin(BaseWin):

    def initUI(self):

        self.v_line = QVBoxLayout()
        self.hello_label = QLabel(txt_hello)
        self.instruction_label = QLabel(txt_instruction)
        self.next_btn = QPushButton(txt_next)

        self.setLayout(self.v_line)

        self.v_line.addWidget(self.hello_label, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.instruction_label, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.next_btn, alignment=Qt.AlignCenter)

    def next_win(self):

        self.hide()
        self.mw = MainTest()

    def connects(self):
        
        self.next_btn.clicked.connect(self.next_win)

def run():

    app = QApplication([])
    mw = HelloWin()
    app.exec_()
        
run()