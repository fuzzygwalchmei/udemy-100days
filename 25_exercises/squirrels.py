import pandas as pd

df = pd.read_csv("2018_squirrel_count.csv")

counted = df['Primary Fur Color']
counted = counted.value_counts()
counted.to_csv("squirrel_counts.csv")
