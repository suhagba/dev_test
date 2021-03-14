"""
Using pandas:
    - load the CSV file specified by CSV_FILE
    - using the data in the file, create a plot where 
        - the x axis is time (ascending)
        - the y axis is the cumulative sum of daily infections for all people aged over 20
    - save the plot to the file "part_2_4.png"

An example of a "cumulative sum":
    input: [1, 2, 1, 1, 2, 3, 1, 1]
    cumulative sum: [1, 3, 4, 5, 7, 10, 11, 12]

You don't need to get fancy with labelling plot axes or adding titles or anything like that.
If you cannot figure out how to do all of this, then plot something else.
"""
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/report_2_3.csv"  # Same CSV file as the last question

# Your code goes here
data = pd.read_csv(CSV_FILE)

# create unique list of ages
age_groups = data.age.unique()

# only consider ages above 20
age_groups_filtered = [number for number in age_groups if number > 20]


# create a data frame dictionary to store data frames based on age groups
data_frame_dict = {elem: pd.DataFrame for elem in age_groups_filtered}

for key in data_frame_dict.keys():
    data_frame_dict[key] = data[:][data.age == key]

# calculate cumsum
for key in data_frame_dict.keys():
    data_frame_dict[key]['cumsum_daily_infections'] = data_frame_dict[key]['daily_infections'].cumsum()
    data_frame_dict[key] = data_frame_dict[key].drop(
        columns=['daily_infections', 'age'])

fig = plt.figure(figsize=(10, 10))
plot_order = 1

for key in data_frame_dict.keys():
    ax = fig.add_subplot(2, 1, plot_order)
    ax.scatter(x=data_frame_dict[key]['time'],
               y=data_frame_dict[key]['cumsum_daily_infections'])

    ax.grid()
    ax.set_ylabel('daliy infections cumulative sum', fontsize=12)
    ax.set_xlabel('time', fontsize=12)
    ax.set_title(f'Age : {key}', fontsize=14)

    plot_order += 1

plt.savefig('part_2_4.png')
