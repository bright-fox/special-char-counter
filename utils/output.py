import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def write_to_file(results):
    with open("results.txt", "w") as f:
        f.write(json.dumps(results))


def display_plot(results):
    df = pd.DataFrame(results, columns=["Character", "Count"])
    char_plot = sns.barplot(
        x=df["Count"],
        y=df["Character"],
        orient="h",
    )
    char_plot.tick_params(left=False)
    plt.show()
