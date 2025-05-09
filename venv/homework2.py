import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("homework3")
        self.setGeometry(200,200,400,150)

        self.label = QLabel("Сколько будет 2+3?", self)
        self.label.move(20,20)

        self.input = QLineEdit(self)
        self.input.move(200,50)
        self.input.setPlaceholderText("Введите ответ: ")

        self.button = QPushButton("Проверить", self)
        self.button.move(250, 47)
        self.button.clicked.connect(self.check_answer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def check_answer(self):
        answer = self.input.text()
        if answer == "5":
            self.label.setText("Правильно!")
        else:
            self.label.setText("Неправильно!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())