# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{background-color: \"#102143\"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 15, 10, 15)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(20, 20))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/hdd-network-fill.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("color: white;\n"
"font: 75 9pt \"Segoe UI Bold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(193, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.btn_settings = QtWidgets.QLabel(self.frame_3)
        self.btn_settings.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_settings.setText("")
        self.btn_settings.setPixmap(QtGui.QPixmap(":/icons/box-arrow-down.png"))
        self.btn_settings.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout_7.addWidget(self.btn_settings)
        spacerItem1 = QtWidgets.QSpacerItem(194, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txt_date = QtWidgets.QLabel(self.frame_2)
        self.txt_date.setStyleSheet("color: white;\n"
"font: 25 9pt \"Segoe UI\";")
        self.txt_date.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_date.setObjectName("txt_date")
        self.horizontalLayout_6.addWidget(self.txt_date)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/divider.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/battery-charging.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ph_container = QtWidgets.QFrame(self.centralwidget)
        self.ph_container.setStyleSheet("#ph_container{\n"
"    border-image: url(:/bg/insight-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.ph_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ph_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ph_container.setObjectName("ph_container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ph_container)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.ph_container)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.frame_7)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.horizontalLayout_12.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setStyleSheet("")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.txt_average_ph_level = QtWidgets.QLabel(self.frame_8)
        self.txt_average_ph_level.setStyleSheet("color: rgb(255, 255, 255, 100);\n"
"font: 9pt \"Segoe UI\";")
        self.txt_average_ph_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_average_ph_level.setObjectName("txt_average_ph_level")
        self.horizontalLayout_14.addWidget(self.txt_average_ph_level)
        self.horizontalLayout_12.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.ph_container)
        self.frame_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Segoe UI\";")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.txt_current_ph_level = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_current_ph_level.sizePolicy().hasHeightForWidth())
        self.txt_current_ph_level.setSizePolicy(sizePolicy)
        self.txt_current_ph_level.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_current_ph_level.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_current_ph_level.setObjectName("txt_current_ph_level")
        self.horizontalLayout_16.addWidget(self.txt_current_ph_level)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.ph_container)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.txt_ph_level_ref = QtWidgets.QLabel(self.frame_6)
        self.txt_ph_level_ref.setStyleSheet("color: rgb(255,255,255,100);\n"
"font: 25 10pt \"Segoe UI\";")
        self.txt_ph_level_ref.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_ph_level_ref.setObjectName("txt_ph_level_ref")
        self.horizontalLayout_13.addWidget(self.txt_ph_level_ref)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.ph_container)
        self.tds_container = QtWidgets.QFrame(self.centralwidget)
        self.tds_container.setStyleSheet("#tds_container{\n"
"    \n"
"    border-image: url(:/bg/insight-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.tds_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tds_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tds_container.setObjectName("tds_container")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tds_container)
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.tds_container)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_21 = QtWidgets.QLabel(self.frame_12)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_19.addWidget(self.label_21)
        self.horizontalLayout_17.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.txt_average_tds_level = QtWidgets.QLabel(self.frame_13)
        self.txt_average_tds_level.setStyleSheet("color: rgb(255, 255, 255, 100);\n"
"font: 9pt \"Segoe UI\";")
        self.txt_average_tds_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_average_tds_level.setObjectName("txt_average_tds_level")
        self.horizontalLayout_20.addWidget(self.txt_average_tds_level)
        self.horizontalLayout_17.addWidget(self.frame_13)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.tds_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.txt_current_tds_level = QtWidgets.QLabel(self.frame_10)
        self.txt_current_tds_level.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_current_tds_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_current_tds_level.setObjectName("txt_current_tds_level")
        self.horizontalLayout_18.addWidget(self.txt_current_tds_level)
        self.label_24 = QtWidgets.QLabel(self.frame_10)
        self.label_24.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_18.addWidget(self.label_24)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.tds_container)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_20 = QtWidgets.QLabel(self.frame_11)
        self.label_20.setStyleSheet("color: rgb(255,255,255,100);\n"
"font: 25 10pt \"Segoe UI\";")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_21.addWidget(self.label_20)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.horizontalLayout_2.addWidget(self.tds_container)
        self.temp_container = QtWidgets.QFrame(self.centralwidget)
        self.temp_container.setStyleSheet("#temp_container{\n"
"    \n"
"    border-image: url(:/bg/insight-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.temp_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.temp_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp_container.setObjectName("temp_container")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.temp_container)
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.temp_container)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_19 = QtWidgets.QFrame(self.frame_14)
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_27 = QtWidgets.QLabel(self.frame_19)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_28.addWidget(self.label_27)
        self.horizontalLayout_23.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_14)
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.txt_average_temp_level = QtWidgets.QLabel(self.frame_20)
        self.txt_average_temp_level.setStyleSheet("color: rgb(255, 255, 255, 100);\n"
"font: 9pt \"Segoe UI\";")
        self.txt_average_temp_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_average_temp_level.setObjectName("txt_average_temp_level")
        self.horizontalLayout_27.addWidget(self.txt_average_temp_level)
        self.horizontalLayout_23.addWidget(self.frame_20)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.temp_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setStyleSheet("")
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_24.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.txt_current_temp_level = QtWidgets.QLabel(self.frame_17)
        self.txt_current_temp_level.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.txt_current_temp_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_current_temp_level.setObjectName("txt_current_temp_level")
        self.horizontalLayout_24.addWidget(self.txt_current_temp_level)
        self.horizontalLayout_22.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_25.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_26 = QtWidgets.QLabel(self.frame_18)
        self.label_26.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_25.addWidget(self.label_26)
        self.horizontalLayout_22.addWidget(self.frame_18)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.temp_container)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_29 = QtWidgets.QLabel(self.frame_16)
        self.label_29.setStyleSheet("color: rgb(255,255,255,100);\n"
"font: 25 10pt \"Segoe UI\";")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_26.addWidget(self.label_29)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.horizontalLayout_2.addWidget(self.temp_container)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color: rgba(255,255,255, 100);\n"
"font: 25 12pt \"Segoe UI\";\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.acid_container = QtWidgets.QFrame(self.centralwidget)
        self.acid_container.setStyleSheet("#acid_container{\n"
"    \n"
"    border-image: url(:/bg/chem-level-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.acid_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.acid_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.acid_container.setObjectName("acid_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.acid_container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_21 = QtWidgets.QFrame(self.acid_container)
        self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.bar_acid_level = QtWidgets.QProgressBar(self.frame_21)
        self.bar_acid_level.setMinimumSize(QtCore.QSize(48, 0))
        self.bar_acid_level.setMaximumSize(QtCore.QSize(16777215, 158))
        self.bar_acid_level.setStyleSheet("QProgressBar {\n"
"     border: 0;\n"
"    border-image: url(:/bg/bar-bg.png) 0 0 0 0 stretch stretch;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #14AA50;\n"
"    border: 0;\n"
"    margin: 1px;\n"
" }")
        self.bar_acid_level.setProperty("value", 50)
        self.bar_acid_level.setAlignment(QtCore.Qt.AlignCenter)
        self.bar_acid_level.setTextVisible(False)
        self.bar_acid_level.setOrientation(QtCore.Qt.Vertical)
        self.bar_acid_level.setObjectName("bar_acid_level")
        self.horizontalLayout_29.addWidget(self.bar_acid_level)
        self.verticalLayout_2.addWidget(self.frame_21)
        self.label_9 = QtWidgets.QLabel(self.acid_container)
        self.label_9.setStyleSheet("color: white;\n"
"font: 25 12pt \"Segoe UI\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.horizontalLayout_4.addWidget(self.acid_container)
        self.base_container = QtWidgets.QFrame(self.centralwidget)
        self.base_container.setStyleSheet("#base_container{\n"
"    \n"
"    border-image: url(:/bg/chem-level-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.base_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.base_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base_container.setObjectName("base_container")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.base_container)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_22 = QtWidgets.QFrame(self.base_container)
        self.frame_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.bar_base_level = QtWidgets.QProgressBar(self.frame_22)
        self.bar_base_level.setMinimumSize(QtCore.QSize(48, 0))
        self.bar_base_level.setMaximumSize(QtCore.QSize(16777215, 158))
        self.bar_base_level.setBaseSize(QtCore.QSize(0, 0))
        self.bar_base_level.setStyleSheet("QProgressBar {\n"
"     border: 0;\n"
"    border-image: url(:/bg/bar-bg.png) 0 0 0 0 stretch stretch;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #14AA50;\n"
"    border: 0;\n"
"    margin: 1px;\n"
" }")
        self.bar_base_level.setProperty("value", 24)
        self.bar_base_level.setAlignment(QtCore.Qt.AlignCenter)
        self.bar_base_level.setTextVisible(False)
        self.bar_base_level.setOrientation(QtCore.Qt.Vertical)
        self.bar_base_level.setObjectName("bar_base_level")
        self.horizontalLayout_30.addWidget(self.bar_base_level)
        self.verticalLayout_6.addWidget(self.frame_22)
        self.label_10 = QtWidgets.QLabel(self.base_container)
        self.label_10.setStyleSheet("color: white;\n"
"font: 25 12pt \"Segoe UI\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.horizontalLayout_4.addWidget(self.base_container)
        self.nutrient_a_container = QtWidgets.QFrame(self.centralwidget)
        self.nutrient_a_container.setStyleSheet("#nutrient_a_container{\n"
"    border-image: url(:/bg/chem-level-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.nutrient_a_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nutrient_a_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nutrient_a_container.setObjectName("nutrient_a_container")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.nutrient_a_container)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_23 = QtWidgets.QFrame(self.nutrient_a_container)
        self.frame_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.bar_nutrient_a_level = QtWidgets.QProgressBar(self.frame_23)
        self.bar_nutrient_a_level.setMinimumSize(QtCore.QSize(48, 0))
        self.bar_nutrient_a_level.setMaximumSize(QtCore.QSize(16777215, 158))
        self.bar_nutrient_a_level.setStyleSheet("QProgressBar {\n"
"     border: 0;\n"
"    border-image: url(:/bg/bar-bg.png) 0 0 0 0 stretch stretch;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #14AA50;\n"
"    border: 0;\n"
"    margin: 1px;\n"
" }")
        self.bar_nutrient_a_level.setProperty("value", 24)
        self.bar_nutrient_a_level.setAlignment(QtCore.Qt.AlignCenter)
        self.bar_nutrient_a_level.setTextVisible(False)
        self.bar_nutrient_a_level.setOrientation(QtCore.Qt.Vertical)
        self.bar_nutrient_a_level.setObjectName("bar_nutrient_a_level")
        self.horizontalLayout_31.addWidget(self.bar_nutrient_a_level)
        self.verticalLayout_7.addWidget(self.frame_23)
        self.label_13 = QtWidgets.QLabel(self.nutrient_a_container)
        self.label_13.setStyleSheet("color: white;\n"
"font: 25 12pt \"Segoe UI\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.horizontalLayout_4.addWidget(self.nutrient_a_container)
        self.nutrient_b_container = QtWidgets.QFrame(self.centralwidget)
        self.nutrient_b_container.setStyleSheet("#nutrient_b_container{\n"
"    border-image: url(:/bg/chem-level-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.nutrient_b_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nutrient_b_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nutrient_b_container.setObjectName("nutrient_b_container")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.nutrient_b_container)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_24 = QtWidgets.QFrame(self.nutrient_b_container)
        self.frame_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.bar_nutrient_b_level = QtWidgets.QProgressBar(self.frame_24)
        self.bar_nutrient_b_level.setMinimumSize(QtCore.QSize(48, 0))
        self.bar_nutrient_b_level.setMaximumSize(QtCore.QSize(16777215, 158))
        self.bar_nutrient_b_level.setStyleSheet("QProgressBar {\n"
"     border: 0;\n"
"    border-image: url(:/bg/bar-bg.png) 0 0 0 0 stretch stretch;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #14AA50;\n"
"    border: 0;\n"
"    margin: 1px;\n"
" }")
        self.bar_nutrient_b_level.setProperty("value", 24)
        self.bar_nutrient_b_level.setAlignment(QtCore.Qt.AlignCenter)
        self.bar_nutrient_b_level.setTextVisible(False)
        self.bar_nutrient_b_level.setOrientation(QtCore.Qt.Vertical)
        self.bar_nutrient_b_level.setObjectName("bar_nutrient_b_level")
        self.horizontalLayout_32.addWidget(self.bar_nutrient_b_level)
        self.verticalLayout_8.addWidget(self.frame_24)
        self.label_15 = QtWidgets.QLabel(self.nutrient_b_container)
        self.label_15.setStyleSheet("color: white;\n"
"font: 25 12pt \"Segoe UI\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.horizontalLayout_4.addWidget(self.nutrient_b_container)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mission Control"))
        self.txt_date.setText(_translate("MainWindow", "November 4, 2022"))
        self.label_17.setText(_translate("MainWindow", "PH Level"))
        self.txt_average_ph_level.setText(_translate("MainWindow", "Average: 7"))
        self.txt_current_ph_level.setText(_translate("MainWindow", "7.1"))
        self.txt_ph_level_ref.setText(_translate("MainWindow", "pH 7 / 5% Error"))
        self.label_21.setText(_translate("MainWindow", "TDS(ppm)"))
        self.txt_average_tds_level.setText(_translate("MainWindow", "Average: 500ppm"))
        self.txt_current_tds_level.setText(_translate("MainWindow", "1500"))
        self.label_24.setText(_translate("MainWindow", "ppm"))
        self.label_20.setText(_translate("MainWindow", "500 ppm / 5% Error"))
        self.label_27.setText(_translate("MainWindow", "TEMP(°C)"))
        self.txt_average_temp_level.setText(_translate("MainWindow", "Average: 45°C"))
        self.txt_current_temp_level.setText(_translate("MainWindow", "45"))
        self.label_26.setText(_translate("MainWindow", "°C"))
        self.label_29.setText(_translate("MainWindow", "45°C / 5% Error"))
        self.label_7.setText(_translate("MainWindow", "CHEMICAL SUPPLY LEVELS"))
        self.label_9.setText(_translate("MainWindow", "ACID"))
        self.label_10.setText(_translate("MainWindow", "BASE"))
        self.label_13.setText(_translate("MainWindow", "NUTRIENT A"))
        self.label_15.setText(_translate("MainWindow", "NUTRIENT B"))
import assets_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
