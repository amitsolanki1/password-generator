from gen import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
import sys
import random
from datetime import datetime
from os import startfile,path
class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generatePassword)
        self.ui.pushButton_2.clicked.connect(self.show_password)

    def generatePassword(self): 
        message = QMessageBox()
        message.setText("The password was written to password.txt, show this again?")
        message.setWindowTitle("password")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        message.buttonClicked.connect(self.YesNo)
        x = message.exec_()

    def show_password(self):
        with open("password.txt","rt")as f:
            data=f.read()
            # print(data)
        startfile(path.join('',"password.txt"))
    def YesNo(self, button):
        if button.text() == "&Yes":
            alphabats= 'abcdefghijklmnopqrstuvwxyz'
            alphabats+=alphabats.upper()
            number=str('1234567890')
            special_number='@#$_&'
            length=int(self.ui.label.text())
            print(length)
            combination=alphabats+number+special_number
            pwd="".join(random.sample(combination,length))
            print(pwd)
            with open('password.txt','a') as f:
                f.write('\n'+pwd +'   : length :  ' +str(length) +'  : date : '+ str(datetime.now()))

        elif button.text() == "&No":
            with open("showMessage", "w") as f:
                f.write("0")

app = QApplication(sys.argv)
wc = window()
wc.show()
sys.exit(app.exec_())
