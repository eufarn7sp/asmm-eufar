# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutwindow.ui'
#
# Created: Fri Feb 13 13:26:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_aboutStandard(object):
    def setupUi(self, aboutStandard):
        aboutStandard.setObjectName(_fromUtf8("aboutStandard"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutStandard.sizePolicy().hasHeightForWidth())
        aboutStandard.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        aboutStandard.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/xml_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutStandard.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(aboutStandard)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.aw_label_2 = QtGui.QLabel(aboutStandard)
        self.aw_label_2.setMinimumSize(QtCore.QSize(55, 55))
        self.aw_label_2.setMaximumSize(QtCore.QSize(55, 55))
        self.aw_label_2.setText(_fromUtf8(""))
        self.aw_label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/xml_icon.png")))
        self.aw_label_2.setScaledContents(True)
        self.aw_label_2.setObjectName(_fromUtf8("aw_label_2"))
        self.verticalLayout.addWidget(self.aw_label_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.aw_label_1 = QtGui.QLabel(aboutStandard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aw_label_1.sizePolicy().hasHeightForWidth())
        self.aw_label_1.setSizePolicy(sizePolicy)
        self.aw_label_1.setMinimumSize(QtCore.QSize(341, 170))
        self.aw_label_1.setMaximumSize(QtCore.QSize(341, 250))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_1.setFont(font)
        self.aw_label_1.setFrameShape(QtGui.QFrame.NoFrame)
        self.aw_label_1.setFrameShadow(QtGui.QFrame.Plain)
        self.aw_label_1.setLineWidth(1)
        self.aw_label_1.setMidLineWidth(0)
        self.aw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.aw_label_1.setScaledContents(False)
        self.aw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aw_label_1.setWordWrap(True)
        self.aw_label_1.setObjectName(_fromUtf8("aw_label_1"))
        if os.name == "posix":
            aboutStandard.resize(452, 220)
            aboutStandard.setMinimumSize(QtCore.QSize(450, 220))
            aboutStandard.setMaximumSize(QtCore.QSize(452, 270))
            self.aw_label_1.setMinimumSize(QtCore.QSize(341, 170))
            self.aw_label_1.setMaximumSize(QtCore.QSize(341, 250))
        elif os.name == "nt":
            aboutStandard.resize(550, 350)
            aboutStandard.setMinimumSize(QtCore.QSize(550, 350))
            aboutStandard.setMaximumSize(QtCore.QSize(550, 350))
            self.aw_label_1.setMinimumSize(QtCore.QSize(450, 220))
            self.aw_label_1.setMaximumSize(QtCore.QSize(450, 220))
        else:
            aboutStandard.resize(452, 220)
            aboutStandard.setMinimumSize(QtCore.QSize(450, 220))
            aboutStandard.setMaximumSize(QtCore.QSize(452, 270))
            self.aw_label_1.setMinimumSize(QtCore.QSize(341, 170))
            self.aw_label_1.setMaximumSize(QtCore.QSize(341, 250))
        self.horizontalLayout.addWidget(self.aw_label_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.aw_okButton = QtGui.QPushButton(aboutStandard)
        self.aw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.aw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.aw_okButton.setFont(font)
        self.aw_okButton.setObjectName(_fromUtf8("aw_okButton"))
        self.horizontalLayout_2.addWidget(self.aw_okButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(aboutStandard)
        QtCore.QMetaObject.connectSlotsByName(aboutStandard)

    def retranslateUi(self, aboutStandard):
        aboutStandard.setWindowTitle(_translate("aboutStandard", "About ASMM XML Standard", None))
        self.aw_label_1.setText(_translate("aboutStandard", "<html><head/><body><p><br/></p></body></html>", None))
        self.aw_okButton.setText(_translate("aboutStandard", "OK", None))

