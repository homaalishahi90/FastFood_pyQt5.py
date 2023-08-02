import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QTextCursor

class FastFood(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(" Fast Food ")
        self.setGeometry(200, 200, 800, 450)
        self.setStyleSheet("background-color: #a4fbf9;")

        # Food Name
        self.l1 = QLabel("FoodName", self)
        self.l1.move(10, 10)
        self.l1.resize(120, 30)
        self.l1.setStyleSheet("background-color: #a4fbf9; font-size: 14pt;")

        self.t1 = QTextEdit(self)
        self.t1.move(120, 10)
        self.t1.resize(120, 30)
        self.t1.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

        # Price
        self.l2 = QLabel("Price :", self)
        self.l2.move(10, 60)
        self.l2.resize(120, 30)
        self.l2.setStyleSheet("background-color: #a4fbf9; font-size: 14pt;")

        self.t2 = QTextEdit(self)
        self.t2.move(120, 60)
        self.t2.resize(120, 30)
        self.t2.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

        # Number
        self.l3 = QLabel("Number :", self)
        self.l3.move(10, 110)
        self.l3.resize(120, 30)
        self.l3.setStyleSheet("background-color: #a4fbf9; font-size: 14pt;")

        self.t3 = QTextEdit(self)
        self.t3.move(120, 110)
        self.t3.resize(120, 30)
        self.t3.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

        # Off
        self.l4 = QLabel("Off :", self)
        self.l4.move(10, 160)
        self.l4.resize(120, 30)
        self.l4.setStyleSheet("background-color: #a4fbf9; font-size: 14pt;")

        self.t4 = QTextEdit(self)
        self.t4.move(120, 160)
        self.t4.resize(120, 30)
        self.t4.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

        # Price * Num
        self.l5 = QLabel("Price*Num :", self)
        self.l5.move(300, 10)
        self.l5.resize(120, 30)
        self.l5.setStyleSheet("background-color: #a4fbf9; font-size: 14pt;")

        self.t5 = QTextEdit(self)
        self.t5.move(410, 10)
        self.t5.resize(120, 30)
        self.t5.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

        # Off Value
        self.l6 = QLabel("Off Value :", self)
        self.l6.move(300, 60)
        self.l6.resize(120, 30)
        self.l6.setStyleSheet("background-color: #a4fbf9; font-size: 14pt;")

        self.t6 = QTextEdit(self)
        self.t6.move(410, 60)
        self.t6.resize(120, 30)
        self.t6.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

        # Payment
        self.l7 = QLabel("Payment :", self)
        self.l7.move(300, 110)
        self.l7.resize(120, 30)
        self.l7.setStyleSheet("background-color: #a4fbf9; font-size: 14pt;")

        self.t7 = QTextEdit(self)
        self.t7.move(410, 110)
        self.t7.resize(120, 30)
        self.t7.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

        # Calculate Button
        self.btn = QPushButton("Calculate", self)
        self.btn.move(300, 160)
        self.btn.resize(230, 40)
        self.btn.setStyleSheet("background-color: #fbd46d; font-size: 14pt;")
        self.btn.clicked.connect(self.calculate_payment)

        # Clear Button
        self.btn_clear = QPushButton("Clear", self)
        self.btn_clear.move(550, 160        )
        self.btn_clear.resize(230, 40)
        self.btn_clear.setStyleSheet("background-color: #fbd46d; font-size: 14pt;")
        self.btn_clear.clicked.connect(self.clear_all)

        # Output
        self.output = QTextEdit(self)
        self.output.move(10, 210)
        self.output.resize(780, 230)
        self.output.setStyleSheet("background-color: #cffa6d; font-size: 14pt;")

    def calculate_payment(self):
        food_name = self.t1.toPlainText()
        price = float(self.t2.toPlainText())
        num = int(self.t3.toPlainText())
        off = float(self.t4.toPlainText())

        total_price = price * num
        off_value = total_price * off / 100
        payment = total_price - off_value

        self.t5.setText(str(total_price))
        self.t6.setText(str(off_value))
        self.t7.setText(str(payment))

        self.output.append(f"Food Name: {food_name}")
        self.output.append(f"Price: {price}")
        self.output.append(f"Number: {num}")
        self.output.append(f"Off: {off}")
        self.output.append(f"Total Price: {total_price}")
        self.output.append(f"Off Value: {off_value}")
        self.output.append(f"Payment: {payment}")
        self.output.append("------------------------------")

        # Write to file
        with open("output.txt", "a") as f:
            f.write(f"Food Name: {food_name}\n")
            f.write(f"Price: {price}\n")
            f.write(f"Number: {num}\n")
            f.write(f"Off: {off}\n")
            f.write(f"Total Price: {total_price}\n")
            f.write(f"Off Value: {off_value}\n")
            f.write(f"Payment: {payment}\n")
            f.write("------------------------------\n")
            
            

    def clear_all(self):
        self.t1.clear()
        self.t2.clear()
        self.t3.clear()
        self.t4.clear()
        self.t5.clear()
        self.t6.clear()
        self.t7.clear()
        self.output.clear()

if __name__ == '__main__':
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
    app = QApplication([])
    window = FastFood()
    window.show()
    app.exec_()