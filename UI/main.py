import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        t_btn = QPushButton('훈련하기', self)
        t_btn.setGeometry(75, 580, 350, 100)
        t_btn.setCheckable(True)
        t_btn.click()

        s_btn = QPushButton('시작하기', self)
        s_btn.setGeometry(464, 580, 350, 100)
        s_btn.setCheckable(True)
        s_btn.click()

        r_btn = QPushButton('기록보기', self)
        r_btn.setGeometry(853, 580, 350, 100)
        r_btn.setCheckable(True)
        r_btn.click()

        font2 = t_btn.font()
        font2.setPointSize(20)
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        t_btn.setFont(font2)

        font2 = s_btn.font()
        font2.setPointSize(20)
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        s_btn.setFont(font2)

        font2 = r_btn.font()
        font2.setPointSize(20)
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        r_btn.setFont(font2)

        record_pix = QPixmap('기록보기 아이콘.png')
        start_pix = QPixmap("시작아이콘.png")
        train_pix = QPixmap('훈련아이콘.png')
        logo_pix = QPixmap('ACoach_logo.png')

        t_lb = QLabel(self)
        t_lb.setPixmap(train_pix)
        t_lb.setGeometry(75, 225, 350, 350)

        s_lb = QLabel(self)
        s_lb.setPixmap(start_pix)
        s_lb.setGeometry(464, 225, 350, 350)

        r_lb = QLabel(self)
        r_lb.setPixmap(record_pix)
        r_lb.setGeometry(853, 225, 350, 350)

        l_lb = QLabel(self)
        l_lb.setPixmap(logo_pix)
        l_lb.setGeometry(405, 40, 470, 160)

        self.setWindowTitle('ACoach')
        self.setWindowIcon(QIcon('ACoach_icon.png'))
        self.setGeometry(300, 300, 1280, 760)
        self.show()




if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())