from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from base_win import BaseWin
from instr import *

class FinalWin(BaseWin):

    def __init__(self, transfer_results):
        self.results = transfer_results
        super().__init__()

    def initUI(self):

        self.end_label = QLabel('Конец')
        self.workheart_label = QLabel(txt_workheart+self.get_result())
        self.index_label = QLabel(txt_index+' '+str(self.index))

        self.v_line = QVBoxLayout()
        self.setLayout(self.v_line)

        self.v_line.addWidget(self.end_label, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.index_label, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.workheart_label, alignment=Qt.AlignCenter)

    def get_result(self):

        self.index = (4*(self.results.p1+self.results.p2+self.results.p3)-200)/10

        if self.results.age <= 8:
            if self.index <= 6.4:
                return txt_res5
            elif self.index <= 11.9:
                return txt_res4
            elif self.index <= 16.9:
                return txt_res3
            elif self.index <= 20.9:
                return txt_res2
            else:
                return txt_res1
        if self.results.age <= 10:
            if self.index <= 4.9:
                return txt_res5
            elif self.index <= 10.4:
                return txt_res4
            elif self.index <= 15.4:
                return txt_res3
            elif self.index <= 19.5:
                return txt_res2
            else:
                return txt_res1
        if self.results.age <= 12:
            if self.index <= 3.4:
                return txt_res5
            elif self.index <= 8.9:
                return txt_res4
            elif self.index <= 13.9:
                return txt_res3
            elif self.index <= 18:
                return txt_res2
            else:
                return txt_res1
        if self.results.age <= 14:
            if self.index <= 1.9:
                return txt_res5
            elif self.index <= 7.4:
                return txt_res4
            elif self.index <= 12.4:
                return txt_res3
            elif self.index <= 16.4:
                return txt_res2
            else:
                return txt_res1
        else:
            if self.index <= 0.4:
                return txt_res5
            elif self.index <= 5.9:
                return txt_res4
            elif self.index <= 10.9:
                return txt_res3
            elif self.index <= 14.9:
                return txt_res2
            else:
                return txt_res1