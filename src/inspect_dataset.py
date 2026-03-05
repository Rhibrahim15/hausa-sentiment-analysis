import pandas as pd

# read train file
train = pd.read_csv("data/train.tsv", sep="\t")

print("TRAIN DATA")
print(train.head())
print(train.columns)

# read dev file
dev = pd.read_csv("data/dev.tsv", sep="\t")

print("\nDEV DATA")
print(dev.head())
print(dev.columns)

# read neutral file
neutral = pd.read_csv("data/hausa_neutral.tsv", sep="\t")

print("\nNEUTRAL DATA")
print(neutral.head())
print(neutral.columns)

