from PyQt5.QtWidgets import QWidget, QApplication
import sys
import sqlite3
from MyProject.design.dialog_time_design import Ui_Dialog
from MyProject.design.pomo_settings_design import Ui_Form
from MyProject.ringtons import GetRington

con = sqlite3.connect('other_files/my_project.db')
cur = con.cursor()
POMO_SETTINGS_INFO = cur.execute("""SELECT * FROM pomoSettings 
    WHERE id = 1""").fetchall()
con.commit()
con.close()


class SetPomoTimer(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_pomo_duration = SetPomoDuration(self.pomo_duration)
        self.pomo_duration.clicked.connect(self.set_pomo_duration.show)
        self.set_break_duration = SetBreakDuration(self.break_duration)
        self.break_duration.clicked.connect(self.set_break_duration.show)
        self.set_sessions_count = SetSessionsCount(self.num_of_sessions)
        self.num_of_sessions.clicked.connect(self.set_sessions_count.show)
        self.get_rington = GetRington(POMO_SETTINGS_INFO[0][4])
        self.rington.clicked.connect(self.get_rington.show)
        self.save_changes_btn.clicked.connect(self.save_changes)

        self.write_task.setPlainText(POMO_SETTINGS_INFO[0][5])

    def save_changes(self):
        self.rington_path = str(self.get_rington.get_rington())
        self.sessions_count = int(
            self.set_sessions_count.return_sessions_value())
        self.break_duration_value = int(
            self.set_break_duration.return_break_value())
        self.task_text = str(self.write_task.toPlainText())
        self.pomo_duration_value = int(
            self.set_pomo_duration.return_pomo_value())

        con = sqlite3.connect('other_files/my_project.db')
        cur = con.cursor()
        cur.execute(f"""UPDATE pomoSettings 
        SET pomoDuration = {self.pomo_duration_value},
            breakDuration = {self.break_duration_value},
            sessions = {self.sessions_count}, rington = '{self.rington_path}',
            text = '{self.task_text}' WHERE id = 1""")
        con.commit()
        con.close()
        self.close()


class SetBreakDuration(QWidget, Ui_Dialog):
    break_duration_value = POMO_SETTINGS_INFO[0][2]

    def __init__(self, text=None):
        super().__init__()
        self.setupUi(self)
        self.text = text
        self.set_duration.setMinimum(2)
        self.set_duration.setMaximum(15)
        self.text.setText(f"Длительность перерыва - "
                          f"{self.return_break_value()}min")

        self.set_duration.setValue(SetBreakDuration.break_duration_value)
        self.set_duration.valueChanged.connect(self.show_duration.display)
        self.buttonBox.accepted.connect(self.func_accepted)
        self.show_duration.display(SetBreakDuration.break_duration_value)

    def func_accepted(self):
        SetBreakDuration.break_duration_value = int(self.show_duration.value())
        self.text.setText(f"Длительность перерыва - "
                          f"{self.return_break_value()}min")
        self.close()

    def return_break_value(self):
        return SetBreakDuration.break_duration_value


class SetPomoDuration(QWidget, Ui_Dialog):
    pomo_duration_value = POMO_SETTINGS_INFO[0][1]

    def __init__(self, text=None):
        super().__init__()
        self.setupUi(self)
        self.text = text
        self.text.setText(f"Длительность помодоро - \n "
                          f"{self.return_pomo_value()}min")

        self.set_duration.setValue(SetPomoDuration.pomo_duration_value)
        self.set_duration.valueChanged.connect(self.show_duration.display)
        self.buttonBox.accepted.connect(self.func_accepted)
        self.show_duration.display(SetPomoDuration.pomo_duration_value)

    def func_accepted(self):
        SetPomoDuration.pomo_duration_value = int(self.show_duration.value())
        self.text.setText(f"Длительность помодоро - \n "
                          f"{self.return_pomo_value()}min")
        self.close()

    def return_pomo_value(self):
        return SetPomoDuration.pomo_duration_value


class SetSessionsCount(QWidget, Ui_Dialog):
    value_of_sessions = POMO_SETTINGS_INFO[0][3]

    def __init__(self, text=None):
        super().__init__()
        self.setupUi(self)
        self.text = text
        self.set_duration.setMinimum(1)
        self.set_duration.setMaximum(5)
        self.text.setText(
            f"Количество сессий - {self.return_sessions_value()}")
        self.set_duration.setValue(SetSessionsCount.value_of_sessions)
        self.set_duration.valueChanged.connect(self.show_duration.display)
        self.buttonBox.accepted.connect(self.func_accepted)
        self.show_duration.display(SetSessionsCount.value_of_sessions)

    def func_accepted(self):
        SetSessionsCount.value_of_sessions = int(self.show_duration.value())
        self.text.setText(
            f"Количество сессий - {self.return_sessions_value()}")
        self.close()

    def return_sessions_value(self):
        return SetSessionsCount.value_of_sessions


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = SetPomoTimer()
    form.show()
    sys.exit(app.exec())
