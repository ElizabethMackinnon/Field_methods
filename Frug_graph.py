import matplotlib.pyplot as plt
import numpy as np

conditions = ('In Water', 'On Lilypad')
variables = {
    'Moving':  [5, 1],
    'Not Moving': [20, 20]
}

colors = ['orange', 'green']

x = np.arange(len(conditions))
width = 0.25 
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in variables.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute, color = colors[multiplier])
    ax.bar_label(rects, padding=3)
    multiplier += 1
    
ax.set_ylabel('Number of Occurances')
ax.set_title('Frog Behavior in Different Conditions \nWith Scan and Behaviour Sampling')
ax.set_xticks(x)
ax.legend()

ax.xaxis.set_ticks_position('none')
ax.set_xticklabels(['In Water', 'On Lilypad'])

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()