import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import (QApplication, QWidget, QHeaderView,
                             QTableWidgetItem)


class Cappuccino(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.setFixedSize(self.size())
        self.setWindowTitle('Espresso') 

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.btnEdit.clicked.connect(self.edit)

        self.load_data()
        self.show()

    def load_data(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()

        query = """SELECT id, title, sort, roasting, type, taste, price, volume FROM coffee"""
        cur.execute(query)
        rows = cur.fetchall()

        self.table.setRowCount(len(rows))

        for row, row_data in enumerate(rows):
            for col, col_data in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(col_data)))

        con.close()

    def edit(self):
        from edit import Edit
        self.hide()
        self.edit_window = Edit()
        self.edit_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cappuccino()
    sys.exit(app.exec())