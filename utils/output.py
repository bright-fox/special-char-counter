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
        x=df["Count"], y=df["Character"], orient="h", palette="viridis"
    )
    char_plot.tick_params(left=False)

    # Add count labels to the end of each bar
    label_offset = 0.4
    for index, row in df.iterrows():
        char_plot.text(
            row["Count"] + label_offset, index, str(row["Count"]), va="center"
        )

    plt.show()
