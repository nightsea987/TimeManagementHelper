from PyQt5.QtWidgets import QWidget, QApplication
import sys
from MyProject.design.set_color_design import Ui_Form

TEXT_NOTE_DESIGN_WHITE = """padding-left: 30px; padding-right: 30px; 
                            background-color: #fff; padding-top: 6px;"""
TEXT_NOTE_DESIGN_YELLOW = """padding-left: 30px; padding-right: 30px; 
                            background-color: #faf87d; padding-top: 6px;"""
TEXT_NOTE_DESIGN_BLUE = """padding-left: 30px; padding-right: 30px; 
                            background-color: #ADD8E6; padding-top: 6px;"""
TEXT_NOTE_DESIGN_ORANGE = """padding-left: 30px; padding-right: 30px; 
                            background-color: #ffc966; padding-top: 6px;"""


class GetColor(QWidget, Ui_Form):
    design_result, color_result = '', ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.color_btn_lst = self.color_btn_group.buttons()
        self.color_btn_dc_design = {
                             self.color_btn_lst[0]: TEXT_NOTE_DESIGN_YELLOW,
                             self.color_btn_lst[1]: TEXT_NOTE_DESIGN_WHITE,
                             self.color_btn_lst[2]: TEXT_NOTE_DESIGN_BLUE,
                             self.color_btn_lst[3]: TEXT_NOTE_DESIGN_ORANGE}
        self.color_dc = {self.color_btn_lst[0]: '#faf87d',
                         self.color_btn_lst[1]: '#fff',
                         self.color_btn_lst[2]: '#ADD8E6',
                         self.color_btn_lst[3]: '#ffc966'}

        self.color_btn.clicked.connect(self.set_color)

    def set_color(self):
        for i in range(len(self.color_btn_lst)):
            if self.color_btn_lst[i].isChecked():
                GetColor.design_result = \
                    self.color_btn_dc_design[self.color_btn_lst[i]]
                GetColor.color_result = self.color_dc[self.color_btn_lst[i]]
        self.close()
        return GetColor.design_result, GetColor.color_result



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = GetColor()
    form.show()
    sys.exit(app.exec())
