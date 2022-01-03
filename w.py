#!/usr/bin/python3

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
import sys
from PyQt5.QtWidgets import QLabel 

import mysql.connector
#from mysql.connector import Error
#from mysql.connector import errorcode
 

 
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
    QPushButton, QAction, QLineEdit, QMessageBox)

 
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Тест'
        self.left = 200
        self.top = 200
        self.width = 400
        self.height = 140
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel('Name',self)
        self.label.move(0,30)
        self.label.resize(41,19)
        self.label = QLabel('Email',self)
        self.label.move(0,90)
        self.label.resize(51,19)
        self.label = QLabel('Id',self)
        self.label.move(10,140)
        self.label.resize(31,19)
        self.textbox = QLineEdit(self)
        self.textbox.move(60, 20)
        self.textbox.resize(256, 41)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(60, 80)
        self.textbox2.resize(256, 41)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(60, 130)
        self.textbox3.resize(101, 31)
        self.button = QPushButton('Добавить', self)
        self.button.move(340, 60)
 
        self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        name = self.textbox.text()
        email = self.textbox2.text()
        self.textbox.setText("")
        self.textbox2.setText("")
        id = self.textbox3.text()
        id = int(id)
        try:
            connection = mysql.connector.connect(host='db4free.net',
                                         database='pyqt5test',
                                         user='hookah12',
                                         password='12345678')
            sql = "INSERT INTO test (id,name, email) VALUES (%s,%s, %s)"
            val = (id,name,email)
            cursor = connection.cursor()
            cursor.execute(sql,val)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Laptop table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
 
 
 
   # def InsertData(self):
      #  pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.resize(491,184)
    sys.exit(app.exec_())