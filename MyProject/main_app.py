from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QTabWidget
import sys
from MyProject.design.mainwindow_bad_design import Ui_TabWidget
from add_note import CreateNote
from add_tasks import CreateTask
from pomo_settings import SetPomoTimer


class MainApplication(QTabWidget, Ui_TabWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_note = CreateNote()
        self.add_note_btn.clicked.connect(self.create_note.show)
        self.create_task = CreateTask()
        self.add_task.clicked.connect(self.create_task.show)
        self.set_pomo_timer = SetPomoTimer()
        self.add_timer_pomo.clicked.connect(self.set_pomo_timer.show)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainApplication()
    form.show()
    sys.exit(app.exec())
