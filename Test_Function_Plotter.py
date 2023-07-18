import pytest
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QApplication
from Function_Plotter import MainWindow


@pytest.fixture
def app(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    qtbot.wait_for_window_shown(window)
    yield window
    window.close()


def test_invalid_function_error_message(app, qtbot):
    function_input = app.function_input
    x_min_input = app.x_min_input
    x_max_input = app.x_max_input
    plot_button = app.plot_button

    qtbot.keyClicks(function_input, "invalid_function")
    qtbot.keyClicks(x_min_input, "0")
    qtbot.keyClicks(x_max_input, "10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)



def test_invalid_value_error_message(app, qtbot):
    function_input = app.function_input
    x_min_input = app.x_min_input
    x_max_input = app.x_max_input
    plot_button = app.plot_button

    qtbot.keyClicks(function_input, "x**2")
    qtbot.keyClicks(x_min_input, "invalid_value")
    qtbot.keyClicks(x_max_input, "10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)



def test_invalid_range_error_message(app, qtbot):
    function_input = app.function_input
    x_min_input = app.x_min_input
    x_max_input = app.x_max_input
    plot_button = app.plot_button

    qtbot.keyClicks(function_input, "x**2")
    qtbot.keyClicks(x_min_input, "10")
    qtbot.keyClicks(x_max_input, "5")
    qtbot.mouseClick(plot_button, Qt.LeftButton)



def test_valid_function_and_range(app, qtbot):
    function_input = app.function_input
    x_min_input = app.x_min_input
    x_max_input = app.x_max_input
    plot_button = app.plot_button

    qtbot.keyClicks(function_input, "x**2")
    qtbot.keyClicks(x_min_input, "-5")
    qtbot.keyClicks(x_max_input, "5")
    qtbot.mouseClick(plot_button, Qt.LeftButton)

    assert app.canvas.figure.axes


if __name__ == "__main__":
    pytest.main(["-v"])
