# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1176, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 420, 1311, 291))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.std_piechart = QtGui.QVBoxLayout()
        self.std_piechart.setObjectName(_fromUtf8("std_piechart"))
        self.horizontalLayout_2.addLayout(self.std_piechart)
        self.stdSummary = QtGui.QTextEdit(self.layoutWidget)
        self.stdSummary.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stdSummary.sizePolicy().hasHeightForWidth())
        self.stdSummary.setSizePolicy(sizePolicy)
        self.stdSummary.setMinimumSize(QtCore.QSize(180, 0))
        self.stdSummary.setStyleSheet(_fromUtf8("background-color: rgba(1,1,1,0.5);\n"
"color: rgb(0, 0, 0);"))
        self.stdSummary.setObjectName(_fromUtf8("stdSummary"))
        self.horizontalLayout_2.addWidget(self.stdSummary)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.res_piechart = QtGui.QVBoxLayout()
        self.res_piechart.setObjectName(_fromUtf8("res_piechart"))
        self.horizontalLayout.addLayout(self.res_piechart)
        self.resSummary = QtGui.QTextEdit(self.layoutWidget)
        self.resSummary.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resSummary.sizePolicy().hasHeightForWidth())
        self.resSummary.setSizePolicy(sizePolicy)
        self.resSummary.setMinimumSize(QtCore.QSize(180, 0))
        self.resSummary.setStyleSheet(_fromUtf8("background-color: rgba(1,1,1,0.5);\n"
"color: rgb(0, 0, 0);"))
        self.resSummary.setObjectName(_fromUtf8("resSummary"))
        self.horizontalLayout.addWidget(self.resSummary)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1300, 381))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(950, 10, 321, 271))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox\n"
"{\n"
"border: 1px solid gray;\n"
"}"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 291, 20))
        self.label_3.setStyleSheet(_fromUtf8("border: 1px solid grey;"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(110, 10, 101, 91))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/ui_start/png/save-download-icon-10.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 140, 301, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.browser = QtGui.QLineEdit(self.layoutWidget1)
        self.browser.setObjectName(_fromUtf8("browser"))
        self.horizontalLayout_4.addWidget(self.browser)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.browseBut = QtGui.QPushButton(self.layoutWidget1)
        self.browseBut.setObjectName(_fromUtf8("browseBut"))
        self.horizontalLayout_5.addWidget(self.browseBut)
        self.saveBut = QtGui.QPushButton(self.layoutWidget1)
        self.saveBut.setObjectName(_fromUtf8("saveBut"))
        self.horizontalLayout_5.addWidget(self.saveBut)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.savePie = QtGui.QPushButton(self.layoutWidget1)
        self.savePie.setObjectName(_fromUtf8("savePie"))
        self.horizontalLayout_6.addWidget(self.savePie)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 451, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgba(1,1,1,0.5);\n"
"color: rgb(0, 0, 0);\n"
"border: 0 px;\n"
"font: 63 14pt \"Ubuntu\";"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.res_summary = QtGui.QTextEdit(self.tab)
        self.res_summary.setGeometry(QtCore.QRect(10, 60, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_summary.setFont(font)
        self.res_summary.setStyleSheet(_fromUtf8("background-color: rgba(1,1,1,0.5);\n"
"color: rgb(0, 0, 0);"))
        self.res_summary.setObjectName(_fromUtf8("res_summary"))
        self.test_again = QtGui.QPushButton(self.tab)
        self.test_again.setGeometry(QtCore.QRect(1160, 290, 111, 27))
        self.test_again.setObjectName(_fromUtf8("test_again"))
        self.layoutWidget2 = QtGui.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 119, 241, 232))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.tot = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tot.setFont(font)
        self.tot.setObjectName(_fromUtf8("tot"))
        self.horizontalLayout_15.addWidget(self.tot)
        self.tot_val = QtGui.QLabel(self.layoutWidget2)
        self.tot_val.setText(_fromUtf8(""))
        self.tot_val.setObjectName(_fromUtf8("tot_val"))
        self.horizontalLayout_15.addWidget(self.tot_val)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.line = QtGui.QFrame(self.layoutWidget2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.normal_res = QtGui.QLabel(self.layoutWidget2)
        self.normal_res.setText(_fromUtf8(""))
        self.normal_res.setObjectName(_fromUtf8("normal_res"))
        self.horizontalLayout_7.addWidget(self.normal_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.nep_res = QtGui.QLabel(self.layoutWidget2)
        self.nep_res.setText(_fromUtf8(""))
        self.nep_res.setObjectName(_fromUtf8("nep_res"))
        self.horizontalLayout_8.addWidget(self.nep_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_8 = QtGui.QLabel(self.layoutWidget2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_9.addWidget(self.label_8)
        self.smurf_res = QtGui.QLabel(self.layoutWidget2)
        self.smurf_res.setText(_fromUtf8(""))
        self.smurf_res.setObjectName(_fromUtf8("smurf_res"))
        self.horizontalLayout_9.addWidget(self.smurf_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_9 = QtGui.QLabel(self.layoutWidget2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_10.addWidget(self.label_9)
        self.back_res = QtGui.QLabel(self.layoutWidget2)
        self.back_res.setText(_fromUtf8(""))
        self.back_res.setObjectName(_fromUtf8("back_res"))
        self.horizontalLayout_10.addWidget(self.back_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_11 = QtGui.QLabel(self.layoutWidget2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_11.addWidget(self.label_11)
        self.tear_res = QtGui.QLabel(self.layoutWidget2)
        self.tear_res.setText(_fromUtf8(""))
        self.tear_res.setObjectName(_fromUtf8("tear_res"))
        self.horizontalLayout_11.addWidget(self.tear_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_10 = QtGui.QLabel(self.layoutWidget2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_12.addWidget(self.label_10)
        self.pod_res = QtGui.QLabel(self.layoutWidget2)
        self.pod_res.setText(_fromUtf8(""))
        self.pod_res.setObjectName(_fromUtf8("pod_res"))
        self.horizontalLayout_12.addWidget(self.pod_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_13 = QtGui.QLabel(self.layoutWidget2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_13.addWidget(self.label_13)
        self.land_res = QtGui.QLabel(self.layoutWidget2)
        self.land_res.setText(_fromUtf8(""))
        self.land_res.setObjectName(_fromUtf8("land_res"))
        self.horizontalLayout_13.addWidget(self.land_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_15 = QtGui.QLabel(self.layoutWidget2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_14.addWidget(self.label_15)
        self.anomaly_res = QtGui.QLabel(self.layoutWidget2)
        self.anomaly_res.setText(_fromUtf8(""))
        self.anomaly_res.setObjectName(_fromUtf8("anomaly_res"))
        self.horizontalLayout_14.addWidget(self.anomaly_res)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 10, 451, 321))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 401, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 400, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Save Report To DIsk", None))
        self.label_4.setText(_translate("MainWindow", "Filename", None))
        self.browseBut.setText(_translate("MainWindow", "Browse", None))
        self.saveBut.setText(_translate("MainWindow", "Save", None))
        self.savePie.setText(_translate("MainWindow", "Save PieChart Figure", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">The predictions for the data set are displayed below:</span></p></body></html>", None))
        self.test_again.setText(_translate("MainWindow", "Test Again", None))
        self.tot.setText(_translate("MainWindow", "Total Dataset:", None))
        self.label_6.setText(_translate("MainWindow", "Normal :", None))
        self.label_7.setText(_translate("MainWindow", "Neptune:", None))
        self.label_8.setText(_translate("MainWindow", "Smurf:", None))
        self.label_9.setText(_translate("MainWindow", "Back:", None))
        self.label_11.setText(_translate("MainWindow", "Teardrop:", None))
        self.label_10.setText(_translate("MainWindow", "Pod:", None))
        self.label_13.setText(_translate("MainWindow", "Land:", None))
        self.label_15.setText(_translate("MainWindow", "Anomaly:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Analysis of Result", None))
        self.label.setText(_translate("MainWindow", "True Value:", None))
        self.label_2.setText(_translate("MainWindow", "Detected Value:", None))

import res_rc