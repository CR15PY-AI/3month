import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Напитки")

        self.tea_cb = QCheckBox("Чай")
        self.coffee_cb = QCheckBox("Кофе")
        self.juice_cb = QCheckBox("Сок")

        self.show_button = QPushButton("Показать выбор")
        self.show_button.clicked.connect(self.show_selection)

        self.result_label = QLabel("")
        self.result_label.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(self.tea_cb)
        layout.addWidget(self.coffee_cb)
        layout.addWidget(self.juice_cb)
        layout.addWidget(self.show_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def show_selection(self):
        selected = []
        if self.tea_cb.isChecked():
            selected.append("Чай")
        if self.coffee_cb.isChecked():
            selected.append("Кофе")
        if self.juice_cb.isChecked():
            selected.append("Сок")

        result_text = ", ".join(selected) if selected else "Ничего не выбрано"
        self.result_label.setText(result_text)
        self.result_label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())