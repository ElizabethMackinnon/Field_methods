import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import timedelta

# time vs temperature

data = pd.read_csv(r"C:\Users\Lizma\iCloudDrive\Field_methods\wunder.updated.csv")
start = '00:04'
end = '17:24'

Time = list(data['Time'])
values = list(data['Temperature'])

x = Time.index(start)
y = Time.index(end)

sub_Time = Time[x : y]
sub_values = values[x : y]
obs_start = Time.index('12:39')
obs_end = Time.index('16:54')
plt.axvspan(obs_start, obs_end, color='blue', alpha=0.5, label='Observation period')

plt.plot(sub_Time, sub_values, label='Temperature [deg C]', linestyle = '-', color = 'black')
plt.xlabel('Time')
plt.ylabel("Temperature [deg C]")
plt.title('Temperature vs Time')

plt.legend(loc='upper left')

locs, labels = plt.xticks()
plt.xticks(locs[::10], labels[::10], rotation=45)

locs, labels = plt.yticks()
plt.yticks(locs[::10], labels[::10])
plt.tight_layout()
plt.show()

# time vs solar
Time = list(data['Time'])
values = list(data['Solar'])

x = Time.index(start)
y = Time.index(end)

sub_Time = Time[x : y]
sub_values = values[x : y]

plt.plot(sub_Time, sub_values, label='Solar', linestyle = '--', color = 'pink')
plt.xlabel('Time')
plt.ylabel("Solar")
plt.title('Solar vs Time')

locs, labels = plt.xticks()
plt.xticks(locs[::10], labels[::10], rotation=45)

plt.subplots_adjust(bottom=0.35)
plt.show()