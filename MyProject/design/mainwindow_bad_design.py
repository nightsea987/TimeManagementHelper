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
from PyQt5.QtGui import QPalette


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(598, 453)
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

        self.tasks_window = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasks_window.sizePolicy().hasHeightForWidth())
        self.tasks_window.setSizePolicy(sizePolicy)
        self.tasks_window.setObjectName("tasks_window")
        self.tasks_calendar = QtWidgets.QCalendarWidget(self.tasks_window)
        self.tasks_calendar.setGeometry(QtCore.QRect(0, 0, 591, 183))
        self.tasks_calendar.setObjectName("tasks_calendar")
        print(QDate.currentDate())
        self.tasks_calendar.setMinimumDate(QDate.currentDate())

        self.add_task = QtWidgets.QPushButton(self.tasks_window)
        self.add_task.setGeometry(QtCore.QRect(500, 330, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_task.sizePolicy().hasHeightForWidth())
        self.add_task.setSizePolicy(sizePolicy)
        self.add_task.setStyleSheet(BUTTON_DESIGN)
        self.add_task.setObjectName("add_task")
        self.groupBox = QtWidgets.QGroupBox(self.tasks_window)
        self.groupBox.setGeometry(QtCore.QRect(40, 230, 511, 91))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(30, 20, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("border: none;")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 20, 31, 20))
        self.pushButton_4.setStyleSheet(BUTTON_DESIGN2)
        self.pushButton_4.setObjectName("pushButton_4")
        TabWidget.addTab(self.tasks_window, "")
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
        self.start_pomo_btn.setGeometry(QtCore.QRect(225, 250, 122, 51))
        self.start_pomo_btn.setStyleSheet('font-size: 18px; '
                                          'border-radius: 25px;')
        TabWidget.addTab(self.pomodoro_window, "")

        self.settings_window = QtWidgets.QWidget()
        self.settings_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.settings_window.setObjectName("settings_window")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.settings_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 70, 243, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.change_theme_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_theme_btn.sizePolicy().hasHeightForWidth())
        self.change_theme_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.change_theme_btn.setFont(font)
        self.change_theme_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_theme_btn.setStyleSheet(BUTTON_DESIGN2)
        self.change_theme_btn.setObjectName("change_theme_btn")
        self.verticalLayout.addWidget(self.change_theme_btn)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.change_font_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_font_btn.sizePolicy().hasHeightForWidth())
        self.change_font_btn.setSizePolicy(sizePolicy)
        self.change_font_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_font_btn.setStyleSheet(BUTTON_DESIGN2)
        self.change_font_btn.setObjectName("change_font_btn")
        self.verticalLayout.addWidget(self.change_font_btn)

        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

        self.about_pomodoro = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_pomodoro.sizePolicy().hasHeightForWidth())
        self.about_pomodoro.setSizePolicy(sizePolicy)
        self.about_pomodoro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_pomodoro.setStyleSheet(BUTTON_DESIGN2)
        self.about_pomodoro.setObjectName("about_pomodoro")
        self.verticalLayout.addWidget(self.about_pomodoro)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)

        self.about_project = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_project.sizePolicy().hasHeightForWidth())
        self.about_project.setSizePolicy(sizePolicy)
        self.about_project.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_project.setStyleSheet(BUTTON_DESIGN2)
        self.about_project.setObjectName("about_project")
        self.verticalLayout.addWidget(self.about_project)

        TabWidget.addTab(self.settings_window, "")
        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.add_note_btn.setText(_translate("TabWidget", "+"))


        self.add_task.setText(_translate("TabWidget", "+"))
        self.groupBox.setTitle(_translate("TabWidget", "Группа1"))
        self.checkBox.setText(_translate("TabWidget", "Создать проект"))
        self.pushButton_4.setText(_translate("TabWidget", "..."))
        TabWidget.setTabText(TabWidget.indexOf(self.tasks_window), _translate("TabWidget", "Задачи"))
        self.add_timer_pomo.setText(_translate("TabWidget", "+"))
        self.pomo_label.setText(_translate("TabWidget", "Добавить таймер помодоро"))
        TabWidget.setTabText(TabWidget.indexOf(self.pomodoro_window), _translate("TabWidget", "Pomodoro"))
        self.change_theme_btn.setText(_translate("TabWidget", "Изменить тему программы"))
        self.change_font_btn.setText(_translate("TabWidget", "Изменить шрифт"))
        self.about_pomodoro.setText(_translate("TabWidget", "О технике Pomodoro"))
        self.about_project.setText(_translate("TabWidget", "О проекте"))
        TabWidget.setTabText(TabWidget.indexOf(self.settings_window), _translate("TabWidget", "Настройки"))
        TabWidget.setTabText(TabWidget.indexOf(self.notes_window), _translate("TabWidget", "Заметки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
