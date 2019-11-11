from PyQt5.QtWidgets import QApplication, QTabWidget, QPlainTextEdit, \
    QScrollArea, QGridLayout, QWidget
from PyQt5.QtCore import QSize, Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import sys
from MyProject.design.main_app_design import Ui_TabWidget
from MyProject.add_note import CreateNote, EditNote
from MyProject.pomo_settings import SetPomoTimer
from MyProject.design.about_pomo_design import Ui_ScrollArea
import sqlite3

BASIC_DESIGN = """padding: 10px 5px 10px 5px; font-size: 13px;"""


class QPlainTextWithID(QPlainTextEdit):
    def __init__(self, text, parent, id):
        super().__init__(parent)
        self.id = id
        self.setPlainText(text)


class MainApplication(QTabWidget, Ui_TabWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_note_btn.clicked.connect(self.create_note_func)

        self.scroll_area = QScrollArea(self.notes_window)
        self.notes_widget = QWidget(self)
        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(20, 20, 10, 10)

        self.add_notes()

        self.set_pomo_timer = SetPomoTimer()
        self.add_timer_pomo.clicked.connect(self.set_pomo_timer.show)

        self.exit_from_process_btn.setDisabled(True)
        self.exit_from_process_btn.setVisible(False)

        self.is_break, self.time_left, self.current_time = False, '', 0
        self.count = 0
        self.player = QMediaPlayer()

        self.pomo_timer = QTimer(self)
        self.pomo_timer.timeout.connect(self.pomo_timer_timeout)
        self.start_pomo_btn.setText('Старт')
        self.start_pomo_btn.clicked.connect(self.start_pomo)

        self.about_pomo = AboutPomoWindow()
        self.about_pomodoro.clicked.connect(self.about_pomo.show)

    def create_note_func(self):
        self.create_note = CreateNote(self.add_notes)
        self.create_note.show()

    def edit_note_func(self, current_note_id):
        self.edit_note = EditNote(current_note_id, self.add_notes)
        self.edit_note.show()

    def add_info(self):
        con = sqlite3.connect('other_files/my_project.db')
        cur = con.cursor()
        self.notes_info = cur.execute("""SELECT * FROM notes""").fetchall()
        con.commit()
        con.close()

    def update_notes(self):
        self.main_layout.update()
        for i in range(self.main_layout.count() - 1, -1, -1):
            self.main_layout.itemAt(i).widget().setParent(None)

    def add_notes(self):
        self.add_info()
        self.update_notes()
        for i in range(len(self.notes_info)):
            self.note_id = self.notes_info[i][0]
            self.text = self.notes_info[i][1][:130]
            if len(self.notes_info[i][1]) < 130:
                self.note = QPlainTextWithID(self.text, self, self.note_id)
            else:
                self.note = QPlainTextWithID(self.text + ' ...', self,
                                             self.note_id)
            self.note.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.note.setStyleSheet(BASIC_DESIGN +
                                f'background-color: {self.notes_info[i][4]};')
            self.note.setMinimumSize(QSize(170, 160))
            self.note.setMaximumSize(QSize(170, 160))
            self.note.setReadOnly(True)

            self.note.selectionChanged.connect(self.dblClickNote)

            self.main_layout.addWidget(self.note, i // 3, i % 3, 1, 1)
            self.notes_widget.setGeometry(10, 10, 551, (i // 3 + 1) * 170 + 14)

        self.notes_widget.setLayout(self.main_layout)
        self.notes_widget.setStyleSheet('background-color: white;')
        self.notes_widget.updateGeometry()

        self.scroll_area.setWidget(self.notes_widget)
        self.scroll_area.setGeometry(10, 20, 571, 391)
        self.scroll_area.setStyleSheet('background-color: white;')

        self.add_note_btn.raise_()

    def dblClickNote(self):
        self.edit_note_func(self.sender().id)

    def add_pomo_info(self):
        con = sqlite3.connect('other_files/my_project.db')
        cur = con.cursor()
        self.pomo_info = cur.execute("""SELECT * FROM pomoSettings 
            WHERE id = 1""").fetchall()
        con.commit()
        con.close()

    def start_pomo(self):
        self.add_pomo_info()
        self.player.setMedia(QMediaContent(QUrl(self.pomo_info[0][4])))
        self.start_pomo_btn.setText('Старт')
        self.start_pomo_btn.setDisabled(False)

        if self.is_break is False:
            self.current_duration = self.pomo_info[0][1] * 60
            self.timer_pomo.setStyleSheet('color: rgb(51,122,183)')
        else:
            self.current_duration = self.pomo_info[0][2] * 60
            self.timer_pomo.setStyleSheet('color: #50c878;')

        self.current_time = self.current_duration
        minuts, seconds = divmod(self.current_time, 60)
        self.time_left = str(minuts).zfill(2) + ':' + str(seconds).zfill(2)

        self.pomo_timer.start(1000)

        if self.pomo_info[0][5] == '':
            self.pomo_label.setText('Stay focused')
        else:
            self.pomo_label.setText(self.pomo_info[0][5])

        self.update_gui()

    def pomo_timer_timeout(self):
        self.current_time -= 1
        minuts, seconds = divmod(self.current_time, 60)
        self.time_left = str(minuts).zfill(2) + ':' + str(seconds).zfill(2)

        self.start_pomo_btn.setDisabled(True)
        self.exit_from_process_btn.setDisabled(False)
        self.exit_from_process_btn.setVisible(True)
        self.exit_from_process_btn.clicked.connect(self.stop_timer)

        if self.current_time == 0:
            self.pomo_timer.stop()

            if self.is_break is True:
                self.is_break = False
            else:
                self.is_break = True

            self.start_pomo_btn.setText('Продолжить')
            self.player.play()
            self.start_pomo_btn.setDisabled(False)
            self.exit_from_process_btn.setDisabled(True)
            self.exit_from_process_btn.setVisible(False)

            self.count += 1
            if self.count == int(self.pomo_info[0][3]) * 2:
                self.start_pomo_btn.setText('Завершить')
                self.start_pomo_btn.clicked.connect(self.timer_exit)

        self.update_gui()

    def update_gui(self):
        self.timer_pomo.display(self.time_left)

    def stop_timer(self):
        self.pomo_timer.stop()
        minuts, seconds = divmod(self.current_duration, 60)
        self.time_left = str(minuts).zfill(2) + ':' + str(seconds).zfill(2)
        self.timer_pomo.display(self.time_left)

        self.start_pomo_btn.setDisabled(False)
        self.start_pomo_btn.clicked.connect(self.start_pomo)

        self.exit_from_process_btn.setDisabled(True)
        self.exit_from_process_btn.setVisible(False)

    def timer_exit(self):
        self.pomo_timer.stop()
        self.start_pomo_btn.setText('Старт')
        self.pomo_label.setText('Хорошая работа!')
        self.timer_pomo.display(0)
        self.start_pomo_btn.setDisabled(False)
        self.start_pomo_btn.clicked.connect(self.start_pomo)


class AboutPomoWindow(QScrollArea, Ui_ScrollArea):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainApplication()
    form.show()
    sys.exit(app.exec())
