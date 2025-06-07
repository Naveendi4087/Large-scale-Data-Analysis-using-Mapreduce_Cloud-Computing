import pandas as pd
import matplotlib.pyplot as plt
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
                data.append((sentiment, int(count)))
            except ValueError:
                continue

df = pd.DataFrame(data, columns=["Sentiment", "Count"])

df.to_csv("sentiment_distribution.csv", index=False)

print("\nSentiment Distribution:")
print(df.to_string(index=False))

plt.figure(figsize=(8, 6))
plt.bar(df["Sentiment"], df["Count"], color=["green", "blue", "red"])
plt.title("Sentiment Distribution")
plt.ylabel("Count")
plt.xlabel("Sentiment")
plt.tight_layout()

plt.savefig("sentiment_distribution.png")
plt.show()
