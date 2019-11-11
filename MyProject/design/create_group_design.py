# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creategroup.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

GROUPS_COLOR_DC = {'Коричневый': '#a65e2e', 'Красный': '#ff2b2b',
                                'Розовый': '#e60548', 'Фиолетовый': '#7000cc',
                                'Синий': '#1889ab', 'Зеленый': '#009900'}
COLOR_LST = [i for i in GROUPS_COLOR_DC.keys()]


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 232)
        self.line_error = QtWidgets.QLabel('Пропущено данное поле', Form)
        self.line_error.move(245, 2)
        self.line_error.resize(200, 30)
        self.line_error.setStyleSheet('font-size: 14px; color: red;')

        self.group_name = QtWidgets.QLineEdit(Form)
        self.group_name.setGeometry(QtCore.QRect(220, 30, 221, 41))
        self.group_name.setStyleSheet('font-size: 13px; padding-left: 3px;')

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(220, 90, 221, 41))
        self.comboBox.setObjectName("comboBox")


        for i in range(6):
            self.comboBox.addItem(COLOR_LST[i])
            self.comboBox.setItemData(i, QColor(
                GROUPS_COLOR_DC[COLOR_LST[i]]), Qt.BackgroundRole)


        self.save_group_btn = QtWidgets.QPushButton(Form)
        self.save_group_btn.setGeometry(QtCore.QRect(110, 160, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.save_group_btn.setFont(font)
        self.save_group_btn.setStyleSheet("QPushButton {background-color:  rgba(51,122,183, 0.3); \n"
"                       color: black;\n"
"                       font-size: 14px; font-family: Arial;}\n"
"QPushButton:hover {background-color:  rgba(51,122,183, 0.7);}\n"
"QPushButton:pressed {background-color:  rgba(51,122,183, 0.9);}")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Создать группу"))
        self.label.setText(_translate("Form", "Введите название"))
        self.label_2.setText(_translate("Form", "Выберите цвет группы"))
        self.save_group_btn.setText(_translate("Form", "Добавить группу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
