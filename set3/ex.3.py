import matplotlib.pyplot as plt
import numpy as np

def plot_polynomial(poly_str, x_min, x_max):
    x_val = np.linspace(x_min, x_max, 200)
    try:
        y_val = eval(poly_str, {'x': x_val})
        
        plt.plot(x_val, y_val)
        plt.xlabel('Values of x')
        plt.ylabel('Values of f(x)')
        plt.title('Graph of polynomial: ' + poly_str)
        plt.grid(True)
        plt.show()
    except Exception as e:
        print("An error occurred:", e)

polynomial = "5*x**4 + 2*x**3 - x + 6"
x_min = -10
x_max = 10

plot_polynomial(polynomial, x_min, x_max)
