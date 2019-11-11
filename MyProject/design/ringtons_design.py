# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ringtons.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(316, 415)
        Form.setStyleSheet("QRadioButton {font-size: 14px;}")
        self.set_rington_settings = QtWidgets.QPushButton(Form)
        self.set_rington_settings.setGeometry(QtCore.QRect(90, 330, 141, 51))
        self.set_rington_settings.setStyleSheet("QPushButton {font-size: 18px; "
                    "border-radius: 25px;background-color: rgb(51,122,183); \n"
"                                        color: white;}\n"
"                                       QPushButton:pressed \n"
"                                        {background-color:rgb(31,101,163);}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 30, 181, 271))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.melody1 = QtWidgets.QRadioButton(self.widget)
        self.melody1.setObjectName("melody1")
        self.melody1.setChecked(True)

        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.melody1)
        self.gridLayout.addWidget(self.melody1, 0, 0, 1, 1)
        self.melody2 = QtWidgets.QRadioButton(self.widget)
        self.melody2.setObjectName("melody2")
        self.buttonGroup.addButton(self.melody2)
        self.gridLayout.addWidget(self.melody2, 1, 0, 1, 1)
        self.melody3 = QtWidgets.QRadioButton(self.widget)
        self.melody3.setObjectName("melody3")
        self.buttonGroup.addButton(self.melody3)
        self.gridLayout.addWidget(self.melody3, 2, 0, 1, 1)
        self.melody4 = QtWidgets.QRadioButton(self.widget)
        self.melody4.setObjectName("melody4")
        self.buttonGroup.addButton(self.melody4)
        self.gridLayout.addWidget(self.melody4, 3, 0, 1, 1)
        self.melody5 = QtWidgets.QRadioButton(self.widget)
        self.buttonGroup.addButton(self.melody5)
        self.gridLayout.addWidget(self.melody5, 4, 0, 1, 1)
        self.melodies_lst = self.buttonGroup.buttons()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Установить рингтон"))
        self.set_rington_settings.setText(_translate("Form", "Установить"))
        self.melody1.setText(_translate("Form", "Мелодия 1"))
        self.melody2.setText(_translate("Form", "Мелодия 2"))
        self.melody3.setText(_translate("Form", "Мелодия 3"))
        self.melody4.setText(_translate("Form", "Мелодия 4"))
        self.melody5.setText(_translate("Form", "Мелодия 5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
