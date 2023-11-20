from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.go_find)

    def go_find(self):
        data = sqlite3.connect('coffee.sqlite').cursor().execute(f"""SELECT * FROM table1 WHERE сорт = 
                                                                    '{self.lineEdit.text()}'""").fetchall()
        if data:
            self.label_8.clear()
            self.lineEdit_2.setText(str(data[0][0]))
            self.lineEdit_3.setText(data[0][1])
            self.lineEdit_5.setText(data[0][2])
            self.lineEdit_4.setText(data[0][3])
            self.textEdit.setPlainText(data[0][4])
            self.lineEdit_6.setText(str(data[0][5]))
            self.lineEdit_8.setText(str(data[0][6]))
        else:
            self.label_8.setText(f'Сорт "{self.lineEdit.text()}" не найден')
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_5.clear()
            self.lineEdit_4.clear()
            self.textEdit.clear()
            self.lineEdit_6.clear()
            self.lineEdit_8.clear()


if __name__ == '__main__':
    app = QApplication([])
    coffee = Coffee()
    coffee.show()
    sys.exit(app.exec_())
