import numpy as np
from sklearn import datasets
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import mysql.connector
from mysql.connector import errorcode
from sklearn.preprocessing import StandardScaler


#1
caminho_xlsx = 'downloaded_file.xlsx'
df = pd.read_excel(caminho_xlsx)
caminho_csv = 'Luso.csv'
df.to_csv(caminho_csv, index=False)

from sklearn.model_selection import train_test_split

X_train, X_test= train_test_split(df, test_size=0.3, random_state=42)

#print("\n\nX_train: \n",X_train)
#print("\n\nX_train: \n",X_test)

""""
        "SOBRENOME":"nan",
        "NOME":"José Joaquim",
        "NATURALIDADE":"Lisboa",
#       "IDADE":25.0,        
        "ESTADO_CIVIL":"solteiro",
        "OCUPACAO_PROFISSAO":"tanoeiro",
#       "DATA_DA_CHEGADA":"00\/00\/1832",
#       "ANO_CHEGADA":1832.0,
        "PROCEDENCIA":"Lisboa",
        "DESTINO":"Bahia",
#       "ANO_REGISTRO":1833.0

"""

#data_number = [df["IDADE"], df["ANO_CHEGADA"], df["ANO_REGISTRO"]]
data_number = [df["ANO_CHEGADA"], df["ANO_REGISTRO"]]
print("\n\ndata_number: ",data_number)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_number)

print(scaled_data)
