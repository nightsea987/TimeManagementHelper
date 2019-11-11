# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


BUTTON_DESIGN = """QPushButton {background-color:  rgba(51,122,183, 0.4); 
                                border: 1px solid black;}
                   QPushButton:hover {background-color: rgba(51,122,183, 0.7);}
                   QPushButton:pressed 
                               {background-color:  rgba(51,122,183, 0.9);}"""
TEXT_NOTE_DESIGN_WHITE = """padding-left: 30px; padding-right: 30px; 
                    background-color: #fff; font-size: 14px;"""
TEXT_NOTE_DESIGN_YELLOW = """padding-left: 30px; padding-right: 30px; 
                    background-color: #faf87d; font-size: 14px;"""
TEXT_NOTE_DESIGN_BLUE = """padding-left: 30px; padding-right: 30px; 
                    background-color: #ADD8E6; font-size: 14px;"""
TEXT_NOTE_DESIGN_ORANGE = """padding-left: 30px; padding-right: 30px; 
                    background-color: #ffc966; font-size: 14px;"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(595, 422)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 591, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.text_note_edit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.text_note_edit.setGeometry(QtCore.QRect(0, 0, 591, 361))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.text_note_edit.setFont(font)
        self.text_note_edit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text_note_edit.setMouseTracking(False)
        self.text_note_edit.setStyleSheet("padding-left: 30px; "
                                          "padding-right: 30px; "
                                          "padding-top: 5px;"
                                          "background-color: white;")
        self.text_note_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_note_edit.setObjectName("text_note_edit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontComboBox.setGeometry(QtCore.QRect(270, 10, 161, 41))
        self.fontComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fontComboBox.setObjectName("fontComboBox")
        self.open_file_btn = QtWidgets.QPushButton(Form)
        self.open_file_btn.setGeometry(QtCore.QRect(10, 10, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.open_file_btn.setFont(font)
        self.open_file_btn.setStyleSheet(BUTTON_DESIGN)
        self.open_file_btn.setObjectName("open_file_btn")
        self.save_note_btn = QtWidgets.QPushButton(Form)
        self.save_note_btn.setGeometry(QtCore.QRect(90, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.save_note_btn.setFont(font)
        self.save_note_btn.setStyleSheet(BUTTON_DESIGN)
        self.save_note_btn.setObjectName("save_note_btn")
        self.font_size_box = QtWidgets.QComboBox(Form)
        self.font_size_box.setGeometry(QtCore.QRect(440, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.font_size_box.setFont(font)
        self.font_size_box.setStyleSheet("QComboBox {background-color:   "
            "rgba(51,122,183, 0.5); border: 1px solid grey;}\n"
"QComboBox:hover { border: 1px solid black;}\n"
"QComboBox::drop-down { border: none; }\n"
"QComboBox::drop-down:hover {border: 1px solid rgba(51,122,183, 0.3);\n"
"               background-color:   rgba(51,122,183, 0.2)}\n"
"QComboBox::down-arrow\n"
"{\n"
"        image: url(other_files/arrow-down2_78573.png);\n"
"        width: 20px;\n"
"            height: 24px;\n"
"}")
        self.font_size_box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.lst = [str(i) for i in range(12, 31, 2)]
        for i in self.lst:
            self.font_size_box.addItem(i)

        self.get_color_btn = QtWidgets.QPushButton(Form)
        self.get_color_btn.setGeometry(QtCore.QRect(510, 10, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.get_color_btn.setFont(font)
        self.get_color_btn.setStyleSheet(BUTTON_DESIGN)
        self.get_color_btn.setObjectName("get_color_btn")
        self.del_note_btn = QtWidgets.QPushButton(Form)
        self.del_note_btn.setGeometry(QtCore.QRect(180, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.del_note_btn.setFont(font)
        self.del_note_btn.setStyleSheet(BUTTON_DESIGN)
        self.del_note_btn.setObjectName("del_note_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить заметку"))

        self.open_file_btn.setText(_translate("Form", "Открыть\n"
" файл"))
        self.save_note_btn.setText(_translate("Form", "Сохранить\n"
" заметку"))
        self.get_color_btn.setText(_translate("Form", "Цвет \n"
"заметки"))
        self.del_note_btn.setText(_translate("Form", "Удалить \n"
" заметку"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
