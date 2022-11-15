# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PigUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import sqlite3
#import streamlit
#from PigWeb import PigWeb
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(320, 240, 91, 41))
        self.OK.setObjectName("OK")
        self.InputID = QtWidgets.QLineEdit(self.centralwidget)
        self.InputID.setGeometry(QtCore.QRect(190, 140, 241, 31))
        self.InputID.setObjectName("InputID")
        self.PassWord = QtWidgets.QLineEdit(self.centralwidget)
        self.PassWord.setGeometry(QtCore.QRect(190, 190, 241, 31))
        self.PassWord.setObjectName("PassWord")
        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(140, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ID.setFont(font)
        self.label_ID.setObjectName("label_ID")
        self.label_PW = QtWidgets.QLabel(self.centralwidget)
        self.label_PW.setGeometry(QtCore.QRect(140, 190, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_PW.setFont(font)
        self.label_PW.setObjectName("label_PW")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(90, 30, 431, 41))
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(25)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.label_Tips = QtWidgets.QLabel(self.centralwidget)
        self.label_Tips.setGeometry(QtCore.QRect(10, 390, 621, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        self.label_Tips.setFont(font)
        self.label_Tips.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Tips.setText("")
        self.label_Tips.setObjectName("label_Tips")
        self.Back_Img = QtWidgets.QLabel(self.centralwidget)
        self.Back_Img.setGeometry(QtCore.QRect(40, 80, 561, 281))
        self.Back_Img.setText("")
        self.Back_Img.setObjectName("Back_Img")
        self.Back_Img.raise_()
        self.OK.raise_()
        self.InputID.raise_()
        self.PassWord.raise_()
        self.label_ID.raise_()
        self.label_PW.raise_()
        self.Title.raise_()
        self.label_Tips.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #背景图片
#        pix = QtGui.QPixmap("./pig1.png")
#        self.Back_Img.setPixmap(pix)
#        self.Back_Img.resize(267,150)
        #数据库连接
        self.slot_init()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OK.setText(_translate("MainWindow", "登录"))
        self.label_ID.setText(_translate("MainWindow", "账号"))
        self.label_PW.setText(_translate("MainWindow", "密码"))
        self.Title.setText(_translate("MainWindow", "智能猪场看板管理系统"))
    
#    def add_userdata(username, password):
#    
#        if c.execute("SELECT User FROM UserManager WHERE User = :username",{"username":username}):
#            st.warning("用户名已存在，请更换一个新的用户名。")
#        else:
#            c.execute("INSERT INTO userstable(username,password) VALUES(?,?)",(username,password))
#            con.commit()
#            st.success("恭喜，您已成功注册。")
#            st.info("请在左侧选择“登录”选项进行登录。")

            
    def on_OK_clicked(self):
        base_dir=os.path.dirname(os.path.abspath(__file__))
        db_path=base_dir+'\PigManager.db'
        self.con = sqlite3.connect(db_path)
        self.c = self.con.cursor()
        print(self.InputID.text(),self.PassWord.text())
        self.c.execute("SELECT User FROM UserManager WHERE User = :username",{"username":self.InputID.text()})
        Id_check=self.c.fetchall()
        if Id_check:
            self.c.execute("SELECT * FROM UserManager WHERE User = :username AND Password = :password",{"username":self.InputID.text(),"password":self.PassWord.text()})
            IdPW=self.c.fetchall()
            if IdPW:
                os.system("cd "+base_dir)
                os.system("streamlit run .\Mainapp.py")
                #streamlit.cli._main_run_clExplicit('Mainapp.py', 'streamlit run')
                

            else:
                self.label_Tips.setText("密码错误!")
        else:
            self.label_Tips.setText("用户名不存在，请先选择注册按钮完成注册。")
        self.con.close()
        
    def slot_init(self):
        self.OK.clicked.connect(self.on_OK_clicked)

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())