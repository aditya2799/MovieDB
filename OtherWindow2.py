# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
#ind=1

class Ui_OtherWindow2(object):
    def setupUi(self, MainWindow, ind):

        conn = sqlite3.connect('temp2.db')
        c = conn.cursor()
        c.execute("""Select * from MOVIE""")
        res = c.fetchall()
        movie = res[ind]
        aid = res[ind][5]
        actorname = ""
        c.execute(""" SELECT FIRST_NAME,LAST_NAME,AGE FROM ACTOR WHERE AID=(?);""", (aid,))
        temp = c.fetchall()
        actorname += temp[0][0]
        actorname += " "
        actorname += temp[0][1]
        actorage = temp[0][2]

        did = res[ind][4]
        directorname = ""
        c.execute(""" SELECT FIRST_NAME,LAST_NAME,AGE FROM DIRECTOR WHERE DID=(?);""", (did,))
        temp = c.fetchall()
        directorname += temp[0][0]
        directorname += " "
        directorname += temp[0][1]
        directorage = temp[0][2]

        mid = res[ind][0]

        c.execute(""" SELECT GENRE FROM GENRE WHERE MID=(?);""", (mid,))
        temp = c.fetchall()
        genrefull = temp[0][0]
        for i in range(1, len(temp)):
            genrefull+=", "
            genrefull+=temp[i][0]

            


        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.movie_name = QtWidgets.QLabel(self.centralwidget)
        self.movie_name.setGeometry(QtCore.QRect(10, 10, 541, 51))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(50)
        self.movie_name.setFont(font)
        font.setBold(True)
        self.movie_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.movie_name.setObjectName("movie_name")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(230, 80, 311, 231))
        self.image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image.setObjectName("image")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 51, 21))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.actor_name = QtWidgets.QLabel(self.centralwidget)
        self.actor_name.setGeometry(QtCore.QRect(10, 140, 201, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        self.actor_name.setFont(font)
        self.actor_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.actor_name.setText(actorname)
        self.actor_name.setObjectName("actor_name")
        self.actor_age = QtWidgets.QLabel(self.centralwidget)
        self.actor_age.setGeometry(QtCore.QRect(10, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        self.actor_age.setFont(font)
        self.actor_age.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.actor_age.setText(str(actorage))
        self.actor_age.setObjectName("actor_age")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 71, 21))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.director_name = QtWidgets.QLabel(self.centralwidget)
        self.director_name.setGeometry(QtCore.QRect(10, 250, 201, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        self.director_name.setFont(font)
        self.director_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.director_name.setText(directorname)
        self.director_name.setObjectName("director_name")
        self.director_age = QtWidgets.QLabel(self.centralwidget)
        self.director_age.setGeometry(QtCore.QRect(10, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        self.director_age.setFont(font)
        self.director_age.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.director_age.setText(str(directorage))
        self.director_age.setObjectName("director_age")
        self.rating = QtWidgets.QLabel(self.centralwidget)
        self.rating.setGeometry(QtCore.QRect(360, 320, 171, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        font.setBold(True)
        self.rating.setFont(font)
        self.rating.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rating.setText(str(res[ind][6])+" /10")
        self.rating.setObjectName("rating")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(30, 370, 471, 181))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        font.setBold(True)
        self.description.setFont(font)
        self.description.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.description.setText(res[ind][3])
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.genre = QtWidgets.QLabel(self.centralwidget)
        self.genre.setGeometry(QtCore.QRect(10, 330, 251, 31))
        self.genre.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.genre.setText(genrefull)
        self.genre.setObjectName("genre")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.yor = QtWidgets.QLabel(self.centralwidget)
        self.yor.setGeometry(QtCore.QRect(100, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        self.yor.setFont(font)
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(12)
        font.setBold(True)
        self.genre.setFont(font)
        self.yor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.yor.setText(str(res[ind][1]))
        self.yor.setObjectName("yor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, ind)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        image_name = res[ind][2].split(' ',1)[0].lower()
        
        fileName = 'C:/Users/Aditya/Desktop/MovieDB/{}.jpg'.format(image_name)
        pixmap = QtGui.QPixmap(fileName)
        pixmap = pixmap.scaled(self.image.width(), self.image.height(), QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(pixmap)
        self.image.setAlignment(QtCore.Qt.AlignCenter)


        MainWindow.setWindowIcon(QtGui.QIcon('wb.png'))
        

    def retranslateUi(self, MainWindow, ind):



        conn = sqlite3.connect('temp2.db')
        c = conn.cursor()
        c.execute("""Select * from MOVIE""")
        res = c.fetchall()



        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warner Bros Movie DataBase"))
        self.movie_name.setText(_translate("MainWindow", res[ind][2]))
        self.image.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Actor : "))
        self.label_4.setText(_translate("MainWindow", "Director : "))
        self.label_5.setText(_translate("MainWindow", "Year : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow2()
    ui.setupUi(MainWindow, 0)
    MainWindow.show()
    sys.exit(app.exec_())

