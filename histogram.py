import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('benchmark_res.csv')

df.sort_values('Replicas', inplace=True)

plt.figure(figsize=(10, 6))
plt.bar(df['Replicas'].astype(str), df['Req/Sec (Average)'], color='skyblue', edgecolor='black', width=1.0) 

plt.xlabel('Number of Replicas')
plt.ylabel('Requests Per Second (Average)')

for index, value in enumerate(df['Req/Sec (Average)']):
    plt.text(index, value, str(value), ha='center')

plt.savefig('histogram.png')
