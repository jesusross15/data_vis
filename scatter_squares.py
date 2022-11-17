#%%
import matplotlib.pyplot as plt

"""x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]"""

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# using a ccolor map
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# This is to get rid of the default scientific notation in the x and y axis
ax.ticklabel_format(useOffset=False, style='plain')

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()


# %%
