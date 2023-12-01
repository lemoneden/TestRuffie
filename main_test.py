from PyQt5.QtWidgets        import (QWidget, QLabel, QApplication, QPushButton, QVBoxLayout,
                                    QHBoxLayout, QLineEdit, QSlider, QLCDNumber)
from PyQt5.QtCore           import QTimer, QTime, Qt
from base_win               import BaseWin
from final_win              import FinalWin
from transfer_results       import TransferResults
from instr                  import *
from my_timer               import Timer

class MainTest(BaseWin):
    
    def initUI(self):

        self.name_label = QLabel(txt_name)
        self.age_label = QLabel(txt_age)
        self.test1_label = QLabel(txt_test1)
        self.test2_label = QLabel(txt_test2)
        self.test3_label = QLabel(txt_test3)

        self.lcd_age = QLCDNumber()
        self.lcd_age.display(0)

        self.slider_age = QSlider(Qt.Horizontal)
        self.slider_age.setMinimum(7)
        self.slider_age.setMaximum(100)

        self.input_name = QLineEdit(txt_hintname)
        self.input_pulse1 = QLineEdit(txt_hinttest)
        self.input_pulse2 = QLineEdit(txt_hinttest)
        self.input_pulse3 = QLineEdit(txt_hinttest)

        self.sendresults = QPushButton(txt_sendresults)
        self.btn_open_timer = QPushButton(txt_open_timer)

        self.h_line = QHBoxLayout()
        self.v_line_1 = QVBoxLayout()
        self.v_line_2 = QVBoxLayout()

        self.h_line.addLayout(self.v_line_1)
        self.h_line.addLayout(self.v_line_2)
        self.setLayout(self.h_line)

        self.v_line_1.addWidget(self.name_label, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.input_name, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.age_label, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.lcd_age, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.slider_age, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.test1_label, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.input_pulse1, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.test2_label, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.test3_label, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.input_pulse2, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.input_pulse3, alignment=Qt.AlignCenter)
        self.v_line_1.addWidget(self.sendresults, alignment=Qt.AlignCenter)
        
        self.v_line_2.addWidget(self.btn_open_timer, alignment=Qt.AlignCenter)

    def start_timer(self):
        
        pass

    def next_win(self):

        self.transfer_results = TransferResults(int(self.input_pulse1.text()), int(self.input_pulse2.text()),
                                                int(self.input_pulse3.text()), int(self.lcd_age.value()))

        self.hide()
        self.fw = FinalWin(self.transfer_results)

    def open_timer(self):

        self.mt = Timer()      
        
    def connects(self):

        self.slider_age.valueChanged.connect(self.lcd_age.display)
        self.btn_open_timer.clicked.connect(self.open_timer)
        self.sendresults.clicked.connect(self.next_win)