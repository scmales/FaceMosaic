# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_mosaic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(290, 290)
        MainWindow.setMinimumSize(QtCore.QSize(268, 216))
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 75, 31))
        self.pushButton.setObjectName("pushButton")

        self.toolButton_1 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_1.setGeometry(QtCore.QRect(50, 40, 80, 21))
        self.toolButton_1.setObjectName("toolButton_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(140, 40, 120, 21))
        self.label_1.setObjectName("label_1")

        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(50, 90, 80, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 120, 21))
        self.label_2.setObjectName("label_2")

        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(50, 140, 80, 21))
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 140, 120, 21))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "face_mosaic"))
        self.pushButton.setText(_translate("MainWindow", "打码并保存"))
        self.toolButton_1.setText(_translate("MainWindow", "源文件夹"))
        self.label_1.setText(_translate("MainWindow", "未选择任何路径"))
        self.toolButton_2.setText(_translate("MainWindow", "源图片"))
        self.label_2.setText(_translate("MainWindow", "未选择任何图片"))
        self.toolButton_3.setText(_translate("MainWindow", "保存路径"))
        self.label_4.setText(_translate("MainWindow", "未选择任何路径"))

