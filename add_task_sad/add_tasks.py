from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QColor
import sys
import sqlite3
from add_task_sad.add_tasks_design import Ui_Form
from create_group import CreateGroup

GROUPS_COLOR_DC = {'Коричневый': '#a65e2e', 'Красный': '#ff2b2b',
                                'Розовый': '#e60548', 'Фиолетовый': '#7000cc',
                                'Синий': '#1889ab', 'Зеленый': '#009900'}


class CreateTask(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_group_info()
        self.create_tasks_group_btn.clicked.connect(self.create_group_func)

        self.clicked_count = 0
        self.task_settings.clicked.connect(self.task_settings_clicked)
        self.create_task_btn.clicked.connect(self.save_task_to_bd)
        self.date = QDate.currentDate()
        self.dateEdit.setDate(self.date)

    def create_group_func(self):
        self.create_group = CreateGroup(self.add_group_info)
        self.create_group.show()

    def task_settings_clicked(self):
        self.clicked_count += 1
        if self.clicked_count % 2 == 0:
            self.settings_widget.hide()
        else:
            self.settings_widget.show()

    def add_group_info(self):
        con = sqlite3.connect('my_project.db')
        cur = con.cursor()
        self.groups_info = cur.execute(f"""SELECT * FROM groups""").fetchall()
        con.commit()
        con.close()

        self.set_tasks_group.clear()
        for i in range(len(self.groups_info)):
            self.set_tasks_group.addItem(self.groups_info[i][1])
            self.set_tasks_group.setItemData(i, QColor(
                GROUPS_COLOR_DC[self.groups_info[i][2]]), Qt.BackgroundRole)

    def save_task_to_bd(self):

        print(self.task_name.toPlainText(), self.task_description.toPlainText(),
              self.set_tasks_group.currentText(), self.dateEdit.text())

        con = sqlite3.connect('my_project.db')
        cur = con.cursor()
        #cur.execute(f"""INSERT INTO tasks(title, description,
        #group, date) VALUES ('{self.task_name.toPlainText()}',
        #'{self.task_description.toPlainText()}', '{self.set_tasks_group.currentText()}',
        #'{self.dateEdit.text()}')""")
        con.commit()
        con.close()

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CreateTask()
    form.show()
    sys.exit(app.exec())
