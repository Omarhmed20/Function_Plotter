
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

### Working Example 1

![Working Example](screenshots/Working_Example_1.png)

In this example, we have entered the function `x**2`, with a minimum value of `-5` and a maximum value of `5`. The application successfully plots the function.

### Working Example 2

![Working Example](screenshots/Working_Example_2.png)

In this example, we have entered the function `5*x^3 + 2*x`, with a minimum value of `0` and a maximum value of `10`. The application successfully plots the function.

### Wrong Example 1

![Wrong Example](screenshots/Wrong_Example_2.png)

In this example, we have entered an invalid function `x**2 + a`. The application displays an error message indicating that the function is invalid.

### Wrong Example 2

![Wrong Example](screenshots/Wrong_Example_3.png)

In this example, we have entered an invalid min value `number`. The application displays an error message indicating that the value is invalid.

### Wrong Example 3

![Wrong Example](screenshots/Wrong_Example_1.png)

In this example, we have entered a max value of x that is less than min value of x `min x = -5, max x = -10`. The application displays an error message indicating that max value of x is less than min value of x.

## License

This project is licensed under the [MIT License](LICENSE).


