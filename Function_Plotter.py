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
    QHBoxLayout,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        self.layout = QVBoxLayout()

        # Function input layout
        function_layout = QHBoxLayout()

        # Function label
        self.function_label = QLabel("Enter a function of x:")
        function_layout.addWidget(self.function_label)

        # Function input
        self.function_input = QLineEdit()
        function_layout.addWidget(self.function_input)

        self.layout.addLayout(function_layout)

        # Horizontal layout for x min and max inputs
        x_range_layout = QHBoxLayout()

        # x min input
        self.x_min_label = QLabel("Minimum value of x:")
        self.x_min_input = QLineEdit()
        x_range_layout.addWidget(self.x_min_label)
        x_range_layout.addWidget(self.x_min_input)

        # x max input
        self.x_max_label = QLabel("Maximum value of x:")
        self.x_max_input = QLineEdit()
        x_range_layout.addWidget(self.x_max_label)
        x_range_layout.addWidget(self.x_max_input)

        self.layout.addLayout(x_range_layout)

        # Plot button
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.plot_button)

        # Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Matplotlib navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)

        # Central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Set size policies and stretch factors for scalability
        self.function_input.setSizePolicy(
            self.function_input.sizePolicy().Expanding,
            self.function_input.sizePolicy().Fixed,
        )
        self.x_min_input.setSizePolicy(
            self.x_min_input.sizePolicy().Expanding,
            self.x_min_input.sizePolicy().Fixed,
        )
        self.x_max_input.setSizePolicy(
            self.x_max_input.sizePolicy().Expanding,
            self.x_max_input.sizePolicy().Fixed,
        )
        self.layout.setStretchFactor(self.function_input, 1)
        self.layout.setStretchFactor(self.x_min_input, 1)
        self.layout.setStretchFactor(self.x_max_input, 1)
        self.layout.setStretchFactor(self.canvas, 4)

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
        function = self.parse_function(self.function_input.text().strip())
        x_min = self.parse_value(self.x_min_input.text().strip())
        x_max = self.parse_value(self.x_max_input.text().strip())

        if x_min >= x_max:
            self.show_error_message("Invalid Range", "Minimum value must be less than maximum value")
            return

        x = np.linspace(x_min, x_max, 100)
        try:
            y = eval(function)
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
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.exec_()


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