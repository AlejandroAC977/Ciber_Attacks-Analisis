#librerias
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#lectura de datos
df = pd.read_csv(r'C:\Users\alejandro\Documents\Attacks_analisys\csv\cybersecurity_attacks.csv')

#lectura de datos principales
if __name__ == "__main__":
    print(df.head())
    print(df.info())
    print(df.describe())