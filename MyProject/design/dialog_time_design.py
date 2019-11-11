# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_time.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 152)
        Dialog.setStyleSheet("")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 311, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.set_duration = QtWidgets.QSlider(Dialog)
        self.set_duration.setGeometry(QtCore.QRect(30, 50, 221, 22))
        self.set_duration.setOrientation(QtCore.Qt.Horizontal)
        self.set_duration.setObjectName("set_duration")
        self.set_duration.setMinimum(2)
        self.set_duration.setMaximum(55)
        self.set_duration.setValue(25)

        self.show_duration = QtWidgets.QLCDNumber(Dialog)
        self.show_duration.setEnabled(True)
        self.show_duration.setGeometry(QtCore.QRect(275, 40, 75, 45))
        self.show_duration.setObjectName("show_duration")
        self.show_duration.display(25)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настроить длительность"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
