# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valveui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progress1 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress1.setGeometry(QtCore.QRect(475, 120, 200, 25))
        self.progress1.setProperty("value", 24)
        self.progress1.setObjectName("progress1")
        self.lcd1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd1.setGeometry(QtCore.QRect(675, 120, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd1.setFont(font)
        self.lcd1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd1.setObjectName("lcd1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(675, 70, 100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 70, 100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.ref1 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref1.setGeometry(QtCore.QRect(110, 120, 100, 25))
        self.ref1.setObjectName("ref1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 75, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 120, 50, 25))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(475, 70, 100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.ref2 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref2.setGeometry(QtCore.QRect(110, 150, 100, 25))
        self.ref2.setObjectName("ref2")
        self.lcd2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd2.setGeometry(QtCore.QRect(675, 150, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd2.setFont(font)
        self.lcd2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd2.setObjectName("lcd2")
        self.progress2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress2.setGeometry(QtCore.QRect(475, 150, 200, 25))
        self.progress2.setProperty("value", 24)
        self.progress2.setObjectName("progress2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 150, 50, 25))
        self.label_7.setObjectName("label_7")
        self.ref3 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref3.setGeometry(QtCore.QRect(110, 180, 100, 25))
        self.ref3.setObjectName("ref3")
        self.ref4 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref4.setGeometry(QtCore.QRect(110, 210, 100, 25))
        self.ref4.setObjectName("ref4")
        self.ref5 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref5.setGeometry(QtCore.QRect(110, 240, 100, 25))
        self.ref5.setObjectName("ref5")
        self.ref6 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref6.setGeometry(QtCore.QRect(110, 270, 100, 25))
        self.ref6.setObjectName("ref6")
        self.ref7 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref7.setGeometry(QtCore.QRect(110, 300, 100, 25))
        self.ref7.setObjectName("ref7")
        self.ref8 = QtWidgets.QTextEdit(self.centralwidget)
        self.ref8.setGeometry(QtCore.QRect(110, 330, 100, 25))
        self.ref8.setObjectName("ref8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 180, 50, 25))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 210, 50, 25))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 240, 50, 25))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 270, 50, 25))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 300, 50, 25))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 330, 50, 25))
        self.label_13.setObjectName("label_13")
        self.progress3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress3.setGeometry(QtCore.QRect(475, 180, 200, 25))
        self.progress3.setProperty("value", 24)
        self.progress3.setObjectName("progress3")
        self.progress4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress4.setGeometry(QtCore.QRect(475, 210, 200, 25))
        self.progress4.setProperty("value", 24)
        self.progress4.setObjectName("progress4")
        self.progress5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress5.setGeometry(QtCore.QRect(475, 240, 200, 25))
        self.progress5.setProperty("value", 24)
        self.progress5.setObjectName("progress5")
        self.progress6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress6.setGeometry(QtCore.QRect(475, 270, 200, 25))
        self.progress6.setProperty("value", 24)
        self.progress6.setObjectName("progress6")
        self.progress7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress7.setGeometry(QtCore.QRect(475, 300, 200, 25))
        self.progress7.setProperty("value", 24)
        self.progress7.setObjectName("progress7")
        self.progress8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progress8.setGeometry(QtCore.QRect(475, 330, 200, 25))
        self.progress8.setProperty("value", 24)
        self.progress8.setObjectName("progress8")
        self.lcd3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd3.setGeometry(QtCore.QRect(675, 180, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd3.setFont(font)
        self.lcd3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd3.setObjectName("lcd3")
        self.lcd4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd4.setGeometry(QtCore.QRect(675, 210, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd4.setFont(font)
        self.lcd4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd4.setObjectName("lcd4")
        self.lcd5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd5.setGeometry(QtCore.QRect(675, 240, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd5.setFont(font)
        self.lcd5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd5.setObjectName("lcd5")
        self.lcd6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd6.setGeometry(QtCore.QRect(675, 270, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd6.setFont(font)
        self.lcd6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd6.setObjectName("lcd6")
        self.lcd7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd7.setGeometry(QtCore.QRect(675, 300, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd7.setFont(font)
        self.lcd7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd7.setObjectName("lcd7")
        self.lcd8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd8.setGeometry(QtCore.QRect(675, 330, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcd8.setFont(font)
        self.lcd8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd8.setObjectName("lcd8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 420, 50, 25))
        self.label_14.setObjectName("label_14")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(230, 420, 100, 25))
        self.checkBox.setObjectName("checkBox")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 400, 75, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(110, 400, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(230, 400, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(300, 70, 150, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(575, 505, 200, 50))
        self.startButton.setObjectName("startButton")
        self.status1 = QtWidgets.QLabel(self.centralwidget)
        self.status1.setGeometry(QtCore.QRect(365, 120, 25, 25))
        self.status1.setText("")
        self.status1.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status1.setScaledContents(True)
        self.status1.setObjectName("status1")
        self.status2 = QtWidgets.QLabel(self.centralwidget)
        self.status2.setGeometry(QtCore.QRect(365, 150, 25, 25))
        self.status2.setText("")
        self.status2.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status2.setScaledContents(True)
        self.status2.setObjectName("status2")
        self.status3 = QtWidgets.QLabel(self.centralwidget)
        self.status3.setGeometry(QtCore.QRect(365, 180, 25, 25))
        self.status3.setText("")
        self.status3.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status3.setScaledContents(True)
        self.status3.setObjectName("status3")
        self.status4 = QtWidgets.QLabel(self.centralwidget)
        self.status4.setGeometry(QtCore.QRect(365, 210, 25, 25))
        self.status4.setText("")
        self.status4.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status4.setScaledContents(True)
        self.status4.setObjectName("status4")
        self.status5 = QtWidgets.QLabel(self.centralwidget)
        self.status5.setGeometry(QtCore.QRect(365, 240, 25, 25))
        self.status5.setText("")
        self.status5.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status5.setScaledContents(True)
        self.status5.setObjectName("status5")
        self.status6 = QtWidgets.QLabel(self.centralwidget)
        self.status6.setGeometry(QtCore.QRect(365, 270, 25, 25))
        self.status6.setText("")
        self.status6.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status6.setScaledContents(True)
        self.status6.setObjectName("status6")
        self.status7 = QtWidgets.QLabel(self.centralwidget)
        self.status7.setGeometry(QtCore.QRect(365, 300, 25, 25))
        self.status7.setText("")
        self.status7.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status7.setScaledContents(True)
        self.status7.setObjectName("status7")
        self.status8 = QtWidgets.QLabel(self.centralwidget)
        self.status8.setGeometry(QtCore.QRect(365, 330, 25, 25))
        self.status8.setText("")
        self.status8.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status8.setScaledContents(True)
        self.status8.setObjectName("status8")
        self.status9 = QtWidgets.QLabel(self.centralwidget)
        self.status9.setGeometry(QtCore.QRect(365, 420, 25, 25))
        self.status9.setText("")
        self.status9.setPixmap(QtGui.QPixmap("../../ValveControl/if_Red Ball_38831.png"))
        self.status9.setScaledContents(True)
        self.status9.setObjectName("status9")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(30, 470, 75, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.CycleBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CycleBox.setGeometry(QtCore.QRect(120, 470, 75, 25))
        self.CycleBox.setMinimum(-1)
        self.CycleBox.setProperty("value", 1)
        self.CycleBox.setObjectName("CycleBox")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(20, 500, 75, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(20, 530, 75, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(230, 70, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_32.setObjectName("label_32")
        self.skip1 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip1.setGeometry(QtCore.QRect(230, 120, 25, 25))
        self.skip1.setText("")
        self.skip1.setObjectName("skip1")
        self.skip2 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip2.setGeometry(QtCore.QRect(230, 150, 25, 25))
        self.skip2.setText("")
        self.skip2.setObjectName("skip2")
        self.skip3 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip3.setGeometry(QtCore.QRect(230, 180, 25, 25))
        self.skip3.setText("")
        self.skip3.setObjectName("skip3")
        self.skip4 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip4.setGeometry(QtCore.QRect(230, 210, 25, 25))
        self.skip4.setText("")
        self.skip4.setObjectName("skip4")
        self.skip5 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip5.setGeometry(QtCore.QRect(230, 240, 25, 25))
        self.skip5.setText("")
        self.skip5.setObjectName("skip5")
        self.skip6 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip6.setGeometry(QtCore.QRect(230, 270, 25, 25))
        self.skip6.setText("")
        self.skip6.setObjectName("skip6")
        self.skip7 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip7.setGeometry(QtCore.QRect(230, 300, 25, 25))
        self.skip7.setText("")
        self.skip7.setObjectName("skip7")
        self.skip8 = QtWidgets.QCheckBox(self.centralwidget)
        self.skip8.setGeometry(QtCore.QRect(230, 330, 25, 25))
        self.skip8.setText("")
        self.skip8.setObjectName("skip8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 390, 760, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 440, 760, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.flowTimeBox = QtWidgets.QTimeEdit(self.centralwidget)
        self.flowTimeBox.setGeometry(QtCore.QRect(120, 500, 75, 25))
        self.flowTimeBox.setObjectName("flowTimeBox")
        self.dwellTimeBox = QtWidgets.QTimeEdit(self.centralwidget)
        self.dwellTimeBox.setGeometry(QtCore.QRect(120, 530, 75, 25))
        self.dwellTimeBox.setObjectName("dwellTimeBox")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(270, 480, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(270, 530, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.startTimeBox = QtWidgets.QLabel(self.centralwidget)
        self.startTimeBox.setGeometry(QtCore.QRect(425, 480, 150, 25))
        self.startTimeBox.setObjectName("startTimeBox")
        self.endTimeBox = QtWidgets.QLabel(self.centralwidget)
        self.endTimeBox.setGeometry(QtCore.QRect(425, 530, 150, 25))
        self.endTimeBox.setObjectName("endTimeBox")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(223, 460, 20, 101))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.closeTimeBox = QtWidgets.QTimeEdit(self.centralwidget)
        self.closeTimeBox.setGeometry(QtCore.QRect(120, 420, 75, 25))
        self.closeTimeBox.setObjectName("closeTimeBox")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(0, 10, 800, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.ventButton = QtWidgets.QPushButton(self.centralwidget)
        self.ventButton.setGeometry(QtCore.QRect(400, 400, 100, 45))
        self.ventButton.setObjectName("ventButton")
        self.refButton = QtWidgets.QPushButton(self.centralwidget)
        self.refButton.setGeometry(QtCore.QRect(110, 360, 100, 25))
        self.refButton.setObjectName("refButton")
        self.serNumText = QtWidgets.QTextEdit(self.centralwidget)
        self.serNumText.setGeometry(QtCore.QRect(550, 420, 225, 25))
        self.serNumText.setObjectName("serNumText")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(550, 400, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(575, 450, 100, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.filenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.filenameLabel.setGeometry(QtCore.QRect(575, 470, 200, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.filenameLabel.setFont(font)
        self.filenameLabel.setObjectName("filenameLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Time Remaining<br> (sec)"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Reference <br/><span style=\" font-weight:400;\">(ppm)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Gas/Valve #"))
        self.label.setText(_translate("MainWindow", "Gas #1"))
        self.label_5.setText(_translate("MainWindow", "Current Progress"))
        self.label_7.setText(_translate("MainWindow", "Gas #2"))
        self.label_8.setText(_translate("MainWindow", "Gas #3"))
        self.label_9.setText(_translate("MainWindow", "Gas #4"))
        self.label_10.setText(_translate("MainWindow", "Gas #5"))
        self.label_11.setText(_translate("MainWindow", "Gas #6"))
        self.label_12.setText(_translate("MainWindow", "Gas #7"))
        self.label_13.setText(_translate("MainWindow", "Gas #8"))
        self.label_14.setText(_translate("MainWindow", "Valve #9"))
        self.checkBox.setText(_translate("MainWindow", "Always Open"))
        self.label_15.setText(_translate("MainWindow", "Gas/Valve #"))
        self.label_16.setText(_translate("MainWindow", "Close Time "))
        self.label_18.setText(_translate("MainWindow", "Valve Override"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Status <br/><span style=\" font-weight:400;\">Green = Open<br/>Red = Closed</span></p></body></html>"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p>Repeat Num<br/>Cycles</p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p>Flow Time<br/>(hh:mm:ss)</p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p>Dwell Time<br/>(hh:mm:ss)</p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Skip?"))
        self.flowTimeBox.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.dwellTimeBox.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p>Start Time</p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p>Complete Time</p></body></html>"))
        self.startTimeBox.setText(_translate("MainWindow", "(Start Time)"))
        self.endTimeBox.setText(_translate("MainWindow", "(Estimated Complete Time)"))
        self.closeTimeBox.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p>CO<span style=\" vertical-align:sub;\">2 </span>Valve Automation</p></body></html>"))
        self.ventButton.setText(_translate("MainWindow", "HOLD TO VENT"))
        self.refButton.setText(_translate("MainWindow", "Save Ref. Values"))
        self.label_21.setText(_translate("MainWindow", "Serial Number"))
        self.label_22.setText(_translate("MainWindow", "File Name"))
        self.filenameLabel.setText(_translate("MainWindow", "<filename_xxx>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

