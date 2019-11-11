# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_color.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(171, 211)
        Form.setStyleSheet("background-color:#f8f8ff;")
        self.color_yellow = QtWidgets.QPushButton(Form)
        self.color_yellow.setGeometry(QtCore.QRect(90, 20, 61, 61))
        self.color_yellow.setStyleSheet("""QPushButton 
                                            {background-color: #faf87d; 
                                            border: none; 
                                            border-radius: 30px;} 
                                            QPushButton:checked 
                                            {border: 3px solid black;}""")
        self.color_yellow.setText("")
        self.color_yellow.setObjectName("color_yellow")
        self.color_yellow.setCheckable(True)

        self.color_btn_group = QtWidgets.QButtonGroup(Form)
        self.color_btn_group.setObjectName("buttonGroup")
        self.color_btn_group.addButton(self.color_yellow)

        self.color_white = QtWidgets.QPushButton(Form)
        self.color_white.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.color_white.setStyleSheet("QPushButton {background-color: white;"
                                       "border: none; border-radius: 30px;}"
                                       "QPushButton:checked "
                                       "{border: 3px solid black;}")
        self.color_white.setText("")
        self.color_white.setAutoDefault(True)
        self.color_white.setObjectName("color_white")
        self.color_white.setCheckable(True)
        self.color_white.setChecked(True)
        self.color_btn_group.addButton(self.color_white)

        self.color_blue = QtWidgets.QPushButton(Form)
        self.color_blue.setGeometry(QtCore.QRect(20, 90, 61, 61))
        self.color_blue.setStyleSheet("QPushButton"
                                      "{background-color: lightblue;"
                                      "border: none; border-radius: 30px;}"
                                      "QPushButton:checked "
                                      "{border: 3px solid black;}")
        self.color_blue.setText("")
        self.color_blue.setCheckable(True)
        self.color_blue.setObjectName("color_blue")
        self.color_btn_group.addButton(self.color_blue)

        self.color_orange = QtWidgets.QPushButton(Form)
        self.color_orange.setGeometry(QtCore.QRect(90, 90, 61, 61))
        self.color_orange.setStyleSheet("QPushButton{background-color:#ffc966;"
                                        "border: none; border-radius: 30px;}"
                                        "QPushButton:checked "
                                        "{border: 3px solid black;}")
        self.color_orange.setCheckable(True)
        self.color_orange.setText("")
        self.color_orange.setObjectName("pushButton_4")
        self.color_btn_group.addButton(self.color_orange)

        self.color_btn = QtWidgets.QPushButton(Form)
        self.color_btn.setGeometry(QtCore.QRect(20, 165, 130, 35))
        self.color_btn.setStyleSheet("""QPushButton {background-color:  rgba(51,122,183, 0.4); 
                                border: 1px solid black;}
                   QPushButton:hover {background-color: rgba(51,122,183, 0.7);}
                   QPushButton:pressed 
                               {background-color:  rgba(51,122,183, 0.9);}""")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выбрать цвет заметки"))
        self.color_btn.setText(_translate("Form", "Установить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
