from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import style, sqlite3
import datetime

# Текущая дата
today = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

# Подключение к базе данных
con = sqlite3.connect("money.db")
cur = con.cursor()

class AddRecur(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 300, 400, 600)
        self.setFont(QFont("Times", 13))
        self.setStyleSheet("background-color: black; color: white;") 
        self.setWindowTitle("add regular consumption")
        self.setWindowIcon(QIcon("icons/coin.png"))
        self.setFixedSize(self.size())
        self.initUI()
        self.show()

    def initUI(self):
        self.initWidgets()
        self.initLayouts()

    def initWidgets(self):
        self.titleLabel = QLabel("Regular Consumption")
        self.titleLabel.setFont(QFont("Times", 18))
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.iconLabel = QLabel()
        pixmap = QPixmap("icons/addrecur.png")
        self.iconLabel.setPixmap(pixmap)
        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.iconLabel.setContentsMargins(0, 50, 0, 0)

        self.nameInput = QLineEdit()
        self.nameInput.setPlaceholderText("Name")
        self.nameInput.setContentsMargins(20, 0, 20, 0)

        self.amountInput = QLineEdit()
        self.amountInput.setPlaceholderText("Amount")
        self.amountInput.setContentsMargins(20, 0, 20, 0)

        self.frequencyInput = QLineEdit()
        self.frequencyInput.setPlaceholderText("Frequency (in days)")
        self.frequencyInput.setContentsMargins(20, 0, 20, 0)

        self.dateInput = QLineEdit()
        self.dateInput.setPlaceholderText("Start Date")
        self.dateInput.setContentsMargins(20, 0, 20, 20)

        self.categoryLabel = QLabel("Choose category")
        self.categoryLabel.setAlignment(Qt.AlignCenter)

        self.categoryCombo = QComboBox()
        self.categoryCombo.addItems([
           "Home", "Transport", "Phone", "Food", "Clothing", "Credit card", "Other"
        ])

        self.submitBtn = QPushButton("Add")
        self.submitBtn.setStyleSheet(style.addRevenueSubmitBtn())
        self.submitBtn.clicked.connect(self.addRecur)

    def initLayouts(self):
        layout = QVBoxLayout()
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.iconLabel)
        layout.addStretch()
        layout.addWidget(self.nameInput)
        layout.addWidget(self.amountInput)
        layout.addWidget(self.frequencyInput)
        layout.addWidget(self.dateInput)
        layout.addWidget(self.categoryLabel)
        layout.addWidget(self.categoryCombo)
        layout.addWidget(self.submitBtn)
        self.setLayout(layout)

    def addRecur(self):
        name = self.nameInput.text()
        amount = self.amountInput.text()
        frequency = self.frequencyInput.text()
        start_date = self.dateInput.text()
        category = self.categoryCombo.currentText()

        if name and amount and frequency and start_date:
            try:
                query = """
                INSERT INTO recurring (id, name, category, frequency, per, start_date)
                VALUES (NULL, ?, ?, ?, ?, ?)
                """
                cur.execute(query, (name, category, frequency, amount, start_date))
                con.commit()
                QMessageBox.information(self, "Successfully", "Regular cunsumption added successfully.")
                self.close()
            except Exception:
                QMessageBox.warning(self, "Error", "Error adding regular cunsumption in database.")
        else:
            QMessageBox.warning(self, "Attention", "All fields must be filled in.")
