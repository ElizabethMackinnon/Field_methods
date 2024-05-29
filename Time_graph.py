import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv(r"C:\Users\Lizma\iCloudDrive\Field_methods-main\May_26.csv")
start = '00:00'
end = '23:50'

Time = list(data['Time'])
values = list(data['Temperature'])

x = Time.index(start)
y = Time.index(end)

sub_Time = Time[x : y]
sub_values = values[x : y]

plt.plot(sub_Time, sub_values, label='Temperature [deg C]', linestyle = '--', color = 'black')
plt.xlabel('Time')
plt.ylabel("Temperature [deg C]")
plt.title('Temperature vs Time')

locs, labels = plt.xticks()
plt.xticks(locs[::10], labels[::10], rotation=45)

locs, labels = plt.yticks()
plt.yticks(locs[::10], labels[::10], rotation=45)

plt.axvspan(12, 14, color='gray', alpha=0.5)

plt.subplots_adjust(bottom=0.35)
plt.show()