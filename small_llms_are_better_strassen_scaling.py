import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from matplotlib.colors import LinearSegmentedColormap

# Use the 'science' style for plots
plt.style.use(['science'])

# Define the scaling functions
def linear_scaling(n):
    """Linear scaling function."""
    return n

def strassen_complexity(n):
    """Strassen's complexity function n^log2(7)."""
    return n ** np.log2(7)

# Generate data points for matrix sizes
n_values = np.linspace(1, 100, 1000)

# Calculate the corresponding complexity values
linear_values = linear_scaling(n_values)
strassen_values = strassen_complexity(n_values)

# GPQA line calculation based on two points
x1, y1 = 1, 32.8  # Starting point
x2, y2 = n_values[-1], 46.7  # Ending point (using the last n value)

# Calculate the slope of the GPQA line
gpqa_slope = (y2 - y1) / (x2 - x1)

# Generate the GPQA values (linear interpolation between two points)
gpqa_values = gpqa_slope * (n_values - x1) + y1

# Initialize the plot with custom size and resolution
plt.figure(figsize=(6, 5), dpi=300)

# Create a custom colormap based on the 'viridis' colormap
viridis = plt.get_cmap('viridis')
colors = [viridis(i) for i in np.linspace(0, 1, 256)]
custom_cmap = LinearSegmentedColormap.from_list("custom_viridis", colors)

# Plot the Linear and Strassen complexity curves with continuous color gradient
for i in range(len(n_values) - 1):
    plt.plot(n_values[i:i+2], linear_values[i:i+2], color=custom_cmap(i / len(n_values)), linewidth=2)
    plt.plot(n_values[i:i+2], strassen_values[i:i+2], color=custom_cmap(i / len(n_values)), linewidth=2)

# Plot the GPQA line with a dashed red line
plt.plot(n_values, gpqa_values, color='red', linestyle='--', linewidth=2, label="GPQA score")

# Add legend entries without plotting the actual lines
plt.plot([], [], color=viridis(0.25), label='Linear Scaling')
plt.plot([], [], color=viridis(0.75), label="Strassen's ($n^{\log_2(7)}$)")

# Set custom y-ticks for strassen complexity at minimum and maximum values
yticks_positions = [min(strassen_values), max(strassen_values)]
yticks_labels = ['1', '$n^{\log_2(7)}$']
plt.yticks(yticks_positions, yticks_labels)

# Set x-ticks for start, middle, and end points of the matrix size
plt.xticks([1, 50, 100], ['1', '', 'n'])

# Add titles and labels
plt.title("Matrix Multiplication Complexity with Size", fontsize=16)
plt.xlabel(r"Matrix Size ($n$) $\rightarrow$", fontsize=12)
plt.ylabel(r"Computational Complexity $\rightarrow$", fontsize=12, labelpad=-20)

# Display the legend
plt.legend(fontsize=10)

# Ensure the layout is tight and doesn't overlap
plt.tight_layout()

# Show the final plot
plt.show()

# Print the slope of the GPQA line
print(f"GPQA slope: {gpqa_slope}")
