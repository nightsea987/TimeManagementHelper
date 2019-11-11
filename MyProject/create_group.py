from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import sys
import sqlite3
from MyProject.design.create_group_design import Ui_Form


class CreateGroup(QWidget, Ui_Form):

    def __init__(self, func=None):
        super().__init__()
        self.setupUi(self)
        self.func = func

        self.line_error.hide()
        self.save_group_btn.clicked.connect(self.save_group)

    def save_group(self):
        self.group_title = self.group_name.text()
        if self.group_title == '':
            self.line_error.show()
            self.group_name.setStyleSheet(
                'QLineEdit {font-size: 13px; padding-left: 3px; border: '
                '2px solid red;}'
                'QLineEdit:hover {border: 1px solid red;}')
        else:
            self.line_error.hide()
            self.group_name.setStyleSheet('border-color: black;')
            con = sqlite3.connect('my_project.db')
            cur = con.cursor()
            cur.execute(f"""INSERT INTO groups(name, color) 
                VALUES ('{self.group_title}', 
                '{self.comboBox.currentText()}')""")
            con.commit()
            con.close()
            self.func()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CreateGroup()
    form.show()
    sys.exit(app.exec())
