# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pomo_settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


BUTTONS_DESIGN = """QPushButton {background-color: rgba(51,122,183, 0.3); 
                                 color: black;
					             font-size: 14px; font-family: Arial;}
                    QPushButton:hover 
                                {background-color: rgba(51,122,183, 0.7);}
                    QPushButton:pressed 
                                {background-color:  rgba(51,122,183, 0.9);}"""


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(445, 424)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 35, 271, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.write_task = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.write_task.sizePolicy().hasHeightForWidth())
        self.write_task.setSizePolicy(sizePolicy)
        self.write_task.setStyleSheet("font-size: 14px; font-family: Arial;")
        self.verticalLayout.addWidget(self.write_task)

        self.pomo_duration = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.pomo_duration.setSizePolicy(sizePolicy)
        self.pomo_duration.setStyleSheet(BUTTONS_DESIGN)
        self.pomo_duration.setObjectName("pomo_duration")
        self.verticalLayout.addWidget(self.pomo_duration)

        self.break_duration = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.break_duration.sizePolicy().hasHeightForWidth())
        self.break_duration.setSizePolicy(sizePolicy)
        self.break_duration.setStyleSheet(BUTTONS_DESIGN)
        self.break_duration.setObjectName("short_duration")
        self.verticalLayout.addWidget(self.break_duration)

        self.num_of_sessions = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_of_sessions.sizePolicy().hasHeightForWidth())
        self.num_of_sessions.setSizePolicy(sizePolicy)
        self.num_of_sessions.setStyleSheet(BUTTONS_DESIGN)
        self.num_of_sessions.setObjectName("num_of_sessions")

        self.verticalLayout.addWidget(self.num_of_sessions)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)



        self.rington = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rington.sizePolicy().hasHeightForWidth())
        self.rington.setSizePolicy(sizePolicy)
        self.rington.setStyleSheet(BUTTONS_DESIGN)
        self.rington.setObjectName("rington")
        self.verticalLayout.addWidget(self.rington)

        self.save_changes_btn = QtWidgets.QPushButton('Сохранить', Form)
        self.save_changes_btn.setGeometry(170, 355, 130, 50)
        self.save_changes_btn.setStyleSheet('''QPushButton {font-size: 18px; 
        border-radius: 25px;  background-color: rgb(51,122,183); 
                                        color: white;}
                                       QPushButton:pressed 
                                        {background-color:rgb(31,101,163);}''')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки Pomo"))
        self.pomo_duration.setText(_translate("Form", f"Длительность помодоро - \n {25}min"))
        self.break_duration.setText(_translate("Form", f"Длительность перерыва - {5}min"))
        self.write_task.setPlaceholderText("Введите задачу, над которой Вам нужно работать")
        self.num_of_sessions.setText(_translate("Form", f"Количество сессий - {3}"))

        self.rington.setText(_translate("Form", "Изменить рингтон"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
