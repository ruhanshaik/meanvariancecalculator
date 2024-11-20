import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load data
df = pd.read_csv('epa-sea-level.csv')

# Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)

# Line of best fit for all data
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
sea_levels = slope * years_extended + intercept
plt.plot(years_extended, sea_levels, 'r', label='Best Fit Line (1880–2050)')

# Line of best fit from 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent = pd.Series(range(2000, 2051))
sea_levels_recent = slope_recent * years_recent + intercept_recent
plt.plot(years_recent, sea_levels_recent, 'g', label='Best Fit Line (2000–2050)')

# Add labels, title, and legend
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.legend()

# Save plot
plt.savefig('sea_level_plot.png')
plt.show()
