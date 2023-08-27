import os
import sys
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from collections import defaultdict

if not sys.argv[1]:
    raise Exception("Please provide a path..")

path = sys.argv[1]
if not os.path.exists(path):
    raise Exception("Please provide a valid")

path = os.path.abspath(path)
bigram_counter = defaultdict(lambda: 0)

for file_path in glob.iglob(path + '/**/*.ts', recursive=True):
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('import'):
                continue

            first_char = None
            for char in line:
                if (char.isalnum() or char.isspace()):
                    first_char = None
                    continue

                if (first_char is not None):
                    bigram_counter[f'{first_char}{char}'] += 1

                first_char = char

# visualize the occurences in a bar plot
sorted_counter = sorted(bigram_counter.items(), key=lambda i: -i[1])

df = pd.DataFrame(sorted_counter, columns=['Bigram', 'Count'])
char_plot = sns.barplot(
    x=df['Count'],
    y=df['Bigram'],
    orient='h',
)
char_plot.tick_params(left=False)
plt.show()
