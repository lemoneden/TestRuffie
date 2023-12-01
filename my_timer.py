from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QApplication,
                            QLCDNumber, QVBoxLayout,
                             QHBoxLayout, QPushButton, QButtonGroup)
from base_win import BaseWin
from instr import *

class Timer(BaseWin):

    def set_appear(self):
    
        self.setWindowTitle(title_timer)
        self.resize(win_width//5, win_height//4)
        self.move(win_x, win_y)

    def initUI(self):

        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet("color: rgb(0,0,0);")
        self.lcd.display(0)

        self.btn_start = QPushButton(txt_starttimer)
        self.btn_start.setStyleSheet('background: rgb(153,255,153);')
        self.btn_stop = QPushButton(txt_stoptimer)
        self.btn_stop.setStyleSheet('background: rgb(255,153,153);')
        self.btn_15 = QPushButton(timer_15)
        self.btn_45 = QPushButton(timer_45)
        self.btn_60 = QPushButton(timer_60)
        # self.btn_group = QButtonGroup()
        # self.btn_group.addButton(self.btn_15, id=1)
        # self.btn_group.addButton(self.btn_45, id=2)
        # self.btn_group.addButton(self.btn_60, id=3)

        self.h_line = QHBoxLayout()
        self.h_line2 = QHBoxLayout()
        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.lcd)

        self.v_line.addLayout(self.h_line)
        self.v_line.addLayout(self.h_line2)
        self.setLayout(self.v_line)

        self.h_line.addWidget(self.btn_15, alignment=Qt.AlignCenter)
        self.h_line.addWidget(self.btn_45, alignment=Qt.AlignCenter)
        self.h_line.addWidget(self.btn_60, alignment=Qt.AlignCenter)
        self.h_line2.addWidget(self.btn_start, alignment=Qt.AlignCenter)
        self.h_line2.addWidget(self.btn_stop, alignment=Qt.AlignCenter)

    def option_time(self):

        btn = self.sender()
        txt_btn = btn.text()
        self.time = int(txt_btn)
        self.lcd.display(self.time)

    def show_time(self):
        
        self.lcd.display(self.time)
        self.time -= 1                                            # !!!
        if self.time < 0:
            self.timer.stop()
            self.time = 0

    def start_timer(self):

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

    def stop_timer(self):

        self.timer.stop()

    def connects(self):

        self.btn_15.clicked.connect(self.option_time)
        self.btn_45.clicked.connect(self.option_time)
        self.btn_60.clicked.connect(self.option_time)
        # self.btn_group.buttonClicked.connect(self.option_time)

        self.btn_start.clicked.connect(self.start_timer)
        self.btn_stop.clicked.connect(self.stop_timer)

def run():
    app = QApplication([])
    timer = Timer()
    app.exec_()