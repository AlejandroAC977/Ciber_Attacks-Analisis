from data_load import df
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# agrupamineto de horas
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['hour'] = df['Timestamp'].dt.hour
df['day'] = df['Timestamp'].dt.day
df['day_of_week'] = df['Timestamp'].dt.day_name()
df['month_name'] = df['Timestamp'].dt.month_name()
attacks_by_hour = df['hour'].value_counts().sort_index()

# Numero de ataques por gravedad
severity_counts = df['Severity Level'].value_counts()
print(severity_counts)

# Grafica Numero de ataques por gravedad
max_attacks = severity_counts.idxmax()
severity_counts.plot(
    kind='bar', color= [
    'lightcoral' if hour == max_attacks else 'lightgreen'      #mayor tipo de ataque
    for hour in severity_counts.index
    ],
    figsize=(8,5),
    title='Distribution of Cyber Attacks by Severity Level'
)

plt.xlabel('Severity Level')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=0)
plt.show()

# Gravedad por hora
severity_by_hour = (
    df
    .groupby(['hour', 'Severity Level'])
    .size()
    .reset_index(name='count')
)

print(severity_by_hour.head())

# pivot 
pivot_severity_hour = severity_by_hour.pivot(
    index='hour',
    columns='Severity Level',
    values='count'
).fillna(0)

print(pivot_severity_hour.head())

# Grafica plt
plt.figure(figsize=(12,6))
for severity in pivot_severity_hour.columns:
    plt.plot(
        pivot_severity_hour.index,
        pivot_severity_hour[severity],
        marker='o',
        label=severity
    )
plt.title('Cyber Attacks by Hour and Severity Level')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Attacks')
plt.xticks(range(0,24))
plt.legend(title='Severity Level')
plt.grid(alpha=0.3)
plt.show()

# Agrupamiento de Gravedad por tipo
severity_by_type = (
    df
    .groupby(['Attack Type', 'Severity Level'])
    .size()
    .reset_index(name='count')
)
print(severity_by_type.head())

# pivot
pivot_severity_type = severity_by_type.pivot(
    index='Attack Type',
    columns='Severity Level',
    values='count'
).fillna(0)
print(pivot_severity_type)

# Grafica
pivot_severity_type.plot(
    kind='bar',
    stacked=True,
    figsize=(10,6)
)
plt.title('Severity Level Distribution by Attack Type')
plt.xlabel('Attack Type')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=0)
plt.legend(title='Severity Level')
plt.show()