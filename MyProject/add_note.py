from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtGui import QFont
import sys
import sqlite3
from MyProject.design.add_note_design2 import Ui_Form
from set_color import GetColor


class CreateNote(QWidget, Ui_Form):

    def __init__(self, func=None, create=True):
        super().__init__()
        self.setupUi(self)
        self.func = func
        self.get_color = GetColor()

        self.get_color_btn.clicked.connect(self.get_color.show)
        self.get_color.color_btn.clicked.connect(self.set_design)
        self.background_color = ''

        self.font_changed = QFont()
        self.font_changed.setPixelSize(12)
        self.text_note_edit.setFont(self.font_changed)

        self.save_note_btn.clicked.connect(self.save_note)

        self.fontComboBox.currentFontChanged.connect(self.change_font)
        self.font_size_box.currentTextChanged.connect(self.change_font_size)
        self.open_file_btn.clicked.connect(self.open_file)
        if create:
            self.del_note_btn.setText('Сохранить \n в файл')
            self.del_note_btn.clicked.connect(self.save_to_file)

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать текстовый файл',
                                            '', "Текстовый файл(*.txt)")[0]
        if len(fname) != 0:
            with open(fname, 'r', encoding='utf-8') as f:
                self.text_note_edit.appendPlainText(f.read())

    # изменяет размер шрифта при выборе размера
    def change_font_size(self):
        self.font_changed.setPixelSize(int(self.font_size_box.currentText()))
        self.text_note_edit.setFont(self.font_changed)

    # изменяет шрифт
    def change_font(self):
        self.font_changed.setFamily(QFont
                                    (self.fontComboBox.currentFont()).family())
        self.text_note_edit.setFont(self.font_changed)

    def set_design(self):
        self.background_color = self.get_color.set_color()[1]
        self.text_note_edit.setStyleSheet(f'{self.get_color.set_color()[0]}')

    def save_note(self):
        self.color = self.background_color
        if self.background_color == '':
            self.color = '#fff'
        con = sqlite3.connect('my_project.db')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO notes(note, fontfamily, fontsize, color) 
        VALUES ('{self.text_note_edit.toPlainText()}', 
        '{QFont(self.fontComboBox.currentFont()).family()}', 
        {int(self.font_size_box.currentText())}, '{self.color}')""")
        con.commit()
        con.close()

        self.func()
        self.close()

    def save_to_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать текстовый файл',
                                            '', "Текстовый файл(*.txt)")[0]
        if len(fname) != 0:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(self.text_note_edit.toPlainText())


class EditNote(CreateNote):
    def __init__(self, current_note_id=None, func=None):
        super().__init__(create=False)
        self.current_note_id = current_note_id
        self.func = func
        self.notes_info = []
        self.show_note()
        self.del_note_btn.setText('Удалить \n заметку')
        self.del_note_btn.clicked.connect(self.del_note)
        self.save_note_btn.setText('Сохранить \n изменения')
        self.setWindowTitle('Редактировать заметку')

    def add_note_info(self):
        con = sqlite3.connect('my_project.db')
        cur = con.cursor()
        self.notes_info = cur.execute(f"""SELECT * FROM notes
                WHERE id = {self.current_note_id}""").fetchall()
        con.commit()
        con.close()
        print(self.notes_info)

    def del_note(self):
        con = sqlite3.connect('my_project.db')
        cur = con.cursor()
        cur.execute(f"""DELETE FROM notes WHERE id = {self.current_note_id}""")
        con.commit()
        con.close()

        self.func()
        self.close()

    def save_note(self):
        con = sqlite3.connect('my_project.db')
        cur = con.cursor()
        cur.execute(f"""UPDATE notes SET note =
            '{self.text_note_edit.toPlainText()}',
            fontfamily = '{QFont(self.fontComboBox.currentFont()).family()}',
            fontsize = {int(self.font_size_box.currentText())},
            color = '{self.background_color}' WHERE id = {self.current_note_id}""")
        con.commit()
        con.close()
        self.func()
        self.close()

    def show_note(self):
        self.add_note_info()
        self.text_note_edit.setPlainText(self.notes_info[0][1])
        self.font_size_box.setCurrentText(str(self.notes_info[0][3]))
        self.fontComboBox.setCurrentText(self.notes_info[0][2])
        self.fontComboBox.setCurrentFont(QFont(self.notes_info[0][2]))
        font = QFont()
        font.setFamily(self.notes_info[0][2])
        font.setPixelSize(self.notes_info[0][3])
        self.text_note_edit.setFont(font)
        for i in range(len(self.get_color.color_dc)):
            if self.get_color.color_dc[self.get_color.color_btn_lst[i]] == \
                    self.notes_info[0][4]:
                self.get_color.color_btn_lst[i].setChecked(True)
        self.set_design()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = EditNote()
    form.show()
    sys.exit(app.exec())
