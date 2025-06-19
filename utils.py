import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('future.no_silent_downcasting', True)

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
    plt.figure(figsize=(20,16))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True)
    plt.show()
    return

def hist(df):
    # Recebe um DataFrame e plota um histograma para cada coluna numérica.
    df.hist(bins=50, figsize=(25,16))
    plt.show()
    return

def extract_words(column_name):
    # Encontra todas as palavras dentro das aspas simples
    matches = re.findall(r"\'(.*?)\'", column_name)
    # Remove espaços extras e junta as palavras encontradas
    return ' '.join(match.strip() for match in matches)

def check_columns_for_set(column, value_set):
    """Encontra as colunas que contem apenas subconjuntos de um conjunto de valores."""
    non_nan_values = column.dropna()
    return non_nan_values.isin(value_set).all()

def to_percent(y, position):
    return f'{y * 100:.0f}%'


def extract_last_number(text):
    # Verifica se o input é diferente de string ou Series do pandas
    if not isinstance(text, (str, pd.Series)):
        # Retorna o própio input
        return text
    # Verifica se o input é uma string
    if isinstance(text, str):
        # Regex para encontrar todos os números na string
        numbers = re.findall(r"\b\d[\d.,]*\b", text)
        # Se houver pelo menos dois números, retorna o último
        if len(numbers) > 1:
            return numbers[-1]
        # Se houver apenas um número, retorna esse número
        elif len(numbers) == 1:
            return numbers[0]
        # Se não houver números, retorna 0
        else:
            return 0
    # Verifica se o input é uma Series do pandas
    elif isinstance(text, pd.Series):
        # Aplica a função a cada elemento da Series, a transformando em string
        return text.apply(extract_last_number)
    
def calc_percent(val, total):
    return val.div((total), fill_value=0).replace([np.inf, -np.inf], 0)
