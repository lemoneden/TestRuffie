from PyQt5.QtWidgets import QWidget
from instr import *

class BaseWin(QWidget):
    
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        
        self.setWindowTitle(txt_title1)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):

        pass

    def connects(self):

        pass