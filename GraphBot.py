import numpy as np
import matplotlib.pyplot as plt

class GraphBot:
    def __init__(self, x_data, y_data):
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        
    def plot_with_fit(self):
        # Calculate the line of best fit
        coefficients = np.polyfit(self.x_data, self.y_data, 1)
        polynomial = np.poly1d(coefficients)
        y_fit = polynomial(self.x_data)
        
        # Plot the data points
        plt.scatter(self.x_data, self.y_data, label='Data Points')
        
        # Plot the line of best fit
        plt.plot(self.x_data, y_fit, color='red', label='Line of Best Fit')
        
        # Add labels and title
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Data Points and Line of Best Fit')
        plt.legend()
        
        # Show the plot
        plt.show()

# Example usage:
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 5, 4, 5]

# Initialize the GraphBot with the data
graph_bot = GraphBot(x_data, y_data)

# Plot the data and the line of best fit
graph_bot.plot_with_fit()
