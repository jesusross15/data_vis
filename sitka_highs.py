import csv

import matplotlib.pyplot as plt

filename = "data_vis/sitka.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    """for index, column_header in enumerate(header_row): 
        print(index, column_header)"""
    
    # Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5]) 
        highs.append(high)

print(highs)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24) 
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

