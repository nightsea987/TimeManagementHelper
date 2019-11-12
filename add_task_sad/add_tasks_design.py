# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_tasks.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate


BUTTONS_DESIGN = """QPushButton {background-color: rgba(51,122,183, 0.5); 
                                 color: black;
					             font-size: 13px; font-family: Arial;}
                    QPushButton:hover 
                                {background-color: rgba(51,122,183, 0.7);}
                    QPushButton:pressed 
                                {background-color:  rgba(51,122,183, 0.9);}"""


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 388)
        self.task_name = QtWidgets.QPlainTextEdit(Form)
        self.task_name.setGeometry(QtCore.QRect(30, 20, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.task_name.setFont(font)
        self.task_name.setObjectName("task_name")
        self.create_task_btn = QtWidgets.QPushButton(Form)
        self.create_task_btn.setGeometry(QtCore.QRect(430, 330, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.create_task_btn.setFont(font)
        self.create_task_btn.setStyleSheet(BUTTONS_DESIGN)

        self.task_description = QtWidgets.QPlainTextEdit(Form)
        self.task_description.setGeometry(QtCore.QRect(30, 80, 471, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.task_description.setFont(font)
        self.task_description.setObjectName("task_description")

        self.settings_widget = QtWidgets.QWidget(Form)
        self.settings_widget.setGeometry(QtCore.QRect(450, 70, 121, 81))
        self.settings_widget.setStyleSheet("background: white;")
        self.settings_widget.setObjectName("widget")

        self.create_tasks_group_btn = QtWidgets.QPushButton(self.settings_widget)
        self.create_tasks_group_btn.setGeometry(QtCore.QRect(0, 0, 121, 41))
        self.create_tasks_group_btn.setStyleSheet(BUTTONS_DESIGN)
        self.create_tasks_group_btn.setObjectName("create_tasks_group_btn")

        self.add_reminder_btn = QtWidgets.QPushButton(self.settings_widget)
        self.add_reminder_btn.setGeometry(QtCore.QRect(0, 40, 121, 41))
        self.add_reminder_btn.setStyleSheet(BUTTONS_DESIGN)
        self.add_reminder_btn.setObjectName("add_reminder_btn")
        self.settings_widget.hide()

        self.set_tasks_group = QtWidgets.QComboBox(Form)
        self.set_tasks_group.setGeometry(QtCore.QRect(200, 230, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.set_tasks_group.setFont(font)
        self.set_tasks_group.setObjectName("set_tasks_group")


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 230, 151, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet('font-size: 12px; font-family: "Arial"')

        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(200, 280, 301, 31))
        self.dateEdit.setStyleSheet("background-color: white;")
        self.dateEdit.setObjectName("dateEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 290, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('font-size: 12px; font-family: "Arial"')

        self.task_settings = QtWidgets.QPushButton(Form)
        self.task_settings.setGeometry(QtCore.QRect(520, 20, 51, 51))
        self.task_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.task_settings.setStyleSheet(BUTTONS_DESIGN)
        self.task_settings.setObjectName("task_settings")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Создание задачи"))
        self.task_name.setPlaceholderText(_translate("Form", "Введите задачу"))
        self.create_task_btn.setText(_translate("Form", "Создать"))
        self.task_description.setPlaceholderText(_translate("Form", "Введите описание задачи"))
        self.create_tasks_group_btn.setText(_translate("Form", "Создать группу\n"
" задач"))
        self.add_reminder_btn.setText(_translate("Form", "Добавить\n"
" напоминание"))

        self.label.setText(_translate("Form", "Выберите группу задач"))
        self.label_2.setText(_translate("Form", "Выберите дату"))
        self.task_settings.setText(_translate("Form", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
