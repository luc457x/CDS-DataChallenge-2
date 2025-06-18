import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

def checkNaN(df):
    """Recebe um DataFrame e retorna a quantidade de valores nulos e não nulos."""
    null_count = df.isna().sum()
    non_null_count = df.notnull().sum()
    print(f"Null values:\n {null_count}")
    print(f"Non-null values:\n {non_null_count}")
    return

def checkOutliers(df):
    """Recebe um DataFrame e retorna um DataFrame com os outliers.
    Baseia-se no pressuposto de que os dados estão normalmente distribuídos."""
    outliers_list = []
    # Itera sobre as colunas numéricas
    for column in df.select_dtypes(include=[np.number]).columns:
        # Calcula o 1 quartil (Q1)
        Q1 = df[column].quantile(0.25)
        # Calcula o 3 quartil (Q3)
        Q3 = df[column].quantile(0.75)
        # Calcula o Intervalo Interquartil (IQR)
        IQR = Q3 - Q1
        # Define os limites inferior e superior para outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # Identifica os outliers da coluna atual e adiciona à lista
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        outliers_list.append(outliers)
    # Concatena todos os outliers identificados
    dfOutliers = pd.concat(outliers_list).drop_duplicates().reset_index(drop=True)
    return dfOutliers

def corr(df):
    plt.figure(figsize=(10,8))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True)
    plt.show()
    return

def hist(df):
    # Recebe um DataFrame e plota um histograma para cada coluna numérica.
    df.hist(bins=50, figsize=(25,10))
    plt.show()
    return

def extract_words(column_name):
    # Encontra todas as palavras dentro das aspas simples
    matches = re.findall(r'\'(.*?)\'', column_name)
    # Remove espaços extras e junta as palavras encontradas
    return ' '.join(match.strip() for match in matches)

def check_columns_for_set(column, value_set):
    """Encontra as colunas que contem apenas subconjuntos de um conjunto de valores."""
    non_nan_values = column.dropna()
    return non_nan_values.isin(value_set).all()

def to_percent(y, position):
    return f'{y * 100:.0f}%'