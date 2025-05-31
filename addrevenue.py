from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import style, sqlite3
import datetime

today = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

# Baza bilan bog‘lanish
con = sqlite3.connect("money.db")
cur = con.cursor()

class AddRevenue(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 200, 350, 550)
        self.setFont(QFont("Times", 13))
        self.setStyleSheet("background-color:black; color:white;")
        self.setWindowTitle('')  # Oynaning sarlavhasi
        self.setWindowIcon(QIcon('icons/coin.png'))
        self.setFixedSize(self.size())  # Oynaning o‘lchamini o‘zgartirishni bloklash
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # Sarlavha
        self.addRevenueTitle = QLabel("Add income")
        self.addRevenueTitle.setFont(QFont("Times", 18))
        self.addRevenueTitle.setAlignment(Qt.AlignCenter)

        # Rasm
        self.addRevenueImg = QLabel()
        currencypixmap = QPixmap('icons/coinstack.png')
        self.addRevenueImg.setPixmap(currencypixmap)
        self.addRevenueImg.setAlignment(Qt.AlignCenter)
        self.addRevenueImg.setContentsMargins(0, 50, 0, 0)

        # Kiritish maydonchalari
        self.amountEntry = QLineEdit()
        self.amountEntry.setPlaceholderText("Amount")
        self.amountEntry.setContentsMargins(20, 0, 20, 0)

        self.activityEntry = QLineEdit()
        self.activityEntry.setPlaceholderText("description")
        self.activityEntry.setContentsMargins(20, 0, 20, 20)

        # Tugma
        self.submitBtn = QPushButton("Save")
        self.submitBtn.setStyleSheet(style.addRevenueSubmitBtn())
        self.submitBtn.clicked.connect(self.addRevenue)

    def layouts(self):
        # Layoutni tuzish
        self.addRevenueMainLayout = QVBoxLayout()
        self.addRevenueMainLayout.addWidget(self.addRevenueTitle)
        self.addRevenueMainLayout.addWidget(self.addRevenueImg)
        self.addRevenueMainLayout.addStretch()
        self.addRevenueMainLayout.addWidget(self.amountEntry)
        self.addRevenueMainLayout.addWidget(self.activityEntry)
        self.addRevenueMainLayout.addWidget(self.submitBtn)

        self.setLayout(self.addRevenueMainLayout)

    def addRevenue(self):
        amount = self.amountEntry.text()
        name = self.activityEntry.text()

        if name and amount != "":
            try:
                query = "INSERT INTO 'revenue' (revenueamount, revenuename, date) VALUES(?,?,?)"
                cur.execute(query, (amount, name, today))
                con.commit()
                QMessageBox.information(self, "Successfully", "Income successfully added to the database!")
                self.close()
            except:
                QMessageBox.warning(self, "Error", "Error adding income to the database..")
        else:
            QMessageBox.warning(self, "Attention", "Fields must not be empty.")
