
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import difflib
import random

sessionwpm = []
sessionaccuracy = []


class Ui_MainWindow(object):
    def __init__(self):
        self.resettimer = False
               
    def handle_enter(self):
        if self.resettimer == True:
            self.timer.stop()
            self.accuracy()
            self.wpm()
            self.prompts()
            self.clearinput()
            
            self.resettimer = False

    def clearinput(self):
        self.lineEdit.setText("")

    def accuracy(self):
        accuracy = 0
        sentence = self.sentence
        sentence = sentence.strip()
        response = self.lineEdit.text()
        
        if response == sentence:
        
            accuracy = 100
            self.currentaccuracy.setText("100%")
        
        else:
            accuracy=difflib.SequenceMatcher(None,sentence,response).ratio()
            accuracy=round(accuracy*100,2)
            self.currentaccuracy.setText(str(accuracy) + "%")

        sessionaccuracy.append(accuracy)
        self.sessionaccavg = (sum(sessionaccuracy) / len(sessionaccuracy))
        self.averageaccuracy.setText(str(round(self.sessionaccavg)))

    def wpm(self):
        wpm = ((len(self.sentence) / 5) * (60 /self.timecount))
        wpm = round(wpm)
        self.currentwpm.setText(str(wpm) + " WPM")
        sessionwpm.append(wpm)
        self.sessionavg = (sum(sessionwpm) / len(sessionwpm))
        self.averagewpm.setText(str(round(self.sessionavg)))
        
    def prompts(self):
        self.f = open("sentences.txt")
        self.lines = self.f.readlines()
        self.sentence = random.choice(self.lines)
        self.prompt.setText(self.sentence)
        self.f.close()

    def linktimer(self):
        if self.resettimer == False:
            self.resettimer = True
            
            self.timecount = 0
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.run_time)
            self.timer.setInterval(1000)
            self.timer.start()
        
    def run_time(self):
        self.timecount += 1
    
    def reset_average(self):
        self.averageaccuracy.setText("")
        self.currentaccuracy.setText("")
        self.averagewpm.setText("")
        self.currentwpm.setText("")
        self.prompts()
  
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titlebar = QtWidgets.QLabel(self.centralwidget)
        self.titlebar.setGeometry(QtCore.QRect(230, 0, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.titlebar.setFont(font)
        self.titlebar.setObjectName("titlebar")
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(40, 70, 711, 131))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.prompt.setFont(font)
        self.prompt.setFrameShape(QtWidgets.QFrame.Box)
        self.prompt.setText("")
        self.prompt.setWordWrap(True)
        self.prompt.setObjectName("prompt")
        self.resetbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset_average())
        self.resetbutton.setGeometry(QtCore.QRect(620, 309, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.resetbutton.setFont(font)
        self.resetbutton.setObjectName("resetbutton")
        self.currentaccuracy = QtWidgets.QLabel(self.centralwidget)
        self.currentaccuracy.setGeometry(QtCore.QRect(400, 369, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.currentaccuracy.setFont(font)
        self.currentaccuracy.setFrameShape(QtWidgets.QFrame.Box)
        self.currentaccuracy.setText("")
        self.currentaccuracy.setObjectName("currentaccuracy")
        self.averagewpm = QtWidgets.QLabel(self.centralwidget)
        self.averagewpm.setGeometry(QtCore.QRect(400, 419, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.averagewpm.setFont(font)
        self.averagewpm.setFrameShape(QtWidgets.QFrame.Box)
        self.averagewpm.setText("")
        self.averagewpm.setObjectName("averagewpm")
        self.averageaccuracy = QtWidgets.QLabel(self.centralwidget)
        self.averageaccuracy.setGeometry(QtCore.QRect(400, 469, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.averageaccuracy.setFont(font)
        self.averageaccuracy.setFrameShape(QtWidgets.QFrame.Box)
        self.averageaccuracy.setText("")
        self.averageaccuracy.setObjectName("averageaccuracy")
        self.currentwpm = QtWidgets.QLabel(self.centralwidget)
        self.currentwpm.setGeometry(QtCore.QRect(400, 319, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.currentwpm.setFont(font)
        self.currentwpm.setFrameShape(QtWidgets.QFrame.Box)
        self.currentwpm.setText("")
        self.currentwpm.setObjectName("currentwpm")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(280, 319, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(250, 369, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(280, 419, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(250, 469, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label4.setFont(font)
        self.label4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(42, 230, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.handle_enter)            
        self.lineEdit.textChanged.connect(self.linktimer)
        self.prompts()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing Speed Game"))
        self.titlebar.setText(_translate("MainWindow", "Typing Speed Game"))
        self.resetbutton.setText(_translate("MainWindow", "RESET"))   
        self.label1.setText(_translate("MainWindow", "Current WPM"))
        self.label2.setText(_translate("MainWindow", "Current Accuracy"))
        self.label3.setText(_translate("MainWindow", "Average WPM"))
        self.label4.setText(_translate("MainWindow", "Average Accuracy"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Start Typing To Begin!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
