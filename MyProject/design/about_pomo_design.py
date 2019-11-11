# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_pomo.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScrollArea(object):
    def setupUi(self, ScrollArea):
        ScrollArea.setObjectName("ScrollArea")
        ScrollArea.setEnabled(True)
        ScrollArea.resize(598, 454)
        ScrollArea.setStyleSheet("background-color: white;")
        ScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 596, 452))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.about_pomo_text = \
            QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.about_pomo_text.setGeometry(QtCore.QRect(0, 0, 601, 451))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.about_pomo_text.setFont(font)
        self.about_pomo_text.setStyleSheet("padding: 15px 10px 15px 10px; ")
        self.about_pomo_text.setObjectName("plainTextEdit")
        self.about_pomo_text.setReadOnly(True)
        ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ScrollArea)
        QtCore.QMetaObject.connectSlotsByName(ScrollArea)

    def retranslateUi(self, ScrollArea):
        _translate = QtCore.QCoreApplication.translate
        ScrollArea.setWindowTitle(_translate("ScrollArea", "О Pomodoro"))
        self.about_pomo_text.setPlainText(_translate("ScrollArea",
                                                     "       Одной"
" из ключевых техник тайм-менеджмента является техника Pomodoro. "
"В том или ином виде о ней слышали многие, но общего понимания, что она из "
"себя представляет, нет ни у кого.\n"
"\n"
"      Зачем это нужно\n"
"\n"
"      В эпоху постоянных отвлечений, когда всё делается с целью заманить и "
"обратить на себя ваше внимание, управлять своим временем очень важно. "
"Используя технику Pomodoro или другую альтернативную методику, вы "
"увеличиваете свою продуктивность, делая больше за меньшее время.\n"
"\n"
"      Основные цели  Pomodoro состоят в следующем:\n"
"\n"
"1.  Поддержка решимости достигать собственных целей.\n"
"2.  Улучшение рабочего и учебного процесса.\n"
"3.  Увеличение эффективности работы и учёбы.\n"
"4.  Развитие решимости действовать в сложных ситуациях.\n"
"\n"
"     Суть техники Pomodoro\n"
"\n"
"       Отрезки времени, на которые делится работа, условно называются "
"помидорами. Один «помидор» длится от 30 минут: 25 минут работы и 5 минут "
"отдыха. Чуть ли не каждый год появляются новые исследования, рассказывающие "
"об эффективности других временных отрезков, но для наглядности лучше взять "
"за основу первоначальную технику.\n"
"      Перед запуском таймера вы должны составить список рабочих задач. "
"Возьмите лист бумаги и озаглавьте его «Задачи на сегодня». Учитывая "
"приоритеты (от более к менее важным), составьте список всех задач на сегодня."
        " После этого установите таймер на 25 минут и начинайте работать.\n"
"      Звонок таймера означает наступление 5-минутного отдыха. В это время "
"нежелательно заниматься рабочими делами и лучше расслабиться и отвлечься от "
"работы. По прошествии 5 минут нужно вернуться к задаче и продолжить её "
"выполнение. Закончив работать над задачей, вычеркните её из списка и "
                    "принимайтесь за следующую.\n"
"      Ведение списка задач нужно для самоконтроля и наблюдения за "
                                                     "своей эффективностью. \n"
"\n"
"                                                          источник: "
"https://lifehacker.ru/all-about-pomodoro/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScrollArea = QtWidgets.QScrollArea()
    ui = Ui_ScrollArea()
    ui.setupUi(ScrollArea)
    ScrollArea.show()
    sys.exit(app.exec_())
