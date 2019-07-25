# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import Ui_OtherWindow
from OtherWindow2 import Ui_OtherWindow2
import sqlite3
import sys, traceback

#ind=0

class Ui_MainWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def openWindow2(self,ind):
        
        self.window = QtWidgets.QMainWindow()
        print('here')
        self.ui = Ui_OtherWindow2()
        
        self.ui.setupUi(self.window, ind)
    
        self.window.show()

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 10, 400, 21))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setObjectName("title")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(200, 50, 111, 101))
        self.logoLabel.setAutoFillBackground(False)
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 180, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        fileName = 'C:/Users/Aditya/Desktop/MovieDB/logo.jpg'
        pixmap = QtGui.QPixmap(fileName)
        pixmap = pixmap.scaled(self.logoLabel.width(), self.logoLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton.clicked.connect(self.search)

        MainWindow.setWindowIcon(QtGui.QIcon('wb.png'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warner Bros Movie DataBase"))
        self.title.setText(_translate("MainWindow", "Warner Bros Movie DataBase"))
        self.pushButton.setText(_translate("MainWindow", "GO!"))
        

    def search(self):
        print(self.lineEdit.text())
        text = self.lineEdit.text()
        if text:
            text = text.strip()
            text = text.upper()
            print(text)
            conn = sqlite3.connect('temp2.db')
            c = conn.cursor()
            c.execute("""Select * from MOVIE""")
            res = c.fetchall()
            movie_names = []
            print(res)
            for i in range(len(res)):
                movie_names.append(res[i][2])
            print(movie_names)
            key_words = text.split()
            max_movie = movie_names[0]
            maxx=0
            for movie in movie_names:
                count=0
                for key_word in key_words:
                    movie_words = movie.split()
                    for movie_word in movie_words:
                        if movie_word==key_word:
                            count+=1
                if count>maxx:
                    maxx=count
                    max_movie=movie
            print(maxx)
            print(max_movie)
            if maxx==0:
                #notfound
                print('Not Found')
                self.openWindow()
            else:
                for i in range(len(res)):
                    if max_movie==res[i][2]:
                        ind=i
                        break
                print(ind)
                self.openWindow2(ind)
               
                #print_movie_info(argument is ind) '''
        else:
            self.openWindow()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

