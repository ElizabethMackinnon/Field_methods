import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Scatterplot of instantaneous data

data = {
    'x': [4.5, 16, 4, 2.5, 1, 3.5, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
    'y': [3, 0, 0, 1, 1, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    'colors': ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'orange', 'pink', '#B2BEB5',
               '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5'],
    'label': ['Pacing', 'Panting', 'Laying down', 'walking', 'Running', 'Standing', 'Trotting',
              'observing', 'Sniffing', 'Scratching', 'Eating', 'Sneezing', 'Vocalizing', 'Digging',
              'Drinking', 'Playing']
}

df = pd.DataFrame(data)

for i in range(len(df)):
    plt.scatter(df['x'][i], df['y'][i], color=df['colors'][i], label=df['label'][i])

plt.xlabel('Times Behaviour Actually Happened')
plt.ylabel('Times Behaviour Was Reported Differently')
plt.title('Instantaneous Observations of Arctic Wolf Behaviour \nat Shubenacadie Wildlife Park')

plt.legend()

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()

# scatterplot of interval data

data = {
    'x': [1.5, 20, 14, 2.5, 0, 6, 0.5, 1.5, 2, 0, 0, 0, 0, 0, 0, 0], 
    'y': [1, 0, 1, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    'colors': ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'orange', 'pink', 'maroon',
               '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5', '#B2BEB5'],
    'label': ['Pacing', 'Panting', 'Laying down', 'walking', 'Running', 'Standing', 'Trotting',
              'observing', 'Sniffing', 'Scratching', 'Eating', 'Sneezing', 'Vocalizing', 'Digging',
              'Drinking', 'Playing']
}

df = pd.DataFrame(data)

for i in range(len(df)):
    plt.scatter(df['x'][i], df['y'][i], color=df['colors'][i], label=df['label'][i])

plt.xlabel('Times Behaviour Actually Happened')
plt.ylabel('Times Behaviour Was Reported Differently')
plt.title('Interval Observations of Arctic Wolf Behaviour \nat Shubenacadie Wildlife Park')

plt.legend()

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()