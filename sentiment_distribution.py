import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

output_file = 'sentimentanalysis_output.txt'

if not os.path.exists(output_file):
    print(f"Error: {output_file} not found.")
    exit(1)

data = []
with open(output_file, 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            sentiment, count = parts
            try:
                data.append((sentiment.strip(), int(count.strip())))
            except ValueError:
                continue

df = pd.DataFrame(data, columns=["Sentiment", "Count"])

def get_sentiment_label(score):
    if score == 3:
        return "Positive"
    elif score == 2:
        return "Neutral"
    elif score == 1:
        return "Negative"
    else:
        return "Unknown"

df["Category"] = df["Count"].apply(get_sentiment_label)

result = df.groupby("Category")["Count"].count()

df.to_csv("sentiment_distribution2.csv", index=False)

print("\nSentiment Distribution (Aggregated):")
print(result.to_string())

color_map = {
    "Positive": "green",
    "Neutral": "blue",
    "Negative": "red"
}

plt.figure(figsize=(6, 4))
bars = result.plot(kind="bar", color=[color_map.get(cat, "gray") for cat in result.index])

plt.title("Sentiment Distribution")
plt.ylabel("Number of Sentences")
plt.xlabel("Sentiment")
plt.xticks(rotation=0)

legend_patches = [mpatches.Patch(color=color, label=label) for label, color in color_map.items()]
plt.legend(handles=legend_patches, title="Sentiment Type")

plt.tight_layout()
plt.savefig("sentiment_distribution_summary.png")
plt.show()
