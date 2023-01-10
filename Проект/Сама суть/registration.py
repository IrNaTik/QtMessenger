# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import main_page
import requests
from hashing import main_idea


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.objects_to_del = []
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        font = QtGui.QFont()
        font.setFamily("Parchment")
        self.label.setFont(font)
        
        self.label.setStyleSheet("background-color: rgb(189, 210, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.login_field = QtWidgets.QLineEdit(self.centralwidget)
        self.login_field.setGeometry(QtCore.QRect(350, 210, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(14)
        font.setItalic(False)
        self.login_field.setFont(font)
        self.login_field.setStyleSheet("QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 18px;\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"")
        self.login_field.setText("")
        self.login_field.setObjectName("login_field")
        self.password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.password_field.setGeometry(QtCore.QRect(350, 360, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(14)
        self.password_field.setFont(font)
        self.password_field.setStyleSheet("QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-radius: 18px;\n"
"    padding-left: 10px\n"
"}\n"
"\n"
"")
        self.password_field.setText("")
        self.password_field.setObjectName("password_field")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 80, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(31)
        self.label_2.setFont(font)
        
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 160, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 312, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(20)
        self.label_4.setFont(font)
        
        self.label_4.setObjectName("label_4")
        self.to_registrate = QtWidgets.QPushButton(self.centralwidget)
        self.to_registrate.setGeometry(QtCore.QRect(400, 447, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.to_registrate.setFont(font)
        self.to_registrate.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.to_registrate.setStyleSheet("QPushButton {\n"
"    border-width: 4px;\n"
"    border-style: solid;\n"
"    border-radius: 18px;\n"
"    border-color: black;\n"
"    background-color: rgb(189, 210, 255);\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 19px;\n"
"    background-color: rgb(170, 183, 255);\n"
"}\n"
"")
        self.to_registrate.setObjectName("to_registrate")
        self.to_registrate.setCursor(QtCore.Qt.PointingHandCursor)
        self.get_back = QtWidgets.QPushButton(self.centralwidget)
        self.get_back.setGeometry(QtCore.QRect(0, 0, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.get_back.setFont(font)
        self.get_back.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.get_back.setStyleSheet("QPushButton {\n"
"    border-width: 4px;\n"
"    border-style: solid;\n"
"    border-radius: 18px;\n"
"    border-color: black;\n"
"    background-color: rgb(255, 79, 96);\n"
"    font-size: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 33px;\n"
"    background-color: rgb(170, 183, 255);\n"
"    \n"
"}\n"
"")
        self.get_back.setObjectName("get_back")
        self.get_back.setCursor(QtCore.Qt.PointingHandCursor)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.objects_to_del.extend((self.label, self.label_2, self.label_3, self.label_4, self.to_registrate, self.get_back))
        self.add_signals()

    def destroing(self):
        for obj in self.objects_to_del:
            obj.deleteLater()
        self.objects_to_del = []

    def main_page(self):
        self.destroing()
        ui = main_page.Ui_MainWindow()
        ui.setupUi(self.MainWindow)

    def show_info_messagebox(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
      
        # setting message for Message Box
        msg.setText(message)
          
        # setting Message box window title
        msg.setWindowTitle("Information MessageBox")
          
        # declaring buttons on Message Box
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
          
        # start the app
        retval = msg.exec_()

    def make_request(self, login, hash_password):
        try:
            response = requests.post('http://127.0.0.1:8000/registration', json = {'login': login, 'password': hash_password}, timeout = 5)
            
            if response.status_code == 200:
                self.show_info_messagebox('Поздравляю, регистрация прошла успешно! Теперь войдите в свой профиль через главное меню')
            elif response.status_code == 404:
                self.show_info_messagebox('Извините, но пользователь с таким логином уже существует')
        except:
            self.show_info_messagebox('Ошибка соединения')



    def check_input_data(self):
        login = self.login_field.text()
        password = self.password_field.text()

        if login == '' or password == '':
            self.show_info_messagebox("Все поля должны быть заполнены!")
        elif len(login) >= 16 or len(login) < 3:
            self.show_info_messagebox('Длина логина должна быть больше 2 и меньше 16')
        elif len(password) >= 21 or len(password) <= 3:
            self.show_info_messagebox('Длина пароля должна быть больше 3 и меньше 21')
        else:
            for el in login:
                if el not in map(chr, range(1, 256)):
                    self.show_info_messagebox('В логине могут быть лишь латинские буквы, цифры и специальные символы')
                    break
            else:
                for el in password:
                    if el not in map(chr, range(1, 256)):
                        self.show_info_messagebox('В пароле могут быть лишь латинские буквы, цифры и специальные символы')
                        break
                else:
                    print('Something')
                    hash_password = main_idea(password)
                    self.make_request(login, hash_password)

           

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Регистрация"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.to_registrate.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.get_back.setText(_translate("MainWindow", "<"))

    def add_signals(self):
        self.get_back.clicked.connect(lambda: self.main_page())
        self.to_registrate.clicked.connect(lambda: self.check_input_data())
       


