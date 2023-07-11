import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.function_label = QLabel("Enter a function of x:")
        self.function_input = QLineEdit()
        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)

        self.x_min_label = QLabel("Enter the minimum value of x:")
        self.x_min_input = QLineEdit()
        self.layout.addWidget(self.x_min_label)
        self.layout.addWidget(self.x_min_input)

        self.x_max_label = QLabel("Enter the maximum value of x:")
        self.x_max_input = QLineEdit()
        self.layout.addWidget(self.x_max_label)
        self.layout.addWidget(self.x_max_input)

        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.plot_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def parse_function(self, func):
        # Check if the function is valid and replace ^ with ** for exponentiation
        func = func.replace("^", "**")
        if not re.match(r"^[-+*/0-9x\s()]+$", func):
            raise ValueError("Invalid function")
        return func

    def parse_value(self, value):
        try:
            return float(value)
        except ValueError:
            raise ValueError("Invalid value")

    def plot_function(self):
        function = self.function_input.text().strip()
        x_min = self.x_min_input.text().strip()
        x_max = self.x_max_input.text().strip()

        try:
            parsed_function = self.parse_function(function)
        except ValueError as e:
            self.show_error_message("Invalid Function", str(e))
            return

        try:
            parsed_x_min = self.parse_value(x_min)
            parsed_x_max = self.parse_value(x_max)
        except ValueError as e:
            self.show_error_message("Invalid Value", str(e))
            return

        if parsed_x_min >= parsed_x_max:
            self.show_error_message("Invalid Range", "Minimum value must be less than maximum value")
            return

        x = np.linspace(parsed_x_min, parsed_x_max, 100)
        try:
            y = eval(parsed_function)
        except Exception as e:
            self.show_error_message("Evaluation Error", str(e))
            return

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        self.canvas.draw()

    def show_error_message(self, title, message):
        error_dialog = QMessageBox()
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Apply some styling
    app.setStyle("Fusion")
    palette = app.palette()
    palette.setColor(palette.Window, Qt.white)
    palette.setColor(palette.WindowText, Qt.black)
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
