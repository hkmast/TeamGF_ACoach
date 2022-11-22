from PyQt5 import QtCore, QtWidgets
import stackdesign

def nextpage():
    currentpage = ui.stackedWidget.currentIndex()
    ui.stackedWidget.setCurrentIndex(currentpage+1)


def prevpage():
    currentpage = ui.stackedWidget.currentIndex()
    ui.stackedWidget.setCurrentIndex(currentpage-1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = stackdesign.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.s_btn.clicked.connect(nextpage)
    ui.male.clicked.connect(prevpage)
    MainWindow.show()
    sys.exit(app.exec_())
