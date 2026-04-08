#librearias
from data_load import df
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Ataque por hora 

# Limpieza de datos para una categoria especifica
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['hour'] = df['Timestamp'].dt.hour
df['day'] = df['Timestamp'].dt.day
df['day_of_week'] = df['Timestamp'].dt.day_name()
df['month_name'] = df['Timestamp'].dt.month_name()

print(df[['Timestamp', 'hour', 'day', 'day_of_week', 'month_name']].head())

attacks_by_hour = df['hour'].value_counts().sort_index()
print(attacks_by_hour)

# Uso de Graficas 
plt.figure(figsize=(10,5))
max_hour = attacks_by_hour.idxmax()
attacks_by_hour.plot(kind='bar', color= [
    'lightcoral' if hour == max_hour else 'lightgreen'      #hora de ataque mas alta resaltada
    for hour in attacks_by_hour.index
])
plt.title('Number of Cyber Attacks by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=0)
plt.show()

# Ataques por hora y tipo

# Agrupamiento de datos
attacks_hour_type = (
    df
    .groupby(['hour', 'Attack Type'])
    .size()
    .reset_index(name='count')
)

# pivot
print(attacks_hour_type.head())

pivot_hour_type = attacks_hour_type.pivot(
    index='hour',
    columns='Attack Type',
    values='count'
).fillna(0)

pivot_hour_type.head()

# Grafica
plt.figure(figsize=(12,6))
for attack in pivot_hour_type.columns:
    plt.plot(pivot_hour_type.index, pivot_hour_type[attack], label=attack)

plt.title('Cyber Attacks by Hour and Attack Type')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Attacks')
plt.legend()
plt.xticks(range(0,24))
plt.show()

# Mapa de Calor 

# Agrupamiento
heatmap_data = (
    df
    .groupby(['day_of_week', 'hour'])
    .size()
    .reset_index(name='count')
)
# Pivot
heatmap_pivot = heatmap_data.pivot(
    index='day_of_week',
    columns='hour',
    values='count'
)
# orden del index
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
              'Friday', 'Saturday', 'Sunday']
heatmap_pivot = heatmap_pivot.reindex(days_order)

# Grafica con Seaborn
plt.figure(figsize=(14,6))
sns.heatmap(
    heatmap_pivot,
    cmap='Reds',
    linewidths=0.5
)

plt.title('Heatmap of Cyber Attacks by Day of Week and Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.show()
