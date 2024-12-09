import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('noisy-dataA 1.csv')

# Plot the 2nd column (ValueA) and 3rd column (ValueB) over the first one (Time)
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['ValueA'], label='ValueA')
plt.plot(df['Time'], df['ValueB'], label='ValueB')

# Adding title and labels
plt.title('Plot of ValueA and ValueB over Time')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()

# Show the plot
plt.show()