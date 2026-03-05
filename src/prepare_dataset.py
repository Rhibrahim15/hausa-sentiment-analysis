import pandas as pd

# load datasets
train = pd.read_csv("data/train.tsv", sep="\t")
dev = pd.read_csv("data/dev.tsv", sep="\t")
neutral = pd.read_csv("data/hausa_neutral.tsv", sep="\t")

# combine datasets
df = pd.concat([train, dev, neutral], ignore_index=True)

# rename column from tweet → text
df = df.rename(columns={"tweet": "text"})

# keep only necessary columns
df = df[["text", "label"]]

# save combined dataset
df.to_csv("data/hausa_sentiment.csv", index=False)

print("Dataset prepared successfully")
print(df.head())