"""
Using pandas:
    - load the CSV file specified by CSV_FILE
    - using the data in the file, create a plot where 
        - the x axis is time (ascending)
        - the y axis is the number of daily infections (per age group)
    - save the plot to the file "part_2_3.png"

You don't need to get fancy with labelling plot axes or adding titles or anything like that.
If you cannot figure out how to do all of this, then plot something else.
"""
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/report_2_3.csv"

# Your code goes here
data_plot = pd.read_csv(CSV_FILE) 
data = data_plot.melt(id_vars=['time', 'age'])

# aussume that age is a categorical variable 

fig = plt.figure(figsize=(10,10))
plot_order = 1

for idx, gp in data.groupby('age'):
    ax = fig.add_subplot(2,2,plot_order) 
    ax.scatter(x=gp['time'], y=gp['value'])
    
    ax.grid()
    ax.set_ylabel('daliy infections', fontsize=12)
    ax.set_xlabel('time', fontsize=12)
    ax.set_title(f'Age : {idx}', fontsize=14)

    plot_order += 1
    
plt.savefig('part_2_3.png')