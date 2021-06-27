# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setIconSize(QtCore.QSize(16, 16))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OSIcon = QtWidgets.QLabel(self.centralwidget)
        self.OSIcon.setObjectName("OSIcon")
        self.horizontalLayout.addWidget(self.OSIcon)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.OSName = QtWidgets.QLabel(self.centralwidget)
        self.OSName.setObjectName("OSName")
        self.verticalLayout.addWidget(self.OSName)
        self.Version = QtWidgets.QLabel(self.centralwidget)
        self.Version.setObjectName("Version")
        self.verticalLayout.addWidget(self.Version)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.HostType = QtWidgets.QLabel(self.centralwidget)
        self.HostType.setObjectName("HostType")
        self.verticalLayout.addWidget(self.HostType)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.CPUInfo = QtWidgets.QLabel(self.centralwidget)
        self.CPUInfo.setObjectName("CPUInfo")
        self.verticalLayout.addWidget(self.CPUInfo)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.MemInfo = QtWidgets.QLabel(self.centralwidget)
        self.MemInfo.setObjectName("MemInfo")
        self.verticalLayout.addWidget(self.MemInfo)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.Disk = QtWidgets.QLabel(self.centralwidget)
        self.Disk.setObjectName("Disk")
        self.verticalLayout.addWidget(self.Disk)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.GPUInfo = QtWidgets.QLabel(self.centralwidget)
        self.GPUInfo.setObjectName("GPUInfo")
        self.verticalLayout.addWidget(self.GPUInfo)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.Serial = QtWidgets.QLabel(self.centralwidget)
        self.Serial.setObjectName("Serial")
        self.verticalLayout.addWidget(self.Serial)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SysReport = QtWidgets.QPushButton(self.centralwidget)
        self.SysReport.setMaximumSize(QtCore.QSize(16777215, 22))
        self.SysReport.setDefault(True)
        self.SysReport.setFlat(False)
        self.SysReport.setObjectName("SysReport")
        self.horizontalLayout_3.addWidget(self.SysReport)
        spacerItem10 = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.SoftUpdate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SoftUpdate.sizePolicy().hasHeightForWidth())
        self.SoftUpdate.setSizePolicy(sizePolicy)
        self.SoftUpdate.setMaximumSize(QtCore.QSize(16777215, 22))
        self.SoftUpdate.setObjectName("SoftUpdate")
        self.horizontalLayout_3.addWidget(self.SoftUpdate)
        spacerItem11 = QtWidgets.QSpacerItem(80, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.CopyrightNotice = QtWidgets.QLabel(self.centralwidget)
        self.CopyrightNotice.setObjectName("CopyrightNotice")
        self.horizontalLayout_2.addWidget(self.CopyrightNotice)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System Information"))
        self.OSIcon.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"256\" src=\":/icon/icons/big_sur.png\"/></p></body></html>"))
        self.OSName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:504;\">Arch</span><span style=\" font-size:24pt; font-weight:304;\"> Linux</span></p></body></html>"))
        self.Version.setText(_translate("MainWindow", "<html><head/><body><p>Version 5.12.7-zen1-1-zen</p></body></html>"))
        self.HostType.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">HP Envy x360 Convertible (15-inch, Late 2016)</span></p></body></html>"))
        self.CPUInfo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Processor</span><span style=\"font-weight:800;\">  </span><span style=\" font-weight:300;\">3.2 GHz Dual-Core Intel Core i7</span></p></body></html>"))
        self.MemInfo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Memory </span><span style=\" font-weight:300;\">16 GB 2400 MHz DDR4</span></p></body></html>"))
        self.Disk.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Startup Disk </span><span style=\" font-weight:300;\">113.0 GiB Hard Drive</span></p></body></html>"))
        self.GPUInfo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Graphics </span><span style=\" font-weight:300;\">Intel Iris Graphics 540</span></p></body></html>"))
        self.Serial.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Serial Number </span><span style=\" font-weight:300;\">69</span></p></body></html>"))
        self.SysReport.setText(_translate("MainWindow", "System Report..."))
        self.SoftUpdate.setText(_translate("MainWindow", "Software Update..."))
        self.CopyrightNotice.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:304; color:#777777;\">™ and © 2021-2021 EvilSquirrelGuy. Licensed under the LGPLv2.1 License</span></p></body></html>"))
import icon_rc
