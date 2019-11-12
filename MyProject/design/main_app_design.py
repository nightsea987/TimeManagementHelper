# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


BUTTON_DESIGN = """QPushButton {font-size: 30px; 
                                        border-radius: 35px; 
                                        background-color: rgb(51,122,183); 
                                        color: white;
background-attachment: fixed;}
                                       QPushButton:pressed 
                                        {background-color:rgb(31,101,163);}"""
BUTTON_DESIGN2 = """QPushButton {background-color:  rgba(51,122,183, 0.3); 
                       color: black;
					   font-size: 14px; font-family: Arial;}
QPushButton:hover {background-color:  rgba(51,122,183, 0.7);}
QPushButton:pressed {background-color:  rgba(51,122,183, 0.9);}"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(598, 448)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        TabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        TabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        TabWidget.setStyleSheet("QPushButton {font-size: 30px; \n"
"                                        border-radius: 35px; \n"
"                                        background-color: rgb(51,122,183); \n"
"                                        color: white;}\n"
"                                       QPushButton:pressed \n"
"                                        {background-color:rgb(31,101,163);}")
        TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        TabWidget.setIconSize(QtCore.QSize(16, 16))
        TabWidget.setElideMode(QtCore.Qt.ElideNone)

        self.notes_window = QtWidgets.QWidget()
        self.notes_window.setObjectName("tab")
        self.main_layout = QtWidgets.QGridLayout(self)
        self.main_layout.setContentsMargins(20, 20, 10, 10)

        self.add_note_btn = QtWidgets.QPushButton(self.notes_window)
        self.add_note_btn.setGeometry(QtCore.QRect(500, 330, 71, 71))
        self.add_note_btn.setStyleSheet(BUTTON_DESIGN)
        self.add_note_btn.setObjectName("add_note_btn")

        TabWidget.addTab(self.notes_window, "")


        self.pomodoro_window = QtWidgets.QWidget()
        self.pomodoro_window.setObjectName("pomodoro_window")

        self.timer_pomo = QtWidgets.QLCDNumber(self.pomodoro_window)
        self.timer_pomo.setGeometry(QtCore.QRect(150, 150, 271, 61))
        self.timer_pomo.setStyleSheet("color:  rgb(51,122,183);")


        self.add_timer_pomo = QtWidgets.QPushButton(self.pomodoro_window)
        self.add_timer_pomo.setGeometry(QtCore.QRect(500, 330, 71, 71))
        self.add_timer_pomo.setStyleSheet("font-size: 25px; border-color: black; font-size: 30px;")
        self.add_timer_pomo.setObjectName("add_timer_pomo")

        self.exit_from_process_btn = QtWidgets.QPushButton('Выход', self.pomodoro_window)
        self.exit_from_process_btn.setGeometry(QtCore.QRect(230, 300, 111, 51))
        self.exit_from_process_btn.setStyleSheet('QPushButton {border: none; '
                                                 'font-size: 16px; color: grey;'
                                                 'background-color: white;}'
                                                 'QPushButton:hover '
                                                 '{color: dimgray;}'
                                                 'QPushButton:pressed '
                                                 '{color: black;}')

        self.pomo_label = QtWidgets.QLabel(self.pomodoro_window, alignment=Qt.AlignCenter)
        self.pomo_label.setGeometry(QtCore.QRect(150, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pomo_label.setFont(font)
        self.pomo_label.setObjectName("pomo_label")

        self.start_pomo_btn = QtWidgets.QPushButton('Старт', self.pomodoro_window)
        self.start_pomo_btn.setGeometry(QtCore.QRect(222, 250, 128, 51))
        self.start_pomo_btn.setStyleSheet('font-size: 18px; '
                                          'border-radius: 25px;')

        self.about_pomodoro = QtWidgets.QPushButton(self.pomodoro_window)
        self.about_pomodoro.setGeometry(510, 15, 65, 65)
        self.about_pomodoro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_pomodoro.setStyleSheet(
            'QPushButton {border-radius: 17px; background-color: white; image: url(other_files/pomo.png)};'
            'QPushButton:pressed {background-color: rgba(51,122,183, 0.3)};')
        self.about_pomodoro.setToolTip('О технике Pomodoro')
        TabWidget.addTab(self.pomodoro_window, "")


        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Десктопное приложение для тайм менеджмента"))
        self.add_note_btn.setText(_translate("TabWidget", "+"))



        self.add_timer_pomo.setText(_translate("TabWidget", "+"))
        self.pomo_label.setText(_translate("TabWidget", "Добавить таймер помодоро"))
        TabWidget.setTabText(TabWidget.indexOf(self.pomodoro_window), _translate("TabWidget", "Pomodoro"))

        TabWidget.setTabText(TabWidget.indexOf(self.notes_window), _translate("TabWidget", "Заметки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
