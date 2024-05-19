import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#boxplot

duck_behaviours = [
    ("female", (0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 12, 14, 16, 20, 44, 50)),
    ("male", (3, 0, 0, 1, 13, 2, 0, 22, 27, 2, 2, 0, 0, 5, 11, 0))
]

labels = ['Female', 'Male']
colors = ['pink', 'blue']

fig, ax = plt.subplots()
ax.set_ylabel('Number of Behaviours')

data = [behaviour[1] for behaviour in duck_behaviours]

bplot = ax.boxplot(data, patch_artist=True)

ax.set_xticklabels([behaviour[0] for behaviour in duck_behaviours])

ax.set_title('Eider Behaviours Seperated by Sex')
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
    
plt.show()

#scatterplot

Data = {
    'x': [0, 5, 11, 0, 16, 0, 12, 4],
    'y': [27, 2, 2, 0, 14, 50, 3, 44],
    'colors': ['blue', 'blue', 'blue', 'blue', 'pink', 'pink', 'pink', 'pink'],
    'labels': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female']
}
df = pd.DataFrame(Data)

added_labels = set()

for i in range(len(df)):
    plt.scatter(df['x'][i], df['y'][i], color=df['colors'][i], label=df['labels'][i] if df['labels'][i] not in added_labels else "")
    added_labels.add(df['labels'][i])

plt.xlabel('Dives')
plt.ylabel('Bobbing')
plt.title('Eider Dives vs. Bobbing')

plt.legend()

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()

# histogram

conditions = ['Ruffles Feathers', 'Shakes Neck', 'Bobs Head', 'Dives']
variables = {
    'Male': [4, 47, 31, 16],
    'Female': [0, 22, 111, 32]
}

colors = ['blue', 'pink']

x = np.arange(len(conditions))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in variables.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute, color=colors[multiplier])
    multiplier += 1
    
ax.set_ylabel('Number of Occurances')
ax.set_title('Comparison of Male and Female Eider Behaviours')
ax.set_xticks(x)
ax.legend()

ax.xaxis.set_ticks_position('none')
ax.set_xticklabels(['Ruffles Feathers', 'Shakes Neck', 'Bobs Head', 'Dives'])

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()