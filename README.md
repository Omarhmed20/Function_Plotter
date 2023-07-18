
# Function Plotter

Function Plotter is a simple application that allows you to plot mathematical functions using the PySide2 and Matplotlib libraries.

## Installation

1. Make sure you have Python 3.9 or later installed.
2. Install the required dependencies by running the following command:
   ```shell
   pip install PySide2 matplotlib 
## Usage

Run the `function_plotter.py` script to launch the application:
   ```shell
   python function_plotter.py
   ```

Enter a valid mathematical function, along with the minimum and maximum values of x, and click the "Plot" button to visualize the function.

## Examples

### Working Example

![Working Example](screenshots/working_example.png)

In this example, we have entered the function `x**2`, with a minimum value of `-5` and a maximum value of `5`. The application successfully plots the function.

### Wrong Example

![Wrong Example](screenshots/wrong_example.png)

In this example, we have entered an invalid function `invalid_function`. The application displays an error message indicating that the function is invalid.

## License

This project is licensed under the [MIT License](LICENSE).


