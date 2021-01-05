import pandas as pd
import csv


# with open("weather_data.csv") as f:
#     data = csv.reader(f)

#     for row in data:
#         print(row)

df = pd.read_csv("weather_data.csv")
# print(df['temp'])

print(df['temp'].mean())

print(df.temp.mean())

print(df[df.temp == df.temp.max()]['day'])

df['temp_f'] = df['temp'] *  9/5 + 32
print(df)
