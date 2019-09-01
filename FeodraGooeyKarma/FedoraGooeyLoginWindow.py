# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(250, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(250, 300))
        Login.setMaximumSize(QtCore.QSize(250, 300))
        self.gridLayoutWidget = QtWidgets.QWidget(Login)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 5, 0, 1, 1)
        self.label_username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 2, 0, 1, 1)
        self.label_Password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Password.setObjectName("label_Password")
        self.gridLayout.addWidget(self.label_Password, 4, 0, 1, 1)
        self.fedoraReleases = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.fedoraReleases.setObjectName("fedoraReleases")
        self.gridLayout.addWidget(self.fedoraReleases, 7, 0, 1, 1)
        self.label_FeodraVersion = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_FeodraVersion.setObjectName("label_FeodraVersion")
        self.gridLayout.addWidget(self.label_FeodraVersion, 6, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 8, 0, 1, 1)
        self.Username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Username.setObjectName("Username")
        self.gridLayout.addWidget(self.Username, 3, 0, 1, 1)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_username.setText(_translate("Login", "Username"))
        self.label_Password.setText(_translate("Login", "Password"))
        self.label_FeodraVersion.setText(_translate("Login", "Fedora Version"))
        self.saveButton.setText(_translate("Login", "Save"))
