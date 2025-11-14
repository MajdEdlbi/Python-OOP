import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QLineEdit, QGridLayout, QPushButton
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        new_label = QLabel("Name:")
        new_line = QLineEdit()

        birth_label = QLabel("Date of birth:")
        self.birth_line = QLineEdit()


        calcluaebtn = QPushButton("Calculate")
        calcluaebtn.clicked.connect(self.calage)
        self.outputlable = QLabel('')


        grid.addWidget(new_label, 0, 0)
        grid.addWidget(new_line, 0, 1)
        grid.addWidget(birth_label, 1, 0)
        grid.addWidget(self.birth_line, 1, 1)

        grid.addWidget(calcluaebtn, 2, 0, 1, 2)
        grid.addWidget(self.outputlable, 3, 0, 1, 2)

        self.setLayout(grid)

    def calage(self):
        current_year = datetime.now().year
        year_of_birth= self.birth_line.text()
        age = current_year - int(year_of_birth)
        self.outputlable.setText(str(age))

app = QApplication(sys.argv)
age_cal = AgeCalculator()
age_cal.show()
sys.exit(app.exec())