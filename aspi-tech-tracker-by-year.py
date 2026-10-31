import matplotlib.pyplot as plt

# Hardcoded data based on ASPI Critical Technology Tracker dataset windows
# Using the ending year of the 5-year rolling window as the plotting year
years = [2007, 2017, 2022, 2023, 2024, 2025]
total_technologies = [64, 64, 44, 64, 74, 74]
china_leads = [3, 28, 37, 57, 66, 69]
us_leads = [60, 36, 7, 7, 8, 5]

# Initialize the plot
plt.figure(figsize=(10, 6))

# Plot lines for China and the US
plt.plot(years, china_leads, marker='o', color='#DE2910', linewidth=2.5, label='China Lead')
plt.plot(years, us_leads, marker='s', color='#0A3161', linewidth=2.5, label='United States Lead')

# Add the total number of tracked technologies as a reference background line
plt.plot(years, total_technologies, color='gray', linestyle='--', alpha=0.7, label='Total Technologies Tracked')

# Add data labels next to the points for clarity
for i, txt in enumerate(china_leads):
    plt.annotate(f"{txt}/{total_technologies[i]}", (years[i], china_leads[i]), 
                 textcoords="offset points", xytext=(0, 10), ha='center', color='#DE2910', weight='bold')

for i, txt in enumerate(us_leads):
    plt.annotate(f"{txt}/{total_technologies[i]}", (years[i], us_leads[i]), 
                 textcoords="offset points", xytext=(0, -15), ha='center', color='#0A3161', weight='bold')

# Configure labels, titles, and grid
plt.title('ASPI Critical Technology Tracker: Technology Leadership (2007 - 2025)\n(Plotted by the ending year of rolling 5-year windows)', fontsize=14, pad=15)
plt.xlabel('Window Ending Year', fontsize=12)
plt.ylabel('Number of Technologies Led', fontsize=12)
plt.xticks(years)
plt.ylim(-5, 85)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=True)

plt.tight_layout()

# Display the chart
plt.show()
